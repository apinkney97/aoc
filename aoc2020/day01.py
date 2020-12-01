from itertools import combinations

import utils

TARGET = 2020


def part1() -> int:
    data = [int(line) for line in utils.load_data(1)]
    for (a, b) in combinations(data, 2):
        if a + b == TARGET:
            return a * b
    raise Exception("No solution found")


def part2() -> int:
    data = [int(line) for line in utils.load_data(1)]
    for (a, b, c) in combinations(data, 3):
        if a + b + c == TARGET:
            return a * b * c
    raise Exception("No solution found")


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
