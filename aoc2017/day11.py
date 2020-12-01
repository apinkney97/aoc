"""
Cheers to
http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
for providing some insight into hex grids!
"""
from aoc2017.util import load_data

DIRS = {
    "n": (0, 1),
    "s": (0, -1),
    "ne": (1, 0),
    "se": (1, -1),
    "nw": (-1, 1),
    "sw": (-1, 0),
}

GLOBAL_MAX = 0


def hex_dist(x1, y1, x2=0, y2=0):
    z1 = -x1 - y1
    z2 = -x2 - y2

    return max(abs(x2 - x1), abs(y2 - y1), abs(z2 - z1))


def part1():
    global GLOBAL_MAX
    x = 0
    y = 0
    for d in load_data(11)[0].split(","):
        dx, dy = DIRS[d]
        x += dx
        y += dy
        dist = hex_dist(x, y)
        if dist > GLOBAL_MAX:
            GLOBAL_MAX = dist

    return hex_dist(x, y)


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(GLOBAL_MAX))
