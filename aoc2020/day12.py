import utils

DATA = utils.load_data(2020, 12, fn=lambda x: (x[0], int(x[1:])))


# North is +Y
# East is +X
COMPASS_POINTS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}


def part1() -> int:
    angle = 0
    x, y = 0, 0

    directions = [
        (1, 0),  # east
        (0, -1),  # south
        (-1, 0),  # west
        (0, 1),  # north
    ]

    for c, n in DATA:
        if c in COMPASS_POINTS:
            dx, dy = COMPASS_POINTS[c]
            x += n * dx
            y += n * dy
        elif c == "R":
            angle += n
        elif c == "L":
            angle -= n
        elif c == "F":
            dx, dy = directions[(angle % 360) // 90]
            x += dx * n
            y += dy * n

    return abs(x) + abs(y)


def part2() -> int:
    dx = 10
    dy = 1

    x, y = 0, 0

    for c, n in DATA:
        if c in COMPASS_POINTS:
            ddx, ddy = COMPASS_POINTS[c]
            dx += ddx * n
            dy += ddy * n

        elif c in {"L", "R"}:
            angle = n if c == "R" else -n
            angle %= 360
            angle //= 90
            for _ in range(angle):
                dx, dy = dy, -dx

        elif c == "F":
            x += dx * n
            y += dy * n

    return abs(x) + abs(y)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
