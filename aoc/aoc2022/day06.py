import more_itertools

type Data = list[str]


def part1(data: Data, window: int = 4) -> int:
    for i, group in enumerate(more_itertools.windowed(data[0], window), start=window):
        if len(set(group)) == window:
            return i
    return -1


def part2(data: Data) -> int:
    return part1(data, window=14)
