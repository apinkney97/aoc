from itertools import combinations

from aoc.utils import PQ, Coord2D, log

type Data = list[Coord2D]


def parse_data(data: list[str]) -> Data:
    coords = []
    for line in data:
        x, y = map(int, line.split(","))
        coords.append(Coord2D(x, y))
    return coords


def part1(data: Data) -> int:
    result = 0
    for c1, c2 in combinations(data, 2):
        result = max(result, area(c1, c2))
    return result


def area(c1: Coord2D, c2: Coord2D) -> int:
    w = 1 + abs(c1.x - c2.x)
    h = 1 + abs(c1.y - c2.y)
    return w * h


def dump_ps(data: Data) -> None:
    scale = 5
    with open("day09.ps", "w") as f:
        start = data[0]
        f.write("%!\n")
        f.write("0.001 0.001 scale\n")
        f.write(f"newpath {start.x * scale} {start.y * scale} moveto\n")
        for c in data[1:]:
            f.write(f"{c.x * scale} {c.y * scale} lineto\n")
        f.write("closepath 0 setgray fill\n")


def part2(data: Data) -> int:
    # dump_ps(data); return 0

    lines: list[tuple[Coord2D, Coord2D]] = []

    # Add all candidate squares to a queue, taking biggest first
    queue: PQ[tuple[Coord2D, Coord2D]] = PQ(max_heap=True)
    for coord_pair in combinations(data, 2):
        queue.add_item(coord_pair, priority=area(coord_pair[0], coord_pair[1]))

    for c1, c2 in zip(data, data[1:] + data[:1]):
        lines.append((c1, c2))

    candidates = len(queue)
    while queue:
        c1, c2 = queue.pop_item()
        # I don't think this is a general solution, since it will match large squares on concave edges
        # on the exterior of the shape. But it works on the puzzle input so :shrug:
        if not any(line_inside(c1, c2, end1, end2) for end1, end2 in lines):
            tested = candidates - len(queue)
            w = 1 + abs(c1.x - c2.x)
            h = 1 + abs(c1.y - c2.y)
            log(f"Checked {tested} / {candidates}  ({tested / candidates * 100:.2f}%)")
            return w * h

    return 0


def line_inside(
    corner1: Coord2D, corner2: Coord2D, end1: Coord2D, end2: Coord2D
) -> bool:
    # Given two points defining a square, and 2 points defining a horizontal or vertical line,
    # return True if the line is inside the square at any point

    # A line is inside if:
    # - Either end is inside
    # - Both ends are outside on opposite sides and the Y/X (constant) is inside

    assert end1.x == end2.x or end1.y == end2.y, "Line must be horizontal or vertical"

    tl = Coord2D(min(corner1.x, corner2.x), min(corner1.y, corner2.y))
    br = Coord2D(max(corner1.x, corner2.x), max(corner1.y, corner2.y))

    # end 1 inside
    if tl.x < end1.x < br.x and tl.y < end1.y < br.y:
        return True

    # end 2 inside
    if tl.x < end2.x < br.x and tl.y < end2.y < br.y:
        return True

    if end1.x == end2.x:
        # vertical line
        if not tl.x < end1.x < br.x:
            # line outside
            return False
        y1, y2 = sorted([end1.y, end2.y])
        return y1 <= tl.y and y2 >= br.y

    # horizontal line
    if not tl.y < end1.y < br.y:
        # line outside
        return False
    x1, x2 = sorted([end1.x, end2.x])
    return x1 <= tl.x and x2 >= br.x
