from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    if EXAMPLE:
        return 125

    return 36_000_000


DATA = load_data()


def part1() -> int:
    for i in range(1, 100000):
        presents = 0
        for j in range(1, i + 1):
            if i % j == 0:
                presents += j
        presents *= 10
        if presents >= DATA:
            return i
    return 0


def part2() -> int:
    return 0


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
