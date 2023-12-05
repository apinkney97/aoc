from aoc import utils

EXAMPLE = True
# EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 5, example=EXAMPLE)

    return data


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    result = 0

    return result


def part2() -> int:
    result = 0

    return result


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
