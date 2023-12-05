from typing import List

import utils

DATA = utils.load_data(2020, 3)


def check_slope(data: List[str], dx: int, dy: int) -> int:
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


def part1() -> int:
    return check_slope(DATA, 3, 1)


def part2() -> int:
    tests = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return utils.product(check_slope(DATA, dx, dy) for (dx, dy) in tests)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
