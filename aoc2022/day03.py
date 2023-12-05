import string

import more_itertools

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2022, 3, example=EXAMPLE)
    return data


DATA = load_data()

SCORES = {
    letter: score
    for score, letter in enumerate(
        string.ascii_lowercase + string.ascii_uppercase, start=1
    )
}


def part1() -> int:
    total = 0
    for line in DATA:
        half = len(line) // 2
        common = (set(line[:half]) & set(line[half:])).pop()
        total += SCORES[common]
    return total


def part2() -> int:
    total = 0
    for elves in more_itertools.chunked(DATA, 3):
        common = (set(elves[0]) & set(elves[1]) & set(elves[2])).pop()
        total += SCORES[common]
    return total


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
