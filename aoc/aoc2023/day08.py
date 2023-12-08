import re
from itertools import cycle
from math import lcm

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 8, example=EXAMPLE)
    directions = [0 if d == "L" else 1 for d in data[0]]
    matcher = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    tree = {}
    for line in data[2:]:
        match = matcher.fullmatch(line)
        tree[match.group(1)] = [match.group(2), match.group(3)]

    return directions, tree


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    directions, tree = DATA

    current = "AAA"
    target = "ZZZ"
    for i, direction in enumerate(cycle(directions)):
        if current == target:
            return i
        current = tree[current][direction]

    return -1


def part2() -> int:
    directions, tree = DATA
    print(len(directions))
    start_nodes = tuple(node for node in tree if node.endswith("A"))

    seen = [set() for _ in start_nodes]
    done = set()
    current = start_nodes
    for i, (cycle_step, direction) in enumerate(cycle(enumerate(directions))):
        for n, node in enumerate(current):
            if n in done:
                continue
            if (cycle_step, node) in seen[n]:
                print("Cycle found:", cycle_step, node, start_nodes[n], i)
                done.add(n)
            else:
                seen[n].add((cycle_step, node))
        if len(done) == len(start_nodes):
            break
        current = [tree[c][direction] for c in current]

    distances = []
    for current in start_nodes:
        for i, direction in enumerate(cycle(directions)):
            if current[2] == "Z":
                distances.append(i)
                break
            current = tree[current][direction]

    for x in zip(start_nodes, distances):
        print(x)

    return lcm(*distances)  # I mean, ok, I'll take it


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
