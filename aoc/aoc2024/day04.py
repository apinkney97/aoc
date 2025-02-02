from enum import Enum, unique


@unique
class Direction(Enum):
    NORTH = (0, -1)
    NORTH_EAST = (1, -1)
    EAST = (1, 0)
    SOUTH_EAST = (1, 1)
    SOUTH = (0, 1)
    SOUTH_WEST = (-1, 1)
    WEST = (-1, 0)
    NORTH_WEST = (-1, -1)


def is_xmas(data: list[str], x: int, y: int, direction: Direction) -> bool:
    for char in "XMAS":
        if x < 0 or y < 0 or y >= len(data) or x >= len(data[y]):
            return False

        if data[y][x] != char:
            return False

        dx, dy = direction.value
        x += dx
        y += dy

    return True


def is_x_mas(data: list[str], x: int, y: int) -> bool:
    if data[y][x] != "A":
        return False

    ul = data[y - 1][x - 1]
    lr = data[y + 1][x + 1]

    ur = data[y - 1][x + 1]
    ll = data[y + 1][x - 1]

    return {ul, lr} == {ur, ll} == {"M", "S"}


def part1(data: list[str]) -> int:
    result = 0
    for y, line in enumerate(data):
        for x in range(len(line)):
            for direction in Direction:
                if is_xmas(data, x, y, direction):
                    result += 1
    return result


def part2(data: list[str]) -> int:
    result = 0
    for y, line in enumerate(data[1:-1], start=1):
        for x in range(1, len(line) - 1):
            if is_x_mas(data, x, y):
                result += 1

    return result
