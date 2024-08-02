from itertools import count

from aoc import utils


def parse_data(data):
    data = utils.parse_data(data, fn=int)

    return data


def transform(subject: int, loop_size: int) -> int:
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


def find_loop_size(expected: int) -> int:
    value = 1
    for i in count():
        if value == expected:
            return i
        value = (value * 7) % 20201227


def part1(data) -> int:
    loop_size = find_loop_size(data[0])
    return transform(data[1], loop_size)


def part2(data) -> str:
    return "*"
