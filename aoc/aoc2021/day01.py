type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(line) for line in data]


def part1(data: Data) -> int:
    return count_increases(data)


def count_increases(data: Data) -> int:
    increases = 0
    for i, j in zip(data, data[1:]):
        if j > i:
            increases += 1
    return increases


def part2(data: Data) -> int:
    windows = [sum(x) for x in zip(data, data[1:], data[2:])]
    return count_increases(windows)
