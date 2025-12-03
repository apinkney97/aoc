import re

from aoc import utils

type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    RE = re.compile(r"^(\d+)x(\d+)x(\d+)$")
    matches = [RE.match(line) for line in data]
    dimensions = [
        sorted(int(item[i]) for i in (1, 2, 3)) for item in matches if item is not None
    ]
    return dimensions


def part1(data: Data) -> int:
    total = 0
    for ds in data:
        total += 3 * ds[0] * ds[1]
        total += 2 * ds[0] * ds[2]
        total += 2 * ds[1] * ds[2]

    return total


def part2(data: Data) -> int:
    total = 0
    for ds in data:
        total += 2 * (ds[0] + ds[1])
        total += utils.product(ds)

    return total
