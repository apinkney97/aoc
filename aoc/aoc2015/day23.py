from rich import print

from aoc import config
from aoc.utils import pprint

type Instruction = list[str]
type Data = list[Instruction]


def parse_data(data: list[str]) -> Data:
    instructions = []
    for line in data:
        instructions.append(line.split())

    return instructions


def part1(data: Data, a_initial_value: int = 0) -> int:
    registers = {"a": a_initial_value, "b": 0}
    pc = 0
    while True:
        if pc < 0 or pc >= len(data):
            if config.DEBUG:
                print("PC out of bounds:", pc)
            break

        inst = data[pc]
        if config.DEBUG:
            print()
            print(registers)
            for i, instruction in enumerate(data):
                print(i, " ".join(instruction), " | <---------" if i == pc else " |")
            input("Hit enter to continue")

        match inst:
            case "hlf", r:
                registers[r] //= 2
                pc += 1
            case "tpl", r:
                registers[r] *= 3
                pc += 1
            case "inc", r:
                registers[r] += 1
                pc += 1
            case "jmp", offset:
                pc += int(offset)
            case "jie", r, offset:
                pc += int(offset) if registers[r[0]] % 2 == 0 else 1
            case "jio", r, offset:
                pc += int(offset) if registers[r[0]] == 1 else 1

    if config.DEBUG:
        pprint(registers)
    return registers["b"]


def part2(data: Data) -> int:
    return part1(data, a_initial_value=1)
