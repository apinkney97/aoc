from itertools import cycle

from aoc2018.util import load_data


def part1():
    return sum(int(d) for d in load_data(1))


def part2():
    curr = 0
    seen = {0}

    for val in cycle(int(d) for d in load_data(1)):
        curr += val
        if curr in seen:
            return curr
        seen.add(curr)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
