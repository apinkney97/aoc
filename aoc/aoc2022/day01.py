def parse_data(data):
    parsed = []
    current = []
    for row in data:
        if not row:
            parsed.append(current)
            current = []
        else:
            current.append(int(row))
    if current:
        parsed.append(current)
    return parsed


def part1(data) -> int:
    return max(sum(elf) for elf in data)


def part2(data) -> int:
    return sum(sorted(sum(elf) for elf in data)[-3:])
