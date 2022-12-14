import itertools

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(17, example=EXAMPLE, fn=int)

    return data


DATA = load_data()


def part1() -> int:
    count = 0
    for r in range(len(DATA)):
        for comb in itertools.combinations(DATA, r + 1):
            if sum(comb) == (25 if EXAMPLE else 150):
                count += 1
    return count


def part2() -> int:
    count = 0
    for r in range(len(DATA)):
        for comb in itertools.combinations(DATA, r + 1):
            if sum(comb) == (25 if EXAMPLE else 150):
                count += 1
        if count:
            break
    return count


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
