type Data = list[tuple[str, int]]


def parse_data(data: list[str]) -> Data:
    parsed = []

    for line in data:
        direction, distance_raw = line.split()
        distance = int(distance_raw)
        parsed.append((direction, distance))

    return parsed


DIRS = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1),
}


def get_tail_pos(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail

    dx = hx - tx
    dy = hy - ty

    if abs(dx) > 1 or abs(dy) > 1:
        if not (dx and dy):
            # orthogonal move only
            tx += dx // 2
            ty += dy // 2
        else:
            # diagonal
            tx += dx // abs(dx)
            ty += dy // abs(dy)

    return tx, ty


def part1(data: Data, rope_len: int = 2) -> int:
    rope = [(0, 0)] * rope_len

    visited = set()

    for direction, distance in data:
        move = DIRS[direction]
        for _ in range(distance):
            # move head
            rope[0] = (rope[0][0] + move[0], rope[0][1] + move[1])

            # move tail parts
            for i in range(1, rope_len):
                rope[i] = get_tail_pos(rope[i - 1], rope[i])

            visited.add(rope[-1])

    return len(visited)


def part2(data: Data) -> int:
    return part1(data, rope_len=10)
