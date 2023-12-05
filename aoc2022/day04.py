import re

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2022, 4, example=EXAMPLE)
    parsed = []
    for line in data:
        parts = [int(part) for part in re.split("[,-]", line)]
        elf1 = set(range(parts[0], parts[1] + 1))
        elf2 = set(range(parts[2], parts[3] + 1))
        parsed.append((elf1, elf2))

    return parsed


DATA = load_data()


def part1() -> int:
    total = 0
    for elf1, elf2 in DATA:
        if elf1.issubset(elf2) or elf1.issuperset(elf2):
            total += 1
    return total


def part2() -> int:
    total = 0
    for elf1, elf2 in DATA:
        if elf1 & elf2:
            total += 1
    return total


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
