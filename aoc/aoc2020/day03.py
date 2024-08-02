from aoc import utils


def check_slope(data: list[str], dx: int, dy: int) -> int:
    trees = 0
    x = 0
    y = 0

    while y < len(data):
        row = data[y]
        char = row[x % len(row)]
        if char == "#":
            trees += 1
        x += dx
        y += dy

    return trees


def part1(data) -> int:
    return check_slope(data, 3, 1)


def part2(data) -> int:
    tests = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return utils.product(check_slope(data, dx, dy) for (dx, dy) in tests)
