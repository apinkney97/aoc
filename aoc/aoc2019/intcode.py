import asyncio
from enum import Enum, auto
from typing import Callable, List, Mapping, NamedTuple, Optional, Tuple, Union


def parse_data(data):
    return [int(i) for i in data[0].split(",")]


class RunState(Enum):
    NOT_STARTED = auto()
    RUNNING = auto()
    AWAITING_INPUT = auto()
    TERMINATED = auto()


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class ParameterDirection(Enum):
    IN = auto()
    OUT = auto()


class Op(Enum):
    ADD = 1
    MUL = 2
    INP = 3
    PRT = 4
    JNZ = 5
    JEZ = 6
    LT = 7
    EQ = 8
    ROF = 9
    HLT = 99


class OpSpec(NamedTuple):
    type: Op
    params: List[ParameterDirection]
    func: Callable


def nop(*args):
    pass


OPERATIONS: List[OpSpec] = [
    OpSpec(
        type=Op.ADD,
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: args[0] + args[1],
    ),
    OpSpec(
        type=Op.MUL,
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: args[0] * args[1],
    ),
    OpSpec(
        type=Op.INP,
        params=[ParameterDirection.OUT],
        func=nop,
    ),
    OpSpec(type=Op.PRT, params=[ParameterDirection.IN], func=nop),
    OpSpec(
        type=Op.JNZ, params=[ParameterDirection.IN, ParameterDirection.IN], func=nop
    ),
    OpSpec(
        type=Op.JEZ, params=[ParameterDirection.IN, ParameterDirection.IN], func=nop
    ),
    OpSpec(
        type=Op.LT,
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: 1 if args[0] < args[1] else 0,
    ),
    OpSpec(
        type=Op.EQ,
        params=[ParameterDirection.IN, ParameterDirection.IN, ParameterDirection.OUT],
        func=lambda *args: 1 if args[0] == args[1] else 0,
    ),
    OpSpec(type=Op.ROF, params=[ParameterDirection.IN], func=nop),
    OpSpec(type=Op.HLT, params=[], func=nop),
]


OPERATION_MAP: Mapping[Op, OpSpec] = {o.type: o for o in OPERATIONS}


class BadOpCode(Exception):
    def __init__(self, opcode, encoded_opcode, state_dump):
        super().__init__(
            f"Unknown opcode: {opcode} (from {encoded_opcode})  {state_dump}"
        )


class Memory:
    def __init__(self, initial_value: List[int]):
        self._memory = initial_value[:]

    def _expand(self, limit_or_slice: Union[int, slice]):
        mem_size = len(self._memory)

        if isinstance(limit_or_slice, slice):
            max_index = max(limit_or_slice.start, limit_or_slice.stop - 1)
        else:
            max_index = limit_or_slice

        if max_index >= mem_size:
            # double the size until we're within the limit
            while mem_size <= max_index:
                mem_size *= 2

            self._memory.extend([0] * (mem_size - len(self._memory)))

    def __getitem__(self, item):
        self._expand(item)
        return self._memory[item]

    def __setitem__(self, item, value):
        self._expand(item)
        self._memory[item] = value

    def __len__(self):
        return len(self._memory)


class IntCodeProcessor:
    __instance_counter = 0

    def __init__(self, initial_memory: List[int], verbosity=0):
        cls = type(self)
        self.id = cls.__instance_counter
        cls.__instance_counter += 1
        self._stdin = asyncio.Queue()
        self._stdout = asyncio.Queue()
        self._pc = 0
        self._sp = 0
        self._memory = Memory(initial_memory)
        self._state = RunState.NOT_STARTED
        self._verbosity = verbosity

    @property
    def state(self):
        return self._state

    def dump_state(self) -> str:
        return f"{self._pc=} {self._sp=} {len(self._memory)=} {self._state=}"

    def decode_opcode(self, encoded_opcode: int) -> Tuple[OpSpec, List[ParameterMode]]:
        encoded_modes, opcode = divmod(encoded_opcode, 100)
        try:
            op_enum = Op(opcode)
        except ValueError:
            raise BadOpCode(opcode, encoded_opcode, self.dump_state()) from None

        op_spec = OPERATION_MAP[op_enum]

        modes = []
        for _ in range(len(op_spec.params)):
            encoded_modes, mode = divmod(encoded_modes, 10)
            modes.append(ParameterMode(mode))

        return op_spec, modes

    def log(self, *args, verbosity=1):
        if verbosity <= self._verbosity:
            print(f"{self.id:4d}:", *args)

    async def input(self, val):
        await self._stdin.put(val)

    async def output(self):
        return await self._stdout.get()

    def _get_param_addresses(self, modes: List[ParameterMode]) -> List[int]:
        # Given the parameter modes, returns the addresses that should be read from or written to
        param_addrs = []
        for addr, mode in enumerate(modes, start=self._pc + 1):
            if mode is ParameterMode.IMMEDIATE:
                parsed_arg = addr
            elif mode is ParameterMode.POSITION:
                parsed_arg = self._memory[addr]
            elif mode is ParameterMode.RELATIVE:
                parsed_arg = self._memory[addr] + self._sp
            else:
                raise Exception(f"Unhandled parameter mode: {mode.name}")

            param_addrs.append(parsed_arg)

        return param_addrs

    def _handle_jump(self, op_spec: OpSpec, param_addrs: List[int]):
        check = self._memory[param_addrs[0]]
        jump_to = self._memory[param_addrs[1]]

        do_jump = False
        if op_spec.type is Op.JEZ:
            do_jump = check == 0
        elif op_spec.type is Op.JNZ:
            do_jump = check != 0

        if do_jump:
            self._pc = jump_to
        else:
            self._pc += len(op_spec.params) + 1

    async def _handle_io(
        self, op_spec: OpSpec, param_addrs: List[int]
    ) -> Optional[int]:
        if op_spec.type is Op.INP:
            if self._stdin.empty():
                self.log("Awaiting input")

            self._state = RunState.AWAITING_INPUT
            val = await self._stdin.get()
            self._state = RunState.RUNNING

            self.log("<--", val)
            return val

        if op_spec.type is Op.PRT:
            val = self._memory[param_addrs[0]]
            self.log("-->", val)
            await self._stdout.put(val)
            return None

        raise Exception(f"Unhandled IO operation {op_spec.type.name}")

    def has_output(self):
        return not self._stdout.empty()

    def log_instruction(
        self,
        encoded_opcode: int,
        op_spec: OpSpec,
        param_addrs: List[int],
        arg_modes: List[ParameterMode],
    ):
        if self._verbosity < 2:
            return

        args = self._memory[self._pc + 1 : self._pc + len(op_spec.params) + 1]
        formatted_args = []
        for arg, arg_mode in zip(args, arg_modes):
            if arg_mode is ParameterMode.IMMEDIATE:
                formatted_args.append(f"{arg}")
            elif arg_mode is ParameterMode.POSITION:
                formatted_args.append(f"[{arg}]")
            elif arg_mode is ParameterMode.RELATIVE:
                formatted_args.append(f"<{arg}>")

        formatted_args = ", ".join(formatted_args)
        arg_vals = ", ".join(str(self._memory[addr]) for addr in param_addrs)

        self.log(
            f"PC {self._pc:5d} SP: {self._sp:5d}   op: {encoded_opcode:5d}   {op_spec.type.name:4s}"
            f"{formatted_args:30s}   {str(param_addrs):30s}   {arg_vals}",
            verbosity=2,
        )

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

        while True:
            encoded_opcode = self._memory[self._pc]
            op_spec, modes = self.decode_opcode(encoded_opcode)

            param_addrs = self._get_param_addresses(modes)

            self.log_instruction(encoded_opcode, op_spec, param_addrs, modes)

            if op_spec.type is Op.HLT:
                self.log("HALT")
                if not self._stdin.empty():
                    self.log(f"WARNING: unused input: {self._stdin}")
                break

            if op_spec.type in {Op.JEZ, Op.JNZ}:
                self._handle_jump(op_spec, param_addrs)
                continue

            result = None

            if op_spec.type in {Op.INP, Op.PRT}:
                result = await self._handle_io(op_spec, param_addrs)

            elif op_spec.type is Op.ROF:
                self._sp += self._memory[param_addrs[0]]

            else:
                result = op_spec.func(*(self._memory[addr] for addr in param_addrs))

            if result is not None:
                for direction, addr in zip(op_spec.params, param_addrs):
                    if direction is ParameterDirection.OUT:
                        self._memory[addr] = result
                        self.log(f"Setting mem[{addr}] == {result}", verbosity=3)

            self._pc += len(op_spec.params) + 1

        self._state = RunState.TERMINATED

        if not return_last_output:
            return None

        if self._stdout.empty():
            self.log("WARN: No output")

        elif self._stdout.qsize() > 1:
            self.log("WARN: Multiple output values")

        value = None

        while not self._stdout.empty():
            value = self._stdout.get_nowait()

        return value
