"""
Cheers to
http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
for providing some insight into hex grids!
"""

type Data = list[str]


def parse_data(data: list[str]) -> Data:
    return data[0].split(",")


DIRS = {
    "n": (0, 1),
    "s": (0, -1),
    "ne": (1, 0),
    "se": (1, -1),
    "nw": (-1, 1),
    "sw": (-1, 0),
}

GLOBAL_MAX = 0


def hex_dist(x1: int, y1: int, x2: int = 0, y2: int = 0) -> int:
    z1 = -x1 - y1
    z2 = -x2 - y2

    return max(abs(x2 - x1), abs(y2 - y1), abs(z2 - z1))


def part1(data: Data) -> int:
    global GLOBAL_MAX
    x = 0
    y = 0
    for d in data:
        dx, dy = DIRS[d]
        x += dx
        y += dy
        dist = hex_dist(x, y)
        if dist > GLOBAL_MAX:
            GLOBAL_MAX = dist

    return hex_dist(x, y)


def part2(data: Data) -> int:
    return GLOBAL_MAX
