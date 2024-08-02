from aoc.utils import BACKGROUND_BLOCK, FOREGROUND_BLOCK


def parse_data(data):
    instructions = []
    for line in data:
        if line != "noop":
            instructions.append("noop")
        instructions.append(line)

    return instructions


def part1(data) -> int:
    x = 1

    total = 0
    for cycle, instruction in enumerate(data, start=1):
        if cycle in {20, 60, 100, 140, 180, 220}:
            total += cycle * x

        if instruction != "noop":
            value = int(instruction.split()[1])
            x += value
    return total


def part2(data) -> int:
    sprite_x = 1

    for cycle, instruction in enumerate(data, start=0):
        if sprite_x - 1 <= cycle % 40 <= sprite_x + 1:
            print(FOREGROUND_BLOCK, end="")
        else:
            print(BACKGROUND_BLOCK, end="")

        if (cycle + 1) % 40 == 0:
            print()

        if instruction != "noop":
            value = int(instruction.split()[1])
            sprite_x += value

    return 0
