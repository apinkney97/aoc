from itertools import combinations

from aoc import utils

TARGET = 2020


def parse_data(data):
    return utils.parse_data(data, fn=int)


def part1(data) -> int:
    for a, b in combinations(data, 2):
        if a + b == TARGET:
            return a * b
    raise Exception("No solution found")


def part2(data) -> int:
    for a, b, c in combinations(data, 3):
        if a + b + c == TARGET:
            return a * b * c
    raise Exception("No solution found")
