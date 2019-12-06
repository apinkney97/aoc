from enum import Enum, auto
from typing import Callable, List, Mapping, NamedTuple, Tuple

from aoc2019 import utils


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
    3: Operation(
        name="INPUT",
        params=[ParameterDirection.OUT],
        func=lambda *args: int(input("Enter value: ").strip()),
    ),
    4: Operation(name="PRINT", params=[ParameterDirection.IN], func=print),
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


class BadOpCode(Exception):
    def __init__(self, opcode):
        super().__init__(f"Unknown opcode: {opcode}")


class IntCodeProcessor:
    def __init__(self, initial_memory):
        self._ip = 0
        self._memory = initial_memory[:]

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

    def run(self, noun: int = None, verb: int = None):
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
                print("HALT")
                break

            if opcode in JUMP_OPCODES:
                self._handle_jump(op, parsed_args)
                continue

            result = op.func(*parsed_args)

            for param_direction, arg in zip(op.params, args):
                if param_direction is ParameterDirection.OUT:
                    self._memory[arg] = result

            self._ip += len(op.params) + 1

        return self._memory[0]


def intcode_eval(noun: int = None, verb: int = None) -> int:
    data = [int(i) for i in utils.load_data(5)[0].split(",")]
    t = IntCodeProcessor(data)
    return t.run(noun, verb)


def main() -> None:
    intcode_eval()


if __name__ == "__main__":
    main()
