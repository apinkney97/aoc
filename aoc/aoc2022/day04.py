import re


def parse_data(data):
    parsed = []
    for line in data:
        parts = [int(part) for part in re.split("[,-]", line)]
        elf1 = set(range(parts[0], parts[1] + 1))
        elf2 = set(range(parts[2], parts[3] + 1))
        parsed.append((elf1, elf2))

    return parsed


def part1(data) -> int:
    total = 0
    for elf1, elf2 in data:
        if elf1.issubset(elf2) or elf1.issuperset(elf2):
            total += 1
    return total


def part2(data) -> int:
    total = 0
    for elf1, elf2 in data:
        if elf1 & elf2:
            total += 1
    return total
