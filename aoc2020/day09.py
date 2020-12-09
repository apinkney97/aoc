from collections import deque
from itertools import combinations

import utils

DATA = utils.load_data(9, fn=int)


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

    start = 0
    end = 0

    while True:
        print("Trying", start, end)
        range_ = DATA[start : end + 1]
        value = sum(range_)
        if value > target:
            start += 1
        elif value < target:
            end += 1
        else:
            return max(range_) + min(range_)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
