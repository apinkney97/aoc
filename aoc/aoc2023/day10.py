import enum

type Data = tuple[tuple[int, int], list[str]]

DISPLAY_MAP = {
    "-": "━",
    "|": "┃",
    "F": "┏",
    "7": "┓",
    "L": "┗",
    "J": "┛",
}


class Direction(enum.Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


TRANSITIONS = {
    Direction.NORTH: {
        "|": Direction.NORTH,
        "F": Direction.EAST,
        "7": Direction.WEST,
    },
    Direction.EAST: {
        "-": Direction.EAST,
        "J": Direction.NORTH,
        "7": Direction.SOUTH,
    },
    Direction.SOUTH: {
        "|": Direction.SOUTH,
        "L": Direction.EAST,
        "J": Direction.WEST,
    },
    Direction.WEST: {
        "-": Direction.WEST,
        "F": Direction.SOUTH,
        "L": Direction.NORTH,
    },
}


def display(lines: list[str]) -> str:
    out = []
    for line in lines:
        for old, new in DISPLAY_MAP.items():
            line = line.replace(old, new)
        out.append(line)
    return "\n".join(out)


def parse_data(data: list[str]) -> Data:
    start_x = -1
    start_y = -1
    for start_y, line in enumerate(data):
        if "S" in line:
            start_x = line.index("S")
            break
    return (start_x, start_y), data


def get_loop_tiles(
    start_pos: tuple[int, int], lines: list[str]
) -> tuple[str, set[tuple[int, int]]]:
    x, y = start_pos

    start_directions = []

    for direction in Direction:
        dx, dy = direction.value
        tile = lines[y + dy][x + dx]
        if tile in TRANSITIONS[direction]:
            start_directions.append(direction)

    direction = start_directions[0]
    x += direction.value[0]
    y += direction.value[1]

    tiles_in_loop = {start_pos, (x, y)}

    while lines[y][x] != "S":
        direction = TRANSITIONS[direction][lines[y][x]]
        dx, dy = direction.value
        x += dx
        y += dy
        tiles_in_loop.add((x, y))

    sds = set(start_directions)
    if sds == {Direction.NORTH, Direction.SOUTH}:
        start_tile = "|"
    elif sds == {Direction.EAST, Direction.WEST}:
        start_tile = "-"
    elif sds == {Direction.NORTH, Direction.EAST}:
        start_tile = "L"
    elif sds == {Direction.NORTH, Direction.WEST}:
        start_tile = "J"
    elif sds == {Direction.SOUTH, Direction.WEST}:
        start_tile = "7"
    elif sds == {Direction.SOUTH, Direction.EAST}:
        start_tile = "F"
    else:
        raise Exception("uh oh")

    return start_tile, tiles_in_loop


def part1(data: Data) -> int:
    start_pos, lines = data

    return round(len(get_loop_tiles(start_pos, lines)[1]) / 2)


def part2(data: Data) -> int:
    start_pos, lines = data

    start_tile, loop_tiles = get_loop_tiles(start_pos, lines)
    lines[start_pos[1]] = lines[start_pos[1]].replace("S", start_tile)

    # print(display(lines))

    result = 0

    for y, line in enumerate(lines):
        inside = False
        for x, tile in enumerate(line):
            if (x, y) in loop_tiles:
                if tile not in "-LJ":
                    inside = not inside
            elif inside:
                result += 1

    return result
