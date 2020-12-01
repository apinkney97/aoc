from itertools import combinations

import utils

TARGET = 2020
DATA = utils.load_data(1, fn=int)


def part1() -> int:
    for (a, b) in combinations(DATA, 2):
        if a + b == TARGET:
            return a * b
    raise Exception("No solution found")


def part2() -> int:
    for (a, b, c) in combinations(DATA, 3):
        if a + b + c == TARGET:
            return a * b * c
    raise Exception("No solution found")


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
