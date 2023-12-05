from statistics import mean, median_high, median_low

from aoc import utils


def load_data():
    data = utils.load_data(2021, 7, example=False)

    return [int(i) for i in data[0].split(",")]


DATA = load_data()


def part1() -> int:
    return min(
        sum(abs(i - pos) for i in DATA) for pos in (median_low(DATA), median_high(DATA))
    )


def part2() -> int:
    m = mean(DATA)
    pos_low = int(m)
    pos_high = int(m + 1)
    return min(
        sum(utils.triangle(abs(i - pos)) for i in DATA) for pos in (pos_high, pos_low)
    )


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
