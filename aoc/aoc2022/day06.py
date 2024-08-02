import more_itertools


def part1(data, window=4) -> int:
    for i, group in enumerate(more_itertools.windowed(data[0], window), start=window):
        if len(set(group)) == window:
            return i
    return -1


def part2(data) -> int:
    return part1(data, window=14)
