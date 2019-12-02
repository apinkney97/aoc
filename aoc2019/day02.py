import operator

from aoc2019 import utils


OPCODES = {
    1: (4, operator.add),
    2: (4, operator.mul),
}


def intcode_eval(noun: int, verb: int) -> int:
    data = utils.load_data(2)[0]

    memory = [int(i) for i in data.split(",")]
    memory[1] = noun
    memory[2] = verb

    ip = 0

    while (opcode := memory[ip]) in OPCODES:
        nargs, op = OPCODES[opcode]
        args = memory[ip + 1 : ip + nargs]

        result = op(memory[args[0]], memory[args[1]])

        memory[args[2]] = result
        ip += nargs

    return memory[0]


def part1() -> int:
    return intcode_eval(12, 2)


def part2() -> int:
    needle = 19690720
    for noun in range(100):
        for verb in range(100):
            if intcode_eval(noun, verb) == needle:
                return 100 * noun + verb

    return -1


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
