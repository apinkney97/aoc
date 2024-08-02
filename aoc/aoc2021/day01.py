from aoc import utils


def parse_data(data):
    data = utils.parse_data(data, fn=int)

    return data


def part1(data) -> int:
    return count_increases(data)


def count_increases(data):
    increases = 0
    for i, j in zip(data, data[1:]):
        if j > i:
            increases += 1
    return increases


def part2(data) -> int:
    windows = [sum(x) for x in zip(data, data[1:], data[2:])]
    return count_increases(windows)
