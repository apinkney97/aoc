from aoc import utils


def parse_data(data):
    data = utils.parse_data(data, fn=lambda line: [0 if c == "." else 1 for c in line])

    bounds = (0, len(data[0]), 0, len(data))
    grid = utils.Grid2D(display_map={0: ".", 1: "#"}, bounds=bounds)
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            grid[x, y] = val

    return grid


def light_corners(grid: utils.Grid2D) -> None:
    xmin, xmax, ymin, ymax = grid._bounds
    xmax -= 1
    ymax -= 1
    grid[xmin, ymin] = 1
    grid[xmin, ymax] = 1
    grid[xmax, ymin] = 1
    grid[xmax, ymax] = 1


def step(grid: utils.Grid2D) -> utils.Grid2D:
    survives = {2, 3}
    appears = {3}

    new_grid = grid.blank_copy()

    old_coords = set(grid)
    for coord in old_coords:
        for neighbour in utils.neighbours(coord, include_diagonals=True):
            new_grid[neighbour] += 1

    new_coords = set(new_grid)
    for coord in new_coords:
        neighbour_count = new_grid[coord]
        if (neighbour_count in survives and coord in old_coords) or (
            neighbour_count in appears and coord not in old_coords
        ):
            new_grid[coord] = 1
        else:
            new_grid[coord] = 0

    return new_grid


def part1(data) -> int:
    grid = data
    for _ in range(100):
        grid = step(grid)
    return len(grid)


def part2(data) -> int:
    grid = data
    light_corners(grid)
    for _ in range(100):
        grid = step(grid)
        light_corners(grid)
    return len(grid)
