import re
from itertools import cycle
from math import lcm

type Data = tuple[list[int], dict[str, list[str]]]


def parse_data(data: list[str]) -> Data:
    directions = [0 if d == "L" else 1 for d in data[0]]
    matcher = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    tree = {}
    for line in data[2:]:
        match = matcher.fullmatch(line)
        assert match is not None
        tree[match.group(1)] = [match.group(2), match.group(3)]

    return directions, tree


def part1(data: Data) -> int:
    directions, tree = data

    current = "AAA"
    target = "ZZZ"
    for i, direction in enumerate(cycle(directions)):
        if current == target:
            return i
        current = tree[current][direction]

    return -1


def part2(data: Data) -> int:
    directions, tree = data
    print(len(directions))
    start_nodes = list(node for node in tree if node.endswith("A"))

    seen: list[set[tuple[int, str]]] = [set() for _ in start_nodes]
    done: set[int] = set()
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
    for current_node in start_nodes:
        for i, direction in enumerate(cycle(directions)):
            if current_node[2] == "Z":
                distances.append(i)
                break
            current_node = tree[current_node][direction]

    for x in zip(start_nodes, distances):
        print(x)

    return lcm(*distances)  # I mean, ok, I'll take it
