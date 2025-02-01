import collections

from aoc import utils
from aoc.utils import Coord2D


def get_neighbours(nodes, coord, reverse=False):
    height = ord(nodes[coord])
    for neighbour in utils.neighbours(coord, include_diagonals=False):
        if neighbour not in nodes:
            continue
        neighbour_height = ord(nodes[neighbour])

        if reverse:
            # exactly one lower, or many higher
            if neighbour_height >= height - 1:
                yield neighbour
        else:
            # exactly one lower, or many lower
            if neighbour_height <= height + 1:
                yield neighbour


def part1(data, reverse=False) -> int:
    nodes: dict[utils.Coord2D, int] = {}

    start = None
    end = None

    for y, row in enumerate(data):
        for x, height in enumerate(row):
            coord = Coord2D(x, y)
            if height == "S":
                height = "a"
                start = coord
            elif height == "E":
                height = "z"
                end = coord

            nodes[coord] = height

    if reverse:
        start = end

    visited = set()

    parents = {start: None}

    queue = collections.deque([start])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        if (not reverse and current == end) or (reverse and nodes[current] == "a"):
            end = current
            break
        for neighbour in get_neighbours(nodes, current, reverse=reverse):
            if neighbour in visited:
                continue
            queue.append(neighbour)
            parents[neighbour] = current

    path = []
    current = end

    while current is not None:
        current = parents[current]
        path.append(current)

    return len(path) - 1


def part2(data) -> int:
    return part1(data, reverse=True)
