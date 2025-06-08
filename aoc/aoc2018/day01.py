from itertools import cycle

from aoc import utils

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return utils.parse_data(data, fn=int)


def part1(data: Data) -> int:
    return sum(data)


def part2(data: Data) -> int:
    curr = 0
    seen = {0}

    for val in cycle(data):
        curr += val
        if curr in seen:
            return curr
        seen.add(curr)

    raise Exception("No solution found")
