from aoc2017.util import load_data


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class SpinLock:
    def __init__(self, head_value=0):
        head = Node(head_value, None)
        head.next_node = head
        self.head = head
        self.curr = head

    def insert(self, value):
        new_node = Node(value, self.curr.next_node)
        self.curr.next_node = new_node
        self.curr = new_node

    def to_list(self):
        vals = [self.head.value]
        node = self.head.next_node
        while node is not self.head:
            vals.append(node.value)
            node = node.next_node
        return vals

    def skip(self, distance):
        for _ in range(distance):
            self.curr = self.curr.next_node


def get_data():
    return int(load_data(17)[0])


def part1():
    step = get_data()
    spinlock = SpinLock()

    max_val = 2017
    for i in range(1, max_val + 1):
        spinlock.insert(i)
        if i != max_val:
            spinlock.skip(step)

    return spinlock.curr.next_node.value


def part2():
    step = get_data()
    curr = 0
    val = 0
    for i in range(1, 50000000 + 1):
        if curr == 0:
            val = i
        curr = (curr + step + 1) % (i + 1)
    return val


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
