import enum

import utils


class Instruction(enum.Enum):
    NOP = "nop"
    JMP = "jmp"
    ACC = "acc"


def _parse(data: str):
    inst, _, val = data.partition(" ")
    return Instruction(inst), int(val)


DATA = utils.load_data(2020, 8, fn=_parse)


def run(data):
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


def part1() -> int:
    return run(DATA)[2]


def part2() -> int:
    for i, (inst, val) in enumerate(DATA):
        if inst is Instruction.ACC:
            continue

        data = list(DATA)
        new_inst = Instruction.NOP if inst is Instruction.JMP else Instruction.JMP
        data[i] = [new_inst, val]

        terminated, pc, acc = run(data)

        if terminated:
            return acc


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
