import itertools

type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    return [[int(i) for i in line.split()] for line in data]


def reduce(line: list[int]) -> list[int]:
    return [b - a for a, b in itertools.pairwise(line)]


def extrapolate(line: list[int]) -> int:
    next_lines = [line]

    while len(set(line)) > 1:
        line = reduce(line)
        next_lines.append(line)

    return sum(line[-1] for line in next_lines)


def part1(data: Data) -> int:
    return sum(extrapolate(line) for line in data)


def part2(data: Data) -> int:
    return sum(extrapolate(line[::-1]) for line in data)
