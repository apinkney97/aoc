import re

from aoc import config
from aoc.utils import BACKGROUND_BLOCK, FOREGROUND_BLOCK
from aoc.utils.coords import Coord2D, Vector2D

if config.EXAMPLE:
    BOUNDS = Coord2D(11, 7)
else:
    BOUNDS = Coord2D(101, 103)

type Data = list[tuple[Coord2D, Vector2D]]


def parse_data(data: list[str]) -> Data:
    parsed = []
    for line in data:
        match = re.fullmatch(r"p=(\d+),(\d+) v=([\d-]+),([\d-]+)", line)
        assert match is not None
        pos = Coord2D(int(match[1]), int(match[2]))
        vec = Vector2D(int(match[3]), int(match[4]))
        parsed.append((pos, vec))
    return parsed


def get_positions(data: Data, steps: int) -> set[Coord2D]:
    positions = set()
    for pos, vec in data:
        vec = vec * steps
        pos += vec
        pos %= BOUNDS
        positions.add(pos)

    return positions


def get_safe_score(positions: set[Coord2D]) -> int:
    tl = 0
    tr = 0
    bl = 0
    br = 0

    mid_x = BOUNDS.x // 2
    mid_y = BOUNDS.y // 2

    for pos in positions:
        if pos.x < mid_x:
            if pos.y < mid_y:
                tl += 1
            elif pos.y > mid_y:
                tr += 1
        elif pos.x > mid_x:
            if pos.y < mid_y:
                bl += 1
            elif pos.y > mid_y:
                br += 1

    return tl * tr * bl * br


def part1(data: Data) -> int:
    return get_safe_score(get_positions(data, steps=100))


def print_board(positions: set[Coord2D]) -> None:
    for y in range(BOUNDS.y):
        for x in range(BOUNDS.x):
            if Coord2D(x, y) in positions:
                print(FOREGROUND_BLOCK, end="")
            else:
                print(BACKGROUND_BLOCK, end="")
        print()


def part2(data: Data) -> int:
    for steps in range(10000):
        positions = get_positions(data, steps=steps)
        if len(positions) == len(data):
            print_board(positions)
            return steps
    return -1
