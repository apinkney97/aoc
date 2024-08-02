from statistics import mean, median_high, median_low

from aoc import utils


def parse_data(data):
    return [int(i) for i in data[0].split(",")]


def part1(data) -> int:
    return min(
        sum(abs(i - pos) for i in data) for pos in (median_low(data), median_high(data))
    )


def part2(data) -> int:
    m = mean(data)
    pos_low = int(m)
    pos_high = int(m + 1)
    return min(
        sum(utils.triangle(abs(i - pos)) for i in data) for pos in (pos_high, pos_low)
    )
