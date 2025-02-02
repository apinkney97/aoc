import re
import typing

from aoc import utils

INSTRUCTION_RE = re.compile(
    r"(?P<action>.*) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)"
)

type Data = list[re.Match[str]]


def parse_data(data: list[str]) -> Data:
    return [
        match
        for match in utils.parse_data(data, fn=lambda s: INSTRUCTION_RE.fullmatch(s))
        if match is not None
    ]


def get_coords(x1: int, y1: int, x2: int, y2: int) -> typing.Generator[int]:
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            yield 1000 * x + y


def part1(data: Data) -> int:
    grid = [0] * (1000 * 1000)

    for instruction in data:
        coords = get_coords(
            int(instruction["x1"]),
            int(instruction["y1"]),
            int(instruction["x2"]),
            int(instruction["y2"]),
        )
        action = instruction["action"]
        if action == "turn on":
            for coord in coords:
                grid[coord] = 1
        elif action == "turn off":
            for coord in coords:
                grid[coord] = 0
        elif action == "toggle":
            for coord in coords:
                grid[coord] = 1 - grid[coord]
        else:
            raise Exception(f"Bad action: {action}")

    return sum(grid)


def part2(data: Data) -> int:
    grid = [0] * (1000 * 1000)

    for instruction in data:
        coords = get_coords(
            int(instruction["x1"]),
            int(instruction["y1"]),
            int(instruction["x2"]),
            int(instruction["y2"]),
        )
        action = instruction["action"]
        if action == "turn on":
            for coord in coords:
                grid[coord] += 1
        elif action == "turn off":
            for coord in coords:
                grid[coord] = max(grid[coord] - 1, 0)
        elif action == "toggle":
            for coord in coords:
                grid[coord] += 2
        else:
            raise Exception(f"Bad action: {action}")

    return sum(grid)
