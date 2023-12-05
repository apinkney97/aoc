from collections import Counter

from aoc import utils


def load_data():
    def parse(line):
        parts = line.split(" -> ")
        x1, y1 = parts[0].split(",")
        x2, y2 = parts[1].split(",")
        return tuple(int(n) for n in (x1, y1, x2, y2))

    data = utils.load_data(2021, 5, fn=parse, example=False)

    return data


DATA = load_data()


def get_line_coords(x1, y1, x2, y2, *, ignore_diagonals=True):
    if x1 != x2 and y1 != y2 and ignore_diagonals:
        return []

    if x1 < x2:
        x_range = range(x1, x2 + 1)
    elif x1 > x2:
        x_range = reversed(range(x2, x1 + 1))
    else:
        x_range = [x1] * (abs(y1 - y2) + 1)

    if y1 < y2:
        y_range = range(y1, y2 + 1)
    elif y1 > y2:
        y_range = reversed(range(y2, y1 + 1))
    else:
        y_range = [y1] * (abs(x1 - x2) + 1)

    return zip(x_range, y_range)


def part1() -> int:
    board = Counter()
    for line in DATA:
        board.update(get_line_coords(*line))

    return len([v for v in board.values() if v >= 2])


def part2() -> int:
    board = Counter()
    for line in DATA:
        board.update(get_line_coords(*line, ignore_diagonals=False))

    return len([v for v in board.values() if v >= 2])


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
