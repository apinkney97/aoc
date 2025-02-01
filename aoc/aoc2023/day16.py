import collections
from enum import Enum
from typing import NamedTuple

from aoc.utils.coords import Coord2D, Vector2D


# [0, 0] is top left
class Direction(Enum):
    up = Vector2D(0, -1)
    right = Vector2D(1, 0)
    down = Vector2D(0, 1)
    left = Vector2D(-1, 0)


VERTICAL = {Direction.up, Direction.down}
HORIZONTAL = {Direction.left, Direction.right}


class Beam(NamedTuple):
    coord: Coord2D
    dir: Direction


def parse_data(data):
    return data


def reflect(grid: list[str], start_coord: Coord2D, start_direction: Direction) -> int:
    seen_beams = set()

    width = len(grid[0])
    height = len(grid)

    visited = set()

    queue: collections.deque[Beam] = collections.deque()

    def enqueue(old_coord: Coord2D, new_direction: Direction) -> None:
        beam = Beam(old_coord + new_direction.value, new_direction)
        if (
            beam in seen_beams
            or beam.coord.x < 0
            or beam.coord.x >= width
            or beam.coord.y < 0
            or beam.coord.y >= height
        ):
            return

        seen_beams.add(beam)
        visited.add(beam.coord)
        queue.append(beam)

    enqueue(start_coord, start_direction)

    while queue:
        coord, direction = queue.popleft()
        cell = grid[coord.y][coord.x]

        match cell, direction:
            case "/", Direction.up:
                enqueue(coord, Direction.right)

            case "/", Direction.right:
                enqueue(coord, Direction.up)

            case "/", Direction.down:
                enqueue(coord, Direction.left)

            case "/", Direction.left:
                enqueue(coord, Direction.down)

            case "\\", Direction.up:
                enqueue(coord, Direction.left)

            case "\\", Direction.right:
                enqueue(coord, Direction.down)

            case "\\", Direction.down:
                enqueue(coord, Direction.right)

            case "\\", Direction.left:
                enqueue(coord, Direction.up)

            case "|", _ if direction in HORIZONTAL:
                enqueue(coord, Direction.up)
                enqueue(coord, Direction.down)

            case "-", _ if direction in VERTICAL:
                enqueue(coord, Direction.left)
                enqueue(coord, Direction.right)

            case _:
                # Continue in the same direction
                enqueue(coord, direction)

    return len(visited)


def part1(data) -> int:
    return reflect(data, Coord2D(-1, 0), Direction.right)


def part2(data) -> int:
    result = 0
    width = len(data[0])
    height = len(data)

    for x in range(width):
        result = max(result, reflect(data, Coord2D(x, -1), Direction.down))
        result = max(result, reflect(data, Coord2D(x, height), Direction.up))

    for y in range(width):
        result = max(result, reflect(data, Coord2D(-1, y), Direction.right))
        result = max(result, reflect(data, Coord2D(width, y), Direction.left))

    return result
