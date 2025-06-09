from collections import Counter
from typing import Iterable

type Data = list[tuple[int, int, int, int]]


def parse_data(data: list[str]) -> Data:
    def parse(line: str) -> tuple[int, int, int, int]:
        parts = line.split(" -> ")
        x1, y1 = parts[0].split(",")
        x2, y2 = parts[1].split(",")
        return int(x1), int(y1), int(x2), int(y2)

    return [parse(line) for line in data]


def get_line_coords(
    x1: int, y1: int, x2: int, y2: int, *, ignore_diagonals: bool = True
) -> Iterable[tuple[int, int]]:
    if x1 != x2 and y1 != y2 and ignore_diagonals:
        return []

    x_range: Iterable[int]
    y_range: Iterable[int]

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


def part1(data: Data) -> int:
    board: Counter[tuple[int, int]] = Counter()
    for line in data:
        board.update(get_line_coords(*line))

    return len([v for v in board.values() if v >= 2])


def part2(data: Data) -> int:
    board: Counter[tuple[int, int]] = Counter()
    for line in data:
        board.update(get_line_coords(*line, ignore_diagonals=False))

    return len([v for v in board.values() if v >= 2])
