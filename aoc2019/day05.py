from enum import Enum, auto
from typing import Callable, List, Mapping, NamedTuple, Optional, Tuple

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
    def __init__(self, initial_memory: List[int], auto_input: List[int] = None):
        self._auto_input = list(reversed(auto_input or []))
        self._output = []
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

    def _handle_io(self, op: Operation, parsed_args: List[int]) -> Optional[int]:
        if op.name == "INPUT":
            if self._auto_input:
                return self._auto_input.pop()
            else:
                return int(input("Enter a value: ").strip())

        if op.name == "PRINT":
            print(*parsed_args)
            self._output.append(parsed_args[0])
            return None

        raise Exception(f"Unhandled IO operation {op.name}")

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
                if self._auto_input:
                    print(f"WARNING: unused input: {list(reversed(self._auto_input))}")
                break

            if opcode in JUMP_OPCODES:
                self._handle_jump(op, parsed_args)
                continue

            if opcode in IO_OPCODES:
                result = self._handle_io(op, parsed_args)

            else:
                result = op.func(*parsed_args)

            if result is not None:
                for param_direction, arg in zip(op.params, args):
                    if param_direction is ParameterDirection.OUT:
                        self._memory[arg] = result

            self._ip += len(op.params) + 1

        if len(self._output) == 0:
            print("WARN: No output")
            return None

        if len(self._output) > 1:
            print("WARN: Multiple output values")

        return self._output[-1]


def intcode_eval(
    auto_input: List[int] = None, noun: int = None, verb: int = None
) -> int:
    memory = [int(i) for i in utils.load_data(5)[0].split(",")]
    t = IntCodeProcessor(memory, auto_input)
    return t.run(noun, verb)


def part1():
    return intcode_eval([1])


def part2():
    return intcode_eval([5])


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
