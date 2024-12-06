import itertools

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse_data(data):
    start = None
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "^":
                start = (x, y)
    grid = [[c for c in line] for line in data]
    return grid, start


class OutOfBoundsError(Exception):
    pass


class LoopError(Exception):
    pass


def is_wall(grid, x, y):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        raise OutOfBoundsError
    return grid[y][x] == "#"


def get_visited(grid, start) -> set[tuple[int, int]]:
    dirs = itertools.cycle(DIRECTIONS)
    dx, dy = next(dirs)
    visited = {start}

    visited_with_direction = {(start, (dx, dy))}

    x, y = start

    try:
        while True:
            while not is_wall(grid, x + dx, y + dy):
                x += dx
                y += dy
                visited.add((x, y))
                pos_and_direction = ((x, y), (dx, dy))
                if pos_and_direction in visited_with_direction:
                    raise LoopError
                visited_with_direction.add(pos_and_direction)
            dx, dy = next(dirs)

    except OutOfBoundsError:
        return visited


def part1(data) -> int:
    grid, start = data
    return len(get_visited(grid, start))


def part2(data) -> int:
    grid, start = data
    result = 0

    visited = get_visited(grid, start)
    visited.remove(start)

    for x, y in visited:
        grid[y][x] = "#"
        try:
            get_visited(grid, start)
        except LoopError:
            result += 1
        grid[y][x] = "."

    return result
