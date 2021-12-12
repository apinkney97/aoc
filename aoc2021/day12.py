from __future__ import annotations

import dataclasses
from collections import defaultdict, deque
from typing import Optional

import utils


def load_data():
    data = utils.load_data(12, example=False)

    adjacencies = defaultdict(list)

    for line in data:
        a, b = line.split("-")
        if a != "end" and b != "start":
            adjacencies[a].append(b)
        if b != "end" and a != "start":
            adjacencies[b].append(a)

    return adjacencies


DATA = load_data()


@dataclasses.dataclass
class Node:
    name: str
    parent: Optional[Node]
    has_double: bool = False


def is_ancestor(node: Node, name: str):
    if node.name == name:
        return True
    while node.parent is not None:
        node = node.parent
        if node.name == name:
            return True
    return False


def part1() -> int:
    start = Node("start", None)

    queue = deque()
    queue.append(start)

    ends = []

    while queue:
        current = queue.popleft()
        for neighbour in DATA[current.name]:
            if neighbour.islower() and is_ancestor(current, neighbour):
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

    while queue:
        current = queue.popleft()
        for neighbour in DATA[current.name]:
            has_double = current.has_double
            if neighbour.islower() and is_ancestor(current, neighbour):
                if has_double:
                    continue
                has_double = True
            new_node = Node(name=neighbour, parent=current, has_double=has_double)
            if neighbour == "end":
                ends.append(new_node)
            queue.append(new_node)

    return len(ends)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
