from aoc.aoc2017.day10 import knot_hash

type Data = list[str]


def get_grid(data: Data) -> list[list[str]]:
    hashes = [knot_hash(data[0] + "-" + str(i)) for i in range(128)]
    return [list(bin(int(h, 16))[2:].zfill(128)) for h in hashes]


def part1(data: Data) -> int:
    grid = get_grid(data)
    ones = 0
    for row in grid:
        ones += row.count("1")
    return ones


def get_neighbours(i: int, j: int) -> list[tuple[int, int]]:
    neighbours = []
    if i != 0:
        neighbours.append((i - 1, j))
    if i != 127:
        neighbours.append((i + 1, j))
    if j != 0:
        neighbours.append((i, j - 1))
    if j != 127:
        neighbours.append((i, j + 1))
    return neighbours


def flood_fill(grid: list[list[str]], i: int, j: int, fill: str = "0") -> None:
    to_expand = {(i, j)}
    match = grid[i][j]
    while to_expand:
        i, j = to_expand.pop()
        grid[i][j] = fill
        for i2, j2 in get_neighbours(i, j):
            if grid[i2][j2] == match:
                to_expand.add((i2, j2))


def part2(data: Data) -> int:
    grid = get_grid(data)
    groups = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j] == "1":
                flood_fill(grid, i, j)
                groups += 1
    return groups
