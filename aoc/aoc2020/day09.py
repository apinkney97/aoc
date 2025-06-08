from collections import deque
from itertools import combinations

from aoc import utils

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return utils.parse_data(data, fn=int)


def part1(data: Data) -> int:
    preamble = 25
    window = deque(data[:preamble])
    for val in data[preamble:]:
        for a, b in combinations(window, 2):
            if val == a + b:
                break
        else:
            return val
        window.popleft()
        window.append(val)

    raise Exception("No value found")


def part2(data: Data) -> int:
    target = part1(data)

    window: deque[int] = deque()
    data_it = iter(data)

    while True:
        value = sum(window)
        if value > target:
            window.popleft()
        elif value < target:
            window.append(next(data_it))
        else:
            return max(window) + min(window)
