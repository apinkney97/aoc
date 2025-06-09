import itertools

type Data = list[str]


def get_sizes(universe: list[str], expand: int) -> tuple[list[int], list[int]]:
    row_sizes = []
    cols: list[set[str]] = [set() for _ in universe[0]]

    for line in universe:
        if set(line) == {"."}:
            row_sizes.append(expand)
        else:
            row_sizes.append(1)
        for i, cell in enumerate(line):
            cols[i].add(cell)

    col_sizes = []

    for col in cols:
        if col == {"."}:
            col_sizes.append(expand)
        else:
            col_sizes.append(1)

    return row_sizes, col_sizes


def get_gx_coords(universe: list[str]) -> list[tuple[int, int]]:
    galaxies = []
    for y, row in enumerate(universe):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))
    return galaxies


def part1(data: Data, expand: int = 2) -> int:
    result = 0

    row_sizes, col_sizes = get_sizes(data, expand=expand)
    galaxies = get_gx_coords(data)

    for (x1, y1), (x2, y2) in itertools.combinations(galaxies, 2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        result += sum(col_sizes[x1:x2]) + sum(row_sizes[y1:y2])

    return result


def part2(data: Data) -> int:
    return part1(data, expand=1000000)
