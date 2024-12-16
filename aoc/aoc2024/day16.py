from enum import Enum
from typing import NamedTuple

from aoc.utils import BACKGROUND_BLOCK, FOREGROUND_BLOCK, PQ, Grid2D
from aoc.utils.coords import Coord, Vector


class Direction(Enum):
    NORTH = Vector(0, -1)
    EAST = Vector(1, 0)
    SOUTH = Vector(0, 1)
    WEST = Vector(-1, 0)


TURNS = {
    Direction.NORTH: [Direction.EAST, Direction.WEST],
    Direction.EAST: [Direction.NORTH, Direction.SOUTH],
    Direction.SOUTH: [Direction.EAST, Direction.WEST],
    Direction.WEST: [Direction.NORTH, Direction.SOUTH],
}

EMPTY = 0
WALL = 1

PART_2 = -1


class Node(NamedTuple):
    coord: Coord
    direction: Direction


def parse_data(data):
    start = end = None
    maze = Grid2D(
        display_map={
            EMPTY: "  ",
            WALL: BACKGROUND_BLOCK,
            2: FOREGROUND_BLOCK,
        }
    )
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            coord = Coord(x, y)
            if char == "#":
                maze[coord] = WALL
            elif char == "S":
                start = coord
            elif char == "E":
                end = coord

    return maze, start, end


def part1(data) -> int:
    maze, start_coord, end_coord = data
    step_cost = 1
    turn_cost = 1000

    start_node = Node(start_coord, Direction.EAST)
    queue: PQ[Node] = PQ()

    queue.add_item(start_node, priority=0)

    costs: dict[Node, int] = {start_node: 0}
    parents: dict[Node, list[Node]] = {start_node: []}

    end_node = None

    while queue:
        curr = queue.pop_item()
        cost = costs[curr]

        if curr.coord == end_coord:
            end_node = curr
            continue

        # Make moves

        new_nodes = []
        # Turn 90 degrees
        for new_dir in TURNS[curr.direction]:
            new_node = Node(curr.coord, new_dir)
            new_cost = cost + turn_cost
            new_nodes.append((new_node, new_cost))

        # Step in current direction
        new_coord = curr.coord + curr.direction.value
        if maze[new_coord] == EMPTY:
            new_node = Node(new_coord, curr.direction)
            new_cost = costs[curr] + step_cost
            new_nodes.append((new_node, new_cost))

        for new_node, new_cost in new_nodes:
            if new_node not in costs or new_cost <= costs[new_node]:
                if new_node not in costs or new_cost < costs[new_node]:
                    parents[new_node] = [curr]
                elif new_node in costs and new_cost == costs[new_node]:
                    parents[new_node].append(curr)

                costs[new_node] = new_cost
                queue.add_item(new_node, priority=new_cost)

    visited = set()
    to_visit: list[Node] = [end_node]

    while to_visit:
        curr = to_visit.pop()
        visited.add(curr.coord)
        to_visit.extend(parents[curr])

    # for coord in visited:
    #     maze[coord] = 2
    # print(maze)

    global PART_2
    PART_2 = len(visited)

    return costs[end_node]


def part2(data) -> int:
    return PART_2
