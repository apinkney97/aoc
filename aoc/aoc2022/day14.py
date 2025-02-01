import itertools

from aoc.utils import Coord2D


def build_grid(data):
    grid = {}

    for line in data:
        parsed_line = []
        parts = line.split(" -> ")
        for part in parts:
            x, y = part.split(",")
            parsed_line.append(Coord2D(int(x), int(y)))

        for c1, c2 in itertools.pairwise(parsed_line):
            if c1.x == c2.x:
                for y in range(*sorted([c1.y, c2.y])):
                    grid[Coord2D(c1.x, y)] = "#"
            elif c1.y == c2.y:
                for x in range(*sorted([c1.x, c2.x])):
                    grid[Coord2D(x, c1.y)] = "#"

            grid[c1] = "#"
            grid[c2] = "#"

    return grid


def drop(grid, limit):
    curr = Coord2D(500, 0)

    while True:
        if curr.y > limit:
            return False

        down = Coord2D(curr.x, curr.y + 1)
        dl = Coord2D(curr.x - 1, curr.y + 1)
        dr = Coord2D(curr.x + 1, curr.y + 1)

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
    curr = Coord2D(500, 0)

    while True:
        down = Coord2D(curr.x, curr.y + 1)
        dl = Coord2D(curr.x - 1, curr.y + 1)
        dr = Coord2D(curr.x + 1, curr.y + 1)

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


def part1(data) -> int:
    grid = build_grid(data)

    max_y = max(c.y for c in grid)

    count = 0
    while True:
        ok = drop(grid, max_y)
        if not ok:
            break
        count += 1

    return count


def part2(data) -> int:
    grid = build_grid(data)

    max_y = max(c.y for c in grid)

    count = 0
    while True:
        ok = drop2(grid, max_y)
        count += 1
        if not ok:
            break

    return count
