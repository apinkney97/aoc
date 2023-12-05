from __future__ import annotations

from typing import NamedTuple, Set

from cachetools import cached

from aoc import utils


def load_data():
    data = utils.load_data(2020, 24, example=False)
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


DATA = load_data()


class Coord(NamedTuple):
    x: int
    y: int

    def __add__(self, other: Coord):
        return Coord(self.x + other.x, self.y + other.y)


VECTORS = {
    "e": Coord(1, 0),
    "w": Coord(-1, 0),
    "ne": Coord(0, 1),
    "sw": Coord(0, -1),
    "nw": Coord(-1, 1),
    "se": Coord(1, -1),
}

CACHE = {}


@cached(CACHE)
def get_neighbours(coord: Coord) -> Set[Coord]:
    ns = set()
    for vector in VECTORS.values():
        ns.add(coord + vector)
    return ns


def init_tiles() -> Set[Coord]:
    tiles: Set[Coord] = set()
    start = Coord(0, 0)
    for line in DATA:
        c = start
        for direction in line:
            c += VECTORS[direction]
        if c not in tiles:
            tiles.add(c)
        else:
            tiles.remove(c)

    return tiles


def part1() -> int:
    tiles = init_tiles()
    return len(tiles)


def step(tiles: Set[Coord]) -> Set[Coord]:
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


def part2() -> int:
    tiles = init_tiles()

    for i in range(100):
        tiles = step(tiles)

    return len(tiles)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
