from typing import List, Mapping, Tuple

from aoc import utils

DIRECTIONS = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}


Point = Tuple[int, int]


def parse_data(data):
    wire1 = data[0].split(",")
    wire2 = data[1].split(",")

    w1_points = get_points(wire1)
    w2_points = get_points(wire2)

    return w1_points, w2_points


def get_points(wire: List[str], start: Point = (0, 0)) -> Mapping[Point, int]:
    points = {}
    x, y = start
    dist = 0

    for move in wire:
        vector = DIRECTIONS[move[0]]
        magnitude = int(move[1:])

        for _ in range(magnitude):
            x += vector[0]
            y += vector[1]
            new_point = (x, y)
            dist += 1
            if new_point not in points:
                points[new_point] = dist

    return points


def manhattan_distance(p1: Point, p2: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def part1(data) -> int:
    origin = (0, 0)

    w1_points, w2_points = data

    intersections = set(w1_points).intersection(set(w2_points))

    min_dist = None
    for intersection in intersections:
        # if intersection == origin:
        #     continue
        dist = manhattan_distance(intersection, origin)
        min_dist = utils.safe_min(min_dist, dist)

    return min_dist


def part2(data) -> int:
    w1_points, w2_points = data

    intersections = set(w1_points).intersection(set(w2_points))

    min_dist = None

    for intersection in intersections:
        dist = w1_points[intersection] + w2_points[intersection]
        min_dist = utils.safe_min(min_dist, dist)

    return min_dist
