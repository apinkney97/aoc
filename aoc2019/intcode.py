import asyncio
from enum import Enum, auto
from typing import Callable, List, Mapping, NamedTuple, Optional, Tuple


class RunState(Enum):
    NOT_STARTED = auto()
    RUNNING = auto()
    TERMINATED = auto()


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class ParameterDirection(Enum):
    IN = auto()
    OUT = auto()


class Operation(NamedTuple):
    name: str
    params: List[ParameterDirection]
    func: Callable


def nop(*args):
    pass


OPERATIONS: Mapping[int, Operation] = {
    1: Operation(
        name="ADD",
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: args[0] + args[1],
    ),
    2: Operation(
        name="MUL",
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: args[0] * args[1],
    ),
    3: Operation(name="INPUT", params=[ParameterDirection.OUT], func=nop,),
    4: Operation(name="PRINT", params=[ParameterDirection.IN], func=nop),
    5: Operation(
        name="JNZ", params=[ParameterDirection.IN, ParameterDirection.IN], func=nop
    ),
    6: Operation(
        name="JZ", params=[ParameterDirection.IN, ParameterDirection.IN], func=nop
    ),
    7: Operation(
        name="LT",
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: 1 if args[0] < args[1] else 0,
    ),
    8: Operation(
        name="EQ",
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: 1 if args[0] == args[1] else 0,
    ),
    99: Operation(name="halt", params=[], func=nop),
}


JUMP_OPCODES = {5, 6}
IO_OPCODES = {3, 4}


class BadOpCode(Exception):
    def __init__(self, opcode):
        super().__init__(f"Unknown opcode: {opcode}")


class IntCodeProcessor:
    __instance_counter = 0

    def __init__(self, initial_memory: List[int], verbose=False):
        cls = type(self)
        self.id = cls.__instance_counter
        cls.__instance_counter += 1
        self._input = asyncio.Queue()
        self._output = asyncio.Queue()
        self._ip = 0
        self._memory = initial_memory[:]
        self._state = RunState.NOT_STARTED
        self._verbose = verbose

    @property
    def state(self):
        return self._state

    @staticmethod
    def decode_opcode(encoded_opcode: int) -> Tuple[int, List[ParameterMode]]:
        encoded_modes, opcode = divmod(encoded_opcode, 100)
        if opcode not in OPERATIONS:
            raise BadOpCode(opcode)

        modes = []
        for _ in range(len(OPERATIONS[opcode].params)):
            encoded_modes, mode = divmod(encoded_modes, 10)
            modes.append(ParameterMode(mode))

        return opcode, modes

    def log(self, *args):
        if self._verbose:
            print(f"{self.id:4d}:", *args)

    async def input(self, val):
        await self._input.put(val)

    async def output(self):
        return await self._output.get()

    def _parse_args(self, args: List[int], modes: List[ParameterMode]) -> List[int]:
        return [
            arg if mode is ParameterMode.IMMEDIATE else self._memory[arg]
            for arg, mode in zip(args, modes)
        ]

    def _handle_jump(self, op: Operation, parsed_args: List[int]):
        check, jump_to = parsed_args
        do_jump = False
        if op.name == "JZ":
            do_jump = check == 0
        elif op.name == "JNZ":
            do_jump = check != 0

        if do_jump:
            self._ip = jump_to
        else:
            self._ip += len(op.params) + 1

    async def _handle_io(self, op: Operation, parsed_args: List[int]) -> Optional[int]:
        if op.name == "INPUT":
            if self._input.empty():
                self.log("Awaiting input")

            val = await self._input.get()
            self.log("<--", val)
            return val

        if op.name == "PRINT":
            self.log("-->", *parsed_args)
            await self._output.put(parsed_args[0])
            return None

        raise Exception(f"Unhandled IO operation {op.name}")

    async def run(self, noun: int = None, verb: int = None, return_last_output=False):
        if self._state is not RunState.NOT_STARTED:
            raise Exception(
                f"Can't run {type(self).__name__} in state {self._state.name}"
            )

        self._state = RunState.RUNNING

        if noun is not None:
            self._memory[1] = noun
        if verb is not None:
            self._memory[2] = verb

        while self._ip < len(self._memory):
            encoded_opcode = self._memory[self._ip]
            opcode, modes = self.decode_opcode(encoded_opcode)

            op = OPERATIONS[opcode]

            args = self._memory[self._ip + 1 : self._ip + len(op.params) + 1]
            parsed_args = self._parse_args(args, modes)

            if opcode == 99:
                self.log("HALT")
                if not self._input.empty():
                    self.log(f"WARNING: unused input: {self._input}")
                break

            if opcode in JUMP_OPCODES:
                self._handle_jump(op, parsed_args)
                continue

            if opcode in IO_OPCODES:
                result = await self._handle_io(op, parsed_args)

            else:
                result = op.func(*parsed_args)

            if result is not None:
                for param_direction, arg in zip(op.params, args):
                    if param_direction is ParameterDirection.OUT:
                        self._memory[arg] = result

            self._ip += len(op.params) + 1

        self._state = RunState.TERMINATED

        if not return_last_output:
            return None

        if self._output.empty():
            self.log("WARN: No output")

        elif self._output.qsize() > 1:
            self.log("WARN: Multiple output values")

        value = None

        while not self._output.empty():
            value = self._output.get_nowait()

        return value
