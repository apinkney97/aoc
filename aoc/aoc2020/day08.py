import enum

type Data = list[tuple[Instruction, int]]


class Instruction(enum.Enum):
    NOP = "nop"
    JMP = "jmp"
    ACC = "acc"


def parse_data(data: list[str]) -> Data:
    def _parse(data_line: str) -> tuple[Instruction, int]:
        inst, _, val = data_line.partition(" ")
        return Instruction(inst), int(val)

    return [_parse(line) for line in data]


def run(data: Data) -> tuple[bool, int, int]:
    acc = 0
    pc = 0
    visited = set()

    while True:
        if pc < 0:
            raise Exception(f"PC went negative: {pc}")

        if pc in visited:
            return False, pc, acc

        visited.add(pc)

        try:
            inst, val = data[pc]
        except IndexError:
            return True, pc, acc

        inc = 1

        if inst is Instruction.NOP:
            pass

        elif inst is Instruction.ACC:
            acc += val

        elif inst is Instruction.JMP:
            inc = val

        else:
            raise Exception(f"Bad instruction {inst}")

        pc += inc


def part1(data: Data) -> int:
    return run(data)[2]


def part2(data: Data) -> int:
    for i, (inst, val) in enumerate(data):
        if inst is Instruction.ACC:
            continue

        data_copy = list(data)
        new_inst = Instruction.NOP if inst is Instruction.JMP else Instruction.JMP
        data_copy[i] = (new_inst, val)

        terminated, pc, acc = run(data_copy)

        if terminated:
            return acc

    raise Exception("No solution found")
