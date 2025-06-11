import itertools
from collections.abc import Collection, Generator

from aoc.utils import product

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data]


def get_groups(
    packages: Collection[int], size: int, target: int
) -> Generator[tuple[int, ...]]:
    for subset in itertools.combinations(packages, size):
        if sum(subset) == target:
            yield subset


def can_bisect(packages: Collection[int]) -> bool:
    target = sum(packages) // 2
    for i in range(len(packages)):
        for subset in itertools.combinations(packages, i + 1):
            if sum(subset) == target:
                return True
    return False


def can_trisect(packages: Collection[int]) -> bool:
    target = sum(packages) // 3
    for i in range(len(packages)):
        for subset in itertools.combinations(packages, i + 1):
            if sum(subset) == target and can_bisect(set(packages) - set(subset)):
                return True
    return False


def part1(data: Data) -> int:
    target = sum(data) // 3
    data_set = set(data)
    solutions: list[tuple[int, ...]] = []

    for i in range(len(data)):
        if solutions:
            break

        for group in get_groups(data, i + 1, target):
            remainder = data_set - set(group)
            if can_bisect(remainder):
                solutions.append(group)

    return min(product(s) for s in solutions)


def part2(data: Data) -> int:
    target = sum(data) // 4
    data_set = set(data)
    solutions: list[tuple[int, ...]] = []

    for i in range(len(data)):
        if solutions:
            break

        for group in get_groups(data, i + 1, target):
            remainder = data_set - set(group)
            if can_trisect(remainder):
                solutions.append(group)

    return min(product(s) for s in solutions)
