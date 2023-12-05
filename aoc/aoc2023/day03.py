import re

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 3, example=EXAMPLE)

    return data


DATA = load_data()


class Number:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self):
        return f"{self.value}"


def part1() -> int:
    numbers_by_coord = {}
    symbols_by_coord = {}
    for y, line in enumerate(DATA):
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n = Number(int(number.group(0)))
            for x in range(number.start(), number.end()):
                numbers_by_coord[(x, y)] = n

        symbols = re.finditer(r"[^.\d]", line)
        for symbol in symbols:
            symbols_by_coord[(symbol.start(), y)] = symbol.group(0)

    part_numbers = set()

    for coord in symbols_by_coord.keys():
        for neighbour in utils.neighbours(coord, include_diagonals=True):
            if neighbour in numbers_by_coord:
                part_numbers.add(numbers_by_coord[neighbour])

    return sum(pn.value for pn in part_numbers)


def part2() -> int:
    numbers_by_coord = {}
    gears_coords = []
    for y, line in enumerate(DATA):
        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            n = Number(int(number.group(0)))
            for x in range(number.start(), number.end()):
                numbers_by_coord[(x, y)] = n

        gears = re.finditer(r"\*", line)
        for gear in gears:
            gears_coords.append((gear.start(), y))

    total = 0

    for coord in gears_coords:
        neighbour_nums = set()
        for neighbour in utils.neighbours(coord, include_diagonals=True):
            if neighbour in numbers_by_coord:
                neighbour_nums.add(numbers_by_coord[neighbour])
        if len(neighbour_nums) == 2:
            total += utils.product(n.value for n in neighbour_nums)
    return total


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
