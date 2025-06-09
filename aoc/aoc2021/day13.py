from aoc import utils

type Data = tuple[utils.Grid2D, list[tuple[str, int]]]


def parse_data(data: list[str]) -> Data:
    grid = utils.Grid2D()
    folds = []
    for line in data:
        if "," in line:
            x, y = line.split(",")
            grid[utils.Coord2D(int(x), int(y))] = 1
        elif line.startswith("fold along "):
            fold_line = line.split()[-1]
            axis, value = fold_line.split("=")
            folds.append((axis, int(value)))
    return grid, folds


def fold(grid: utils.Grid2D, axis: str, value: int) -> utils.Grid2D:
    new_grid = utils.Grid2D()
    for x, y in grid:
        if axis == "x" and x > value:
            x = 2 * value - x
        elif axis == "y" and y > value:
            y = 2 * value - y
        new_grid[utils.Coord2D(x, y)] = 1
    return new_grid


def part1(data: Data) -> int:
    grid, folds = data
    grid = fold(grid, folds[0][0], folds[0][1])
    return len(grid)


def part2(data: Data) -> str:
    grid, folds = data
    for axis, pos in folds:
        grid = fold(grid, axis, pos)

    return "\n" + str(grid)
