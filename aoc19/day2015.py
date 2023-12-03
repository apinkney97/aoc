import utils

EXAMPLE = True
# EXAMPLE = False


def load_data():
    data = utils.load_data(2015, example=EXAMPLE)

    return data


DATA = load_data()


def part1() -> int:
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
