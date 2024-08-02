from itertools import cycle

from aoc import utils


def parse_data(data):
    return utils.parse_data(data, fn=int)


def part1(data):
    return sum(data)


def part2(data):
    curr = 0
    seen = {0}

    for val in cycle(data):
        curr += val
        if curr in seen:
            return curr
        seen.add(curr)
