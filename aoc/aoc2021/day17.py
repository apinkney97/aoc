import re

type Data = tuple[int, int, int, int]


def parse_data(data: list[str]) -> Data:
    match = re.fullmatch(
        r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", data[0]
    )
    assert match is not None
    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )


def part1(data: Data) -> int:
    x1, x2, y1, y2 = data

    # dy downwards will equal dy upwards at the same y value
    # so, initial velocities higher than abs(y1) will make us overshoot in 1 step
    global_max_y = 0
    for dy in range(y1, abs(y1) + 1):
        y = 0

        max_y = 0
        while y >= y2:
            y += dy
            max_y = max(y, max_y)
            dy -= 1
            if y1 <= y <= y2:
                global_max_y = max(global_max_y, max_y)

    return global_max_y


def part2(data: Data) -> int:
    x1, x2, y1, y2 = data

    initial_velocities = set()

    for initial_dy in range(y1, abs(y1) + 1):
        for initial_dx in range(1, x2 + 1):
            x = y = 0

            dx = initial_dx
            dy = initial_dy

            while y >= y1:
                x += dx
                y += dy
                dx = max(dx - 1, 0)
                dy -= 1

                if y1 <= y <= y2 and x1 <= x <= x2:
                    initial_velocities.add((initial_dx, initial_dy))

    return len(initial_velocities)
