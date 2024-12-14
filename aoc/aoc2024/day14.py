import re

from aoc import config
from aoc.utils import BACKGROUND_BLOCK, FOREGROUND_BLOCK
from aoc.utils.coords import Coord, Vector

if config.EXAMPLE:
    BOUNDS = Coord(11, 7)
else:
    BOUNDS = Coord(101, 103)


def parse_data(data):
    parsed = []
    for line in data:
        match = re.fullmatch(r"p=(\d+),(\d+) v=([\d-]+),([\d-]+)", line)
        pos = Coord(int(match[1]), int(match[2]))
        vec = Vector(int(match[3]), int(match[4]))
        parsed.append((pos, vec))
    return parsed


def get_positions(data, steps):
    positions = set()
    for pos, vec in data:
        vec = vec * steps
        pos += vec
        pos %= BOUNDS
        positions.add(pos)

    return positions


def get_safe_score(positions):
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


def part1(data) -> int:
    return get_safe_score(get_positions(data, steps=100))


def print_board(positions):
    for y in range(BOUNDS.y):
        for x in range(BOUNDS.x):
            if Coord(x, y) in positions:
                print(FOREGROUND_BLOCK, end="")
            else:
                print(BACKGROUND_BLOCK, end="")
        print()


def part2(data) -> int:
    for steps in range(10000):
        positions = get_positions(data, steps=steps)
        print(steps)
        print_board(positions)
    return -1
