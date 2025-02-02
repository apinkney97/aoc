import re

from aoc import utils


class Number:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self):
        return f"{self.value}"


def part1(data) -> int:
    numbers_by_coord = {}
    symbols_by_coord = {}
    for y, line in enumerate(data):
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n = Number(int(number.group(0)))
            for x in range(number.start(), number.end()):
                numbers_by_coord[utils.Coord2D(x, y)] = n

        symbols = re.finditer(r"[^.\d]", line)
        for symbol in symbols:
            symbols_by_coord[utils.Coord2D(symbol.start(), y)] = symbol.group(0)

    part_numbers = set()

    for coord in symbols_by_coord.keys():
        for neighbour in utils.neighbours(coord, include_diagonals=True):
            if neighbour in numbers_by_coord:
                part_numbers.add(numbers_by_coord[neighbour])

    return sum(pn.value for pn in part_numbers)


def part2(data) -> int:
    numbers_by_coord = {}
    gears_coords = []
    for y, line in enumerate(data):
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n = Number(int(number.group(0)))
            for x in range(number.start(), number.end()):
                numbers_by_coord[utils.Coord2D(x, y)] = n

        gears = re.finditer(r"\*", line)
        for gear in gears:
            gears_coords.append(utils.Coord2D(gear.start(), y))

    total = 0

    for coord in gears_coords:
        neighbour_nums = set()
        for neighbour in utils.neighbours(coord, include_diagonals=True):
            if neighbour in numbers_by_coord:
                neighbour_nums.add(numbers_by_coord[neighbour])
        if len(neighbour_nums) == 2:
            total += utils.product(n.value for n in neighbour_nums)
    return total
