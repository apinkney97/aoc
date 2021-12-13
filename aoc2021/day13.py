import utils

Coord = tuple[int, int]


class Grid:
    def __init__(self, default_val: int = 0):
        self._default_val = default_val
        self._grid: dict[Coord, int] = {}
        self.max_x: int = 0
        self.max_y: int = 0

    def __setitem__(self, key: Coord, value: int):
        if value == self._default_val:
            self._grid.pop(key, None)
        else:
            self._grid[key] = value
        self.max_x = max(self.max_x, key[0])
        self.max_y = max(self.max_y, key[1])

    def __getitem__(self, key):
        return self._grid.get(key, self._default_val)

    def __iter__(self):
        return iter(self._grid)

    def __len__(self):
        return len(self._grid)

    def __str__(self):
        lines = []
        for y in range(self.max_y + 1):
            line = []
            for x in range(self.max_x + 1):
                line.append("███" if self[(x, y)] == 1 else "   ")
            lines.append("".join(line))
        return "\n".join(lines)


def load_data():
    data = utils.load_data(13, example=False)
    grid = Grid()
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


def fold(grid: Grid, axis: str, value: int) -> Grid:
    new_grid = Grid()
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
