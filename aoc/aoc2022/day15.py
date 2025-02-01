import re

from aoc import config, utils
from aoc.utils import Coord2D


def parse_data(data):
    matcher = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    data = utils.parse_data(data, fn=matcher.fullmatch)

    return [
        (
            utils.Coord2D(int(d.group(1)), int(d.group(2))),
            utils.Coord2D(int(d.group(3)), int(d.group(4))),
        )
        for d in data
    ]


SENSOR = 1
BEACON = 2


def part1(data: list[tuple[Coord2D, Coord2D]]) -> int:
    grid = utils.Grid2D()
    radii = {}
    x_bounds = []
    for sensor_coord, beacon_coord in data:
        grid[sensor_coord] = SENSOR
        grid[beacon_coord] = BEACON
        radius = (sensor_coord - beacon_coord).manhattan
        x_bounds.extend([sensor_coord.x + radius, sensor_coord.x - radius])
        radii[sensor_coord] = radius

    x_min = min(x_bounds)
    x_max = max(x_bounds)

    y = 10 if config.EXAMPLE else 2000000

    empty = 0
    for x in range(x_min, x_max + 1):
        # print(f"Looking at {x}, {y}")
        coord = Coord2D(x, y)
        if grid[coord]:
            continue
        for sensor_coord, radius in radii.items():
            # print(sx, sy, radius)
            if (sensor_coord - coord).manhattan <= radius:
                empty += 1
                break

    return empty


def part2(data: list[tuple[Coord2D, Coord2D]]) -> int:
    if config.EXAMPLE:
        max_x = max_y = 20
    else:
        max_x = max_y = 4000000

    radii: dict[Coord2D, int] = {}
    for sensor_coord, beacon_coord in data:
        radius = (sensor_coord - beacon_coord).manhattan
        radii[sensor_coord] = radius

    for i, (coord, radius) in enumerate(radii.items()):
        print(f"Sensor {i}")
        for rc in utils.manhattan_border(coord, radius + 1):
            if not rc.in_bounds(Coord2D(0, 0), Coord2D(max_x, max_y)):
                continue
            for sensor_coord, r in radii.items():
                if (sensor_coord - rc).manhattan <= r:
                    break
            else:
                print(f"{rc.x}, {rc.y} must be empty???")
                return rc.x * 4000000 + rc.y

    return -1
