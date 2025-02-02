import itertools

from aoc import config, utils

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return utils.parse_data(data, fn=int)


def part1(data: Data) -> int:
    count = 0
    for r in range(len(data)):
        for comb in itertools.combinations(data, r + 1):
            if sum(comb) == (25 if config.EXAMPLE else 150):
                count += 1
    return count


def part2(data: Data) -> int:
    count = 0
    for r in range(len(data)):
        for comb in itertools.combinations(data, r + 1):
            if sum(comb) == (25 if config.EXAMPLE else 150):
                count += 1
        if count:
            break
    return count
