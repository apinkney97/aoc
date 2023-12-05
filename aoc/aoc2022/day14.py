import itertools
import typing

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


class Coord(typing.NamedTuple):
    x: int
    y: int


def load_data():
    data = utils.load_data(2022, 14, example=EXAMPLE)
    grid = {}

    for line in data:
        parsed_line = []
        parts = line.split(" -> ")
        for part in parts:
            x, y = part.split(",")
            parsed_line.append(Coord(int(x), int(y)))

        for c1, c2 in itertools.pairwise(parsed_line):
            if c1.x == c2.x:
                for y in range(*sorted([c1.y, c2.y])):
                    grid[Coord(c1.x, y)] = "#"
            elif c1.y == c2.y:
                for x in range(*sorted([c1.x, c2.x])):
                    grid[Coord(x, c1.y)] = "#"

            grid[c1] = "#"
            grid[c2] = "#"

    return grid


def drop(grid, limit):
    curr = Coord(500, 0)

    while True:
        if curr.y > limit:
            return False

        down = Coord(curr.x, curr.y + 1)
        dl = Coord(curr.x - 1, curr.y + 1)
        dr = Coord(curr.x + 1, curr.y + 1)

        if down not in grid:
            curr = down
        elif dl not in grid:
            curr = dl
        elif dr not in grid:
            curr = dr
        else:
            grid[curr] = "o"
            return True


def drop2(grid, limit):
    curr = Coord(500, 0)

    while True:
        down = Coord(curr.x, curr.y + 1)
        dl = Coord(curr.x - 1, curr.y + 1)
        dr = Coord(curr.x + 1, curr.y + 1)

        above_ground = curr.y < limit + 1

        if above_ground and down not in grid:
            curr = down
        elif above_ground and dl not in grid:
            curr = dl
        elif above_ground and dr not in grid:
            curr = dr
        else:
            grid[curr] = "o"
            if curr.y == 0:
                return False
            return True


def part1() -> int:
    grid = load_data()

    max_y = max(c.y for c in grid)

    count = 0
    while True:
        ok = drop(grid, max_y)
        if not ok:
            break
        count += 1

    return count


def part2() -> int:
    grid = load_data()

    max_y = max(c.y for c in grid)

    count = 0
    while True:
        ok = drop2(grid, max_y)
        count += 1
        if not ok:
            break

    return count


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
