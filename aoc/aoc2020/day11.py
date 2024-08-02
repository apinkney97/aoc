from aoc import utils


def parse_data(data):
    return utils.parse_data(data, fn=list)


def get_adjacent_neighbours(row, col, data):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i < 0 or j < 0 or (i, j) == (row, col):
                continue
            try:
                yield data[i][j]
            except IndexError:
                pass


def get_visible_neighbours(row, col, data):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for dr, dc in directions:
        r, c = row, col

        while True:
            r += dr
            c += dc
            if r < 0 or c < 0:
                break

            try:
                val = data[r][c]
            except IndexError:
                break

            if val in {"#", "L"}:
                yield val
                break


def step(data, neighbour_fn, limit):
    new_data = []
    changed = False

    for row in range(len(data)):
        new_row = []
        new_data.append(new_row)

        for col in range(len(data[row])):
            state = data[row][col]

            neighbours = 0

            if state != ".":
                for neighbour in neighbour_fn(row, col, data):
                    if neighbour == "#":
                        neighbours += 1

            if state == "L" and neighbours == 0:
                new_state = "#"
                changed = True

            elif state == "#" and neighbours >= limit:
                new_state = "L"
                changed = True

            else:
                new_state = state

            new_row.append(new_state)

    return changed, new_data


def run(data, neighbour_fn, limit):
    changed = True

    while changed:
        changed, data = step(data, neighbour_fn=neighbour_fn, limit=limit)

    return sum(row.count("#") for row in data)


def part1(data) -> int:
    return run(data, neighbour_fn=get_adjacent_neighbours, limit=4)


def part2(data) -> int:
    return run(data, neighbour_fn=get_visible_neighbours, limit=5)
