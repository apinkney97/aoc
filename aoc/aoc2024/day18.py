from aoc.config import EXAMPLE
from aoc.utils import PQ, Coord2D, Grid2D

WALL = 1

SIZE = 7 if EXAMPLE else 71


def parse_data(data):
    return [Coord2D(*tuple(map(int, line.split(",")))) for line in data]


def solve(grid: Grid2D) -> int:
    # print(grid)

    start = Coord2D(0, 0)
    end = Coord2D(6, 6) if EXAMPLE else Coord2D(70, 70)

    queue = PQ[Coord2D]()
    queue.add_item(start, priority=0)

    distances = {start: 0}

    while queue:
        curr = queue.pop_item()
        if curr == end:
            return distances[end]

        for neighbour in curr.neighbours():
            if grid[neighbour] == WALL:
                continue
            if neighbour not in distances:
                new_dist = distances[curr] + 1
                queue.add_item(neighbour, priority=new_dist)
                distances[neighbour] = distances[curr] + 1

    return -1


def part1(data) -> int:
    limit = 12 if EXAMPLE else 1024

    grid = Grid2D()
    for coord in data[:limit]:
        grid[coord] = WALL

    for c in range(SIZE):
        # Add walls
        grid[Coord2D(-1, c)] = WALL
        grid[Coord2D(SIZE, c)] = WALL
        grid[Coord2D(c, -1)] = WALL
        grid[Coord2D(c, SIZE)] = WALL

    return solve(grid)


def part2(data) -> str:
    grid = Grid2D()
    for coord in data:
        grid[coord] = WALL

    for c in range(SIZE):
        # Add walls
        grid[Coord2D(-1, c)] = WALL
        grid[Coord2D(SIZE, c)] = WALL
        grid[Coord2D(c, -1)] = WALL
        grid[Coord2D(c, SIZE)] = WALL

    for i in range(len(data) - 1, 0, -1):
        if solve(grid) != -1:
            return ",".join(str(c) for c in data[i + 1])
        grid[data[i]] = 0

    return "???"
