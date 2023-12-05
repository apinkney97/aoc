from collections import deque
from itertools import combinations

import utils

DATA = utils.load_data(2020, 9, fn=int)


def part1() -> int:
    preamble = 25
    window = deque(DATA[:preamble])
    for val in DATA[preamble:]:
        for a, b in combinations(window, 2):
            if val == a + b:
                break
        else:
            return val
        window.popleft()
        window.append(val)

    raise Exception("No value found")


def part2() -> int:
    target = part1()

    window = deque()
    data = iter(DATA)

    while True:
        value = sum(window)
        if value > target:
            window.popleft()
        elif value < target:
            window.append(next(data))
        else:
            return max(window) + min(window)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
