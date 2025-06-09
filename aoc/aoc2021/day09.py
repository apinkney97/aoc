from typing import Generator

from aoc import utils

type Data = list[list[int]]


def _parse_data(data: list[str]) -> Data:
    return [[int(c) for c in line] for line in data]


def neighbours(x: int, y: int, w: int, h: int) -> Generator[tuple[int, int]]:
    if x != 0:
        yield x - 1, y
    if x != w - 1:
        yield x + 1, y
    if y != 0:
        yield x, y - 1
    if y != h - 1:
        yield x, y + 1


def get_low_points(data: Data) -> Generator[tuple[int, int]]:
    w = len(data)
    h = len(data[0])

    for x, heights in enumerate(data):
        for y, height in enumerate(heights):
            for n_x, n_y in neighbours(x, y, w, h):
                if height >= data[n_x][n_y]:
                    break
            else:
                yield x, y


def part1(data: list[str]) -> int:
    parsed = _parse_data(data)
    score = 0
    for x, y in get_low_points(parsed):
        score += 1 + parsed[x][y]

    return score


def part2(data: list[str]) -> int:
    basins = []
    w = len(data)
    h = len(data[0])

    data_copy = _parse_data(data)
    parsed = _parse_data(data)

    for x, y in get_low_points(parsed):
        stack = [(x, y)]
        size = 0
        seen = set()
        while stack:
            xx, yy = stack.pop()
            if data_copy[xx][yy] != 9:
                size += 1
                data_copy[xx][yy] = 9
                for neighbour in neighbours(xx, yy, w, h):
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
        basins.append(size)

    return utils.product(sorted(basins)[-3:])
