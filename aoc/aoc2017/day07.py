from __future__ import annotations

import typing
from collections import defaultdict, deque

type Data = dict[str, tuple[int, list[str]]]


def parse_data(data: list[str]) -> Data:
    parsed_data = {}
    for line in data:
        bits = line.split(" ")
        name = bits[0]
        weight = int(bits[1][1:-1])
        children = sorted(n.strip(",") for n in bits[3:])
        parsed_data[name] = weight, children

    return parsed_data


def part1(data: Data) -> str:
    counts: typing.DefaultDict[str, int] = defaultdict(int)
    for name, (_, children) in data.items():
        counts[name] += 1
        for child in children:
            counts[child] += 1

    for name, count in counts.items():
        if count == 1:
            return name
    raise Exception("Couldn't find root")


class Node:
    def __init__(self, name: str, weight: int, parent: Node | None):
        self.kids: list[Node] = []
        self.name = name
        self.weight = weight
        self.parent = parent

    def total_weight(self) -> int:
        return self.weight + sum(k.total_weight() for k in self.kids)

    def __repr__(self) -> str:
        return "Node({!r}, {!r})".format(self.name, self.weight)

    def print_tree(self, indent: int = 0) -> None:
        print((" " * indent) + repr(self) + ("" if self.is_balanced() else "*****"))
        for kid in self.kids:
            kid.print_tree(indent + 1)

    def is_balanced(self) -> bool:
        if len(self.kids) < 2:
            return True
        expected = self.kids[0].total_weight()
        return all(k.total_weight() == expected for k in self.kids)


def part2(data: Data) -> int:
    root_name = part1(data)
    root = Node(name=root_name, weight=data[root_name][0], parent=None)

    # build tree
    to_expand = deque([root])
    while to_expand:
        curr_node = to_expand.popleft()
        for node_name in data[curr_node.name][1]:
            new_node = Node(name=node_name, weight=data[node_name][0], parent=curr_node)
            curr_node.kids.append(new_node)
            to_expand.append(new_node)

    # find parent of unbalanced node
    curr_node = root
    while True:
        for n in curr_node.kids:
            if not n.is_balanced():
                curr_node = n
                break
        else:
            break

    nodes: dict[int, list[Node]] = {}
    for node in curr_node.kids:
        nodes.setdefault(node.total_weight(), []).append(node)

    bad = good = None

    for nodes_list in nodes.values():
        if len(nodes_list) == 1:
            bad = nodes_list[0]
        else:
            good = nodes_list[0]

    if bad is None or good is None:
        raise Exception("Couldn't determine bad node")

    return bad.weight - bad.total_weight() + good.total_weight()
