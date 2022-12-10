import more_itertools

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(6, example=EXAMPLE)

    return data[0]


DATA = load_data()


def part1(window=4) -> int:
    for i, group in enumerate(more_itertools.windowed(DATA, window), start=window):
        if len(set(group)) == window:
            return i
    return -1


def part2() -> int:
    return part1(14)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
