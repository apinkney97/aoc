from aoc.utils import Coord2D, Vector2D

type Data = list[tuple[str, int]]

CARDINAL_DIRECTIONS = [Vector2D(0, 1), Vector2D(1, 0), Vector2D(0, -1), Vector2D(-1, 0)]


def parse_data(data: list[str]) -> Data:
    parsed: list[tuple[str, int]] = []
    for step in data[0].split(", "):
        parsed.append((step[0], int(step[1:])))
    return parsed


def part1(data: Data, stop_at_dupe: bool = False) -> int:
    start = Coord2D(0, 0)
    direction = 0
    turns = {"L": -1, "R": 1}
    pos = start
    been = {start}
    for turn, steps in data:
        direction = (direction + turns[turn]) % 4
        for _ in range(steps):
            pos += CARDINAL_DIRECTIONS[direction]
            if stop_at_dupe:
                if pos in been:
                    return (pos - start).manhattan
                been.add(pos)

    return (pos - start).manhattan


def part2(data: Data) -> int:
    return part1(data, stop_at_dupe=True)
