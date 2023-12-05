from aoc import utils


def load_data():
    data = utils.load_data(2021, 13, example=False)
    grid = utils.Grid2D()
    folds = []
    for line in data:
        if "," in line:
            x, y = line.split(",")
            grid[(int(x), int(y))] = 1
        elif line.startswith("fold along "):
            fold_line = line.split()[-1]
            axis, value = fold_line.split("=")
            folds.append((axis, int(value)))
    return grid, folds


DATA = load_data()


def fold(grid: utils.Grid2D, axis: str, value: int) -> utils.Grid2D:
    new_grid = utils.Grid2D()
    for x, y in grid:
        if axis == "x" and x > value:
            x = 2 * value - x
        elif axis == "y" and y > value:
            y = 2 * value - y
        new_grid[(x, y)] = 1
    return new_grid


def part1() -> int:
    grid, folds = DATA
    grid = fold(grid, folds[0][0], folds[0][1])
    return len(grid)


def part2() -> str:
    grid, folds = DATA
    for axis, pos in folds:
        grid = fold(grid, axis, pos)

    return "\n" + str(grid)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
