def part1(data) -> int:
    total = 0
    group = set()
    for line in data:
        if not line:
            total += len(group)
            group = set()
        else:
            group |= set(line)

    total += len(group)

    return total


def part2(data) -> int:
    total = 0
    group = None
    for line in data:
        if not line:
            total += len(group)
            group = None
        else:
            if group is None:
                group = set(line)
            else:
                group &= set(line)
    total += len(group)

    return total
