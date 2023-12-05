import re

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    r = re.compile(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)")
    data = utils.load_data(2021, 17, example=EXAMPLE, fn=r.fullmatch)
    match = data[0]
    return tuple(int(match.group(n + 1)) for n in range(4))


DATA = load_data()


def part1() -> int:
    x1, x2, y1, y2 = DATA

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


def part2() -> int:
    x1, x2, y1, y2 = DATA

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


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
