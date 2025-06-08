import string

type Data = list[str]

type Coord = tuple[int, int]


class NoPathFoundError(Exception):
    pass


TOTAL_STEPS = -1


def get_next_pos(path: Data, been: set[Coord], curr: Coord, prev: Coord) -> Coord:
    # always go straight on unless curr is '+'
    x, y = curr
    prev_x, prev_y = prev

    if path[x][y] != "+":
        next_x = 2 * x - prev_x
        next_y = 2 * y - prev_y
        if not is_valid_pos(path, next_x, next_y):
            raise NoPathFoundError("{}, {}", next_x, next_y)
        return next_x, next_y

    for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if not is_valid_pos(path, next_x, next_y):
            continue
        val = path[next_x][next_y]
        if val != " " and (next_x, next_y) not in been:
            return next_x, next_y

    raise NoPathFoundError


def is_valid_pos(path: Data, x: int, y: int) -> bool:
    return 0 <= x < len(path) and 0 <= y < len(path[x])


def part1(data: Data) -> str:
    path = data

    # path = [
    #     "     |          ",
    #     "     |  +--+    ",
    #     "     A  |  C    ",
    #     " F---|----E|--+ ",
    #     "     |  |  |  D ",
    #     "     +B-+  +--+ ",
    #  ]

    curr: Coord
    prev: Coord

    for i, c in enumerate(path[0]):
        if c == "|":
            curr = 0, i
            prev = -1, i
            break
    else:
        raise NoPathFoundError

    been: set[Coord] = set()
    letters = []

    global TOTAL_STEPS
    TOTAL_STEPS = 0

    while True:
        val = path[curr[0]][curr[1]]
        if val in string.ascii_letters:
            letters.append(val)
        elif val == " ":
            break
        TOTAL_STEPS += 1
        been.add(curr)
        next_pos = get_next_pos(path, been, curr, prev)
        prev = curr
        curr = next_pos
    return "".join(letters)


def part2(data: Data) -> int:
    return TOTAL_STEPS
