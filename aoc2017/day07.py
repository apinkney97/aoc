from collections import defaultdict, deque

import utils


def get_data():
    data = {}
    for line in utils.load_data(2017,7):
        bits = line.split(" ")
        name = bits[0]
        weight = int(bits[1][1:-1])
        children = sorted(n.strip(",") for n in bits[3:])
        data[name] = weight, children

    return data


def part1(data):
    counts = defaultdict(int)
    for name, (_, children) in data.items():
        counts[name] += 1
        for child in children:
            counts[child] += 1

    for name, count in counts.items():
        if count == 1:
            return name
    raise Exception("Couldn't find root")


class Node:
    def __init__(self, name, weight, parent):
        self.kids = []
        self.name = name
        self.weight = weight
        self.parent = parent

    def total_weight(self):
        return self.weight + sum(k.total_weight() for k in self.kids)

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.name, self.weight)

    def print_tree(self, indent=0):
        print((" " * indent) + repr(self) + ("" if self.is_balanced() else "*****"))
        for kid in self.kids:
            kid.print_tree(indent + 1)

    def is_balanced(self):
        if len(self.kids) < 2:
            return True
        expected = self.kids[0].total_weight()
        return all(k.total_weight() == expected for k in self.kids)


def part2(data):
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

    nodes = {}
    for node in curr_node.kids:
        nodes.setdefault(node.total_weight(), []).append(node)

    bad = good = None

    for nodes_list in nodes.values():
        if len(nodes_list) == 1:
            bad = nodes_list[0]
        else:
            good = nodes_list[0]

    if None in (good, bad):
        raise Exception("Couldn't determine bad node")

    return bad.weight - bad.total_weight() + good.total_weight()


def main():
    data = get_data()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))


if __name__ == "__main__":
    main()
