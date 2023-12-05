from __future__ import annotations

import dataclasses
from collections import defaultdict, deque
from typing import Optional

import utils


def load_data():
    data = utils.load_data(2021, 12, example=False)

    adjacencies = defaultdict(list)

    small = set()

    for line in data:
        a, b = line.split("-")
        if a.islower():
            small.add(a)
        if b.islower():
            small.add(b)

        if a != "end" and b != "start":
            adjacencies[a].append(b)
        if b != "end" and a != "start":
            adjacencies[b].append(a)

    return adjacencies, small


DATA = load_data()


@dataclasses.dataclass
class Node:
    name: str
    parent: Optional[Node]
    has_double: bool = False


def is_ancestor(node: Node, name: str):
    while node is not None:
        if node.name == name:
            return True
        node = node.parent
    return False


def part1() -> int:
    start = Node("start", None)

    queue = deque()
    queue.append(start)

    ends = []

    adjacencies, small = DATA

    while queue:
        current = queue.popleft()
        for neighbour in adjacencies[current.name]:
            if neighbour in small and is_ancestor(current, neighbour):
                continue
            new_node = Node(name=neighbour, parent=current)
            if neighbour == "end":
                ends.append(new_node)
            queue.append(new_node)

    return len(ends)


def part2() -> int:
    start = Node("start", None)

    queue = deque()
    queue.append(start)

    ends = []

    adjacencies, small = DATA

    while queue:
        current = queue.popleft()
        for neighbour in adjacencies[current.name]:
            has_double = current.has_double
            if neighbour in small and is_ancestor(current, neighbour):
                if has_double:
                    continue
                has_double = True
            new_node = Node(name=neighbour, parent=current, has_double=has_double)
            if neighbour == "end":
                ends.append(new_node)
            queue.append(new_node)

    return len(ends)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")

    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
