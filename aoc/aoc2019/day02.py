import operator

type Data = list[int]

OPCODES = {
    1: (4, operator.add),
    2: (4, operator.mul),
}


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split(",")]


def intcode_eval(memory: Data, noun: int, verb: int) -> int:
    memory = memory[:]
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


def part1(data: Data) -> int:
    return intcode_eval(data, 12, 2)


def part2(data: Data) -> int:
    needle = 19690720
    for noun in range(100):
        for verb in range(100):
            if intcode_eval(data, noun, verb) == needle:
                return 100 * noun + verb

    return -1
