import itertools

from aoc import config, utils


def parse_data(data):
    data = utils.parse_data(data, fn=int)

    return data


def part1(data) -> int:
    count = 0
    for r in range(len(data)):
        for comb in itertools.combinations(data, r + 1):
            if sum(comb) == (25 if config.EXAMPLE else 150):
                count += 1
    return count


def part2(data) -> int:
    count = 0
    for r in range(len(data)):
        for comb in itertools.combinations(data, r + 1):
            if sum(comb) == (25 if config.EXAMPLE else 150):
                count += 1
        if count:
            break
    return count
