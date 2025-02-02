from collections.abc import Iterable
from itertools import groupby

from aoc.utils import rotate_anticlockwise, rotate_clockwise

type Data = list[list[str]]


def parse_data(data: list[str]) -> Data:
    return rotate_anticlockwise(data)


def tilt_line_left(line: list[str]) -> list[str]:
    out: list[str] = []
    group: Iterable[str]
    for key, group in groupby(line, lambda x: x == "#"):
        if not key:
            group = sorted(group, reverse=True)
        out.extend(group)

    return out


def tilt_left(lines: list[list[str]]) -> list[list[str]]:
    return [tilt_line_left(line) for line in lines]


def get_score(line: list[str]) -> int:
    score = 0
    for i, char in enumerate(reversed(line), start=1):
        if char == "O":
            score += i
    return score


def part1(data: Data) -> int:
    score = 0
    for line in data:
        tilted = tilt_line_left(line)
        score += get_score(tilted)

    return score


def part2(data: Data) -> int:
    state_to_pos: dict[str, int] = {get_key(data): 0}
    states = [data]

    cycle_start = 0
    cycle_end = 0

    billion = 1_000_000_000
    for i in range(1, billion):
        # Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east.
        for _ in range(4):
            data = tilt_left(data)
            data = rotate_clockwise(data)

        key = get_key(data)
        if key in state_to_pos:
            cycle_start = state_to_pos[key]
            cycle_end = i
            print(f"Found cycle at step {i}, from step {state_to_pos[key]}")
            break

        state_to_pos[key] = i
        states.append(data)

    cycle_length = cycle_end - cycle_start
    billionth_step = (billion - cycle_start) % cycle_length + cycle_start

    print(f"{billionth_step=}")
    return sum(get_score(line) for line in states[billionth_step])


def get_key(grid: list[list[str]]) -> str:
    parts = []
    for row in grid:
        parts.extend(row)
    return "".join(parts)
