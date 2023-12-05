from typing import NamedTuple, Set

from cachetools import cached

from aoc import utils


class Coord(NamedTuple):
    x: int
    y: int
    z: int
    w: int


def load_data():
    grid = set()
    data = utils.load_data(2020, 17, example=False)
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid.add(Coord(x, y, 0, 0))
    return grid


DATA = load_data()


CACHE = {}


@cached(CACHE)
def get_neighbours(coord: Coord, dimensions) -> Set[Coord]:
    neighbours = set()
    for x in range(coord.x - 1, coord.x + 2):
        for y in range(coord.y - 1, coord.y + 2):
            for z in range(coord.z - 1, coord.z + 2):
                if dimensions == 3:
                    new_coord = Coord(x, y, z, 0)
                    if new_coord != coord:
                        neighbours.add(new_coord)
                elif dimensions == 4:
                    for w in range(coord.w - 1, coord.w + 2):
                        new_coord = Coord(x, y, z, w)
                        if new_coord != coord:
                            neighbours.add(new_coord)

    return neighbours


def step(grid: Set[Coord], dimensions) -> Set[Coord]:
    next_grid = set()

    to_check = set(grid)
    for coord in grid:
        to_check.update(get_neighbours(coord, dimensions))

    for coord in to_check:
        neighbour_count = len(grid & get_neighbours(coord, dimensions=dimensions))

        if coord in grid:
            if neighbour_count in {2, 3}:
                next_grid.add(coord)
        elif neighbour_count == 3:
            next_grid.add(coord)

    return next_grid


def part1() -> int:
    grid = DATA

    for _ in range(6):
        grid = step(grid, dimensions=3)

    return len(grid)


def part2() -> int:
    grid = DATA

    for _ in range(6):
        grid = step(grid, dimensions=4)

    return len(grid)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
