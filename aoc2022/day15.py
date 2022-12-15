import re

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    matcher = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    data = utils.load_data(15, example=EXAMPLE, fn=matcher.fullmatch)

    return [
        ((int(d.group(1)), int(d.group(2))), (int(d.group(3)), int(d.group(4))))
        for d in data
    ]


DATA = load_data()


def part1() -> int:
    grid = {}
    radii = {}
    x_bounds = []
    for (sx, sy), (bx, by) in DATA:
        grid[sx, sy] = "S"
        grid[bx, by] = "B"
        radius = utils.manhattan(sx - bx, sy - by)
        x_bounds.extend([sx + radius, sx - radius])
        radii[sx, sy] = radius

    x_min = min(x_bounds)
    x_max = max(x_bounds)

    y = 10 if EXAMPLE else 2000000

    empty = 0
    for x in range(x_min, x_max + 1):
        # print(f"Looking at {x}, {y}")
        if (x, y) in grid:
            continue
        for (sx, sy), radius in radii.items():
            # print(sx, sy, radius)
            if utils.manhattan(x - sx, y - sy) <= radius:
                empty += 1
                break

    return empty


def part2() -> int:
    if EXAMPLE:
        max_x = max_y = 20
    else:
        max_x = max_y = 4000000

    radii: dict[tuple[int, int], int] = {}
    for (sx, sy), (bx, by) in DATA:
        radius = utils.manhattan(sx - bx, sy - by)
        radii[sx, sy] = radius

    for i, (coord, radius) in enumerate(radii.items()):
        print(f"Sensor {i}")
        for x, y in utils.manhattan_border(coord, radius + 1):
            if x < 0 or y < 0 or x > max_x or y > max_y:
                continue
            for (sx, sy), r in radii.items():
                if utils.manhattan(x - sx, y - sy) <= r:
                    break
            else:
                print(f"{x}, {y} must be empty???")
                return x * 4000000 + y

    return -1


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
