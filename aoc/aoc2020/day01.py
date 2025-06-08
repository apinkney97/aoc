from itertools import combinations

TARGET = 2020

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(line) for line in data]


def part1(data: Data) -> int:
    for a, b in combinations(data, 2):
        if a + b == TARGET:
            return a * b
    raise Exception("No solution found")


def part2(data: Data) -> int:
    for a, b, c in combinations(data, 3):
        if a + b + c == TARGET:
            return a * b * c
    raise Exception("No solution found")
