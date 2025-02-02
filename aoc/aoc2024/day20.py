import collections

from aoc.utils import Coord2D, Grid2D, manhattan_limit

PATH = 1

type Data = tuple[Grid2D, Coord2D, Coord2D]


def parse_data(data: list[str]) -> Data:
    grid = Grid2D()
    start = end = None
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != "#":
                grid[Coord2D(x, y)] = PATH
            if char == "S":
                start = Coord2D(x, y)
            elif char == "E":
                end = Coord2D(x, y)
    assert start is not None and end is not None
    return grid, start, end


def part1(data: Data, cheat_len: int = 2) -> int:
    grid, start, end = data

    distances = {end: 0}
    dist = 0
    curr = end
    while curr != start:
        dist += 1
        for neighbour in curr.neighbours():
            if grid[neighbour] == PATH and neighbour not in distances:
                distances[neighbour] = dist
                curr = neighbour

    cheats: collections.Counter[int] = collections.Counter()

    for cheat_start in distances:
        for cheat_end in manhattan_limit(cheat_start, cheat_len):
            if grid[cheat_end] == PATH:
                cheat_time = (cheat_start - cheat_end).manhattan
                saved = distances[cheat_start] - distances[cheat_end] - cheat_time
                if saved > 0:
                    cheats[saved] += 1

    result = 0
    for saved, count in cheats.items():
        if saved >= 100:
            result += count
    return result


def part2(data: Data) -> int:
    return part1(data, cheat_len=20)
