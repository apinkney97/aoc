from __future__ import annotations

from typing import Set

from cachetools import cached

from aoc.utils import Coord2D, Vector2D


def parse_data(data):
    lines = []
    for line in data:
        directions = []
        lines.append(directions)
        li = iter(line)
        for c in li:
            if c in {"e", "w"}:
                directions.append(c)
            else:
                directions.append(c + next(li))

    return lines


VECTORS = {
    "e": Vector2D(1, 0),
    "w": Vector2D(-1, 0),
    "ne": Vector2D(0, 1),
    "sw": Vector2D(0, -1),
    "nw": Vector2D(-1, 1),
    "se": Vector2D(1, -1),
}

CACHE = {}


@cached(CACHE)
def get_neighbours(coord: Coord2D) -> Set[Coord2D]:
    ns = set()
    for vector in VECTORS.values():
        ns.add(coord + vector)
    return ns


def init_tiles(data) -> Set[Coord2D]:
    tiles: Set[Coord2D] = set()
    start = Coord2D(0, 0)
    for line in data:
        c = start
        for direction in line:
            c += VECTORS[direction]
        if c not in tiles:
            tiles.add(c)
        else:
            tiles.remove(c)

    return tiles


def part1(data) -> int:
    tiles = init_tiles(data)
    return len(tiles)


def step(tiles: Set[Coord2D]) -> Set[Coord2D]:
    next_grid = set()

    to_check = set(tiles)
    for coord in tiles:
        to_check.update(get_neighbours(coord))

    for coord in to_check:
        neighbour_count = len(tiles & get_neighbours(coord))

        if coord in tiles:
            if neighbour_count in {1, 2}:
                next_grid.add(coord)
        elif neighbour_count == 2:
            next_grid.add(coord)

    return next_grid


def part2(data) -> int:
    tiles = init_tiles(data)

    for i in range(100):
        tiles = step(tiles)

    return len(tiles)
