type Data = list[str]


def part1(data: Data) -> int:
    total = 0
    group: set[str] = set()
    for line in data:
        if not line:
            total += len(group)
            group = set()
        else:
            group |= set(line)

    total += len(group)

    return total


def part2(data: Data) -> int:
    total = 0
    group: set[str] | None = None
    for line in data:
        if not line:
            assert group is not None
            total += len(group)
            group = None
        else:
            if group is None:
                group = set(line)
            else:
                assert group is not None
                group &= set(line)
    assert group is not None
    total += len(group)

    return total
