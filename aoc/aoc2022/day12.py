import collections
from typing import Generator

from aoc import utils
from aoc.utils import Coord2D

type Data = list[str]

type Nodes = dict[utils.Coord2D, str]


def get_neighbours(
    nodes: Nodes, coord: Coord2D, reverse: bool = False
) -> Generator[Coord2D, None, None]:
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


def part1(data: Data, reverse: bool = False) -> int:
    nodes: Nodes = {}

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

    assert start is not None

    visited = set()

    parents: dict[Coord2D, Coord2D | None] = {start: None}

    queue: collections.deque[Coord2D] = collections.deque([start])
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
    curr = end

    while curr is not None:
        curr = parents[curr]
        path.append(curr)

    return len(path) - 1


def part2(data: Data) -> int:
    return part1(data, reverse=True)
