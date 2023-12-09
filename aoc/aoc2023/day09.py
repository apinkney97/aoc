import itertools

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(
        2023,
        9,
        example=EXAMPLE,
        fn=lambda line: [int(i) for i in line.split()],
    )

    return data


with utils.timed("Load data"):
    DATA = load_data()


def reduce(line: list[int]) -> list[int]:
    return [b - a for a, b in itertools.pairwise(line)]


def extrapolate(line: list[int]) -> int:
    next_lines = [line]

    while len(set(line)) > 1:
        line = reduce(line)
        next_lines.append(line)

    return sum(line[-1] for line in next_lines)


def part1() -> int:
    return sum(extrapolate(line) for line in DATA)


def part2() -> int:
    return sum(extrapolate(line[::-1]) for line in DATA)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
