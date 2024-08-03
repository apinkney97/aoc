import re

from aoc import utils


def parse_data(data):
    RE = re.compile(r"^(\d+)x(\d+)x(\d+)$")
    data = utils.parse_data(data, fn=RE.match)
    dimensions = [sorted(int(item[i]) for i in (1, 2, 3)) for item in data]
    return dimensions


def part1(data) -> int:
    total = 0
    for ds in data:
        total += 3 * ds[0] * ds[1]
        total += 2 * ds[0] * ds[2]
        total += 2 * ds[1] * ds[2]

    return total


def part2(data) -> int:
    total = 0
    for ds in data:
        total += 2 * (ds[0] + ds[1])
        total += utils.product(ds)

    return total
