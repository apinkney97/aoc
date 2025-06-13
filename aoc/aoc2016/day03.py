from collections.abc import Collection

import more_itertools

type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    return [[int(i) for i in line.split()] for line in data]


def part1(data: Data) -> int:
    result = 0
    for sides in data:
        if is_valid(sides):
            result += 1
    return result


def is_valid(sides: Collection[int]) -> bool:
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]


def part2(data: Data) -> int:
    result = 0
    for rows in more_itertools.chunked(data, 3):
        for sides in zip(*rows):
            if is_valid(sides):
                result += 1

    return result
