from typing import Dict, Optional

import utils


class LinkedCup:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[LinkedCup] = None

    def __repr__(self):
        return f"Cup({self.val})"


def load_data():
    data = utils.load_data(2020, 23, example=False)

    return [int(n) for n in data[0]]


DATA = load_data()


def get_dest(n: int, max_item: int):
    n = (n - 1) % max_item
    if n == 0:
        n = max_item
    return n


def add_linked_cup(
    value: int, cups_map: Dict[int, LinkedCup], prev: LinkedCup
) -> LinkedCup:
    new_cup = LinkedCup(value)
    cups_map[value] = new_cup
    prev.next = new_cup
    return new_cup


def move_cups(current: LinkedCup, cups_map: Dict[int, LinkedCup], max_val: int) -> None:

    removed = [current.next, current.next.next, current.next.next.next]
    removed_vals = {r.val for r in removed}

    current.next = removed[-1].next

    dest_n = get_dest(current.val, max_val)

    while dest_n in removed_vals:
        dest_n = get_dest(dest_n, max_val)

    dest = cups_map[dest_n]

    removed[-1].next = dest.next
    dest.next = removed[0]


@utils.timed
def part1() -> str:
    current = LinkedCup(DATA[0])
    cups_map = {DATA[0]: current}

    c = current
    for value in DATA[1:]:
        c = add_linked_cup(value, cups_map, c)

    c.next = current

    for _ in range(100):
        move_cups(current, cups_map, 9)
        current = current.next

    c = cups_map[1]
    vals = []
    for _ in range(8):
        c = c.next
        vals.append(c.val)
    return "".join(str(v) for v in vals)


@utils.timed
def part2() -> int:

    max_val = 1_000_000

    current = LinkedCup(DATA[0])
    cups_map = {DATA[0]: current}

    c = current
    for value in DATA[1:]:
        c = add_linked_cup(value, cups_map, c)

    for i in range(10, max_val + 1):
        c = add_linked_cup(i, cups_map, c)

    c.next = current

    for i in range(10_000_000):
        move_cups(current, cups_map, max_val)
        current = current.next

    cup_1 = cups_map[1]
    return cup_1.next.val * cup_1.next.next.val


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
