from __future__ import annotations

type Data = list[int]


class LinkedCup:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self._next: LinkedCup | None = None

    @property
    def next(self) -> LinkedCup:
        if self._next is None:
            raise Exception("No next value")
        return self._next

    @next.setter
    def next(self, value: LinkedCup) -> None:
        self._next = value

    def __repr__(self) -> str:
        return f"Cup({self.val})"


def parse_data(data: list[str]) -> Data:
    return [int(n) for n in data[0]]


def get_dest(n: int, max_item: int) -> int:
    n = (n - 1) % max_item
    if n == 0:
        n = max_item
    return n


def add_linked_cup(
    value: int, cups_map: dict[int, LinkedCup], prev: LinkedCup
) -> LinkedCup:
    new_cup = LinkedCup(value)
    cups_map[value] = new_cup
    prev.next = new_cup
    return new_cup


def move_cups(current: LinkedCup, cups_map: dict[int, LinkedCup], max_val: int) -> None:
    removed = [current.next, current.next.next, current.next.next.next]
    removed_vals = {r.val for r in removed}

    current.next = removed[-1].next

    dest_n = get_dest(current.val, max_val)

    while dest_n in removed_vals:
        dest_n = get_dest(dest_n, max_val)

    dest = cups_map[dest_n]

    removed[-1].next = dest.next
    dest.next = removed[0]


def part1(data: Data) -> str:
    current = LinkedCup(data[0])
    cups_map = {data[0]: current}

    c = current
    for value in data[1:]:
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


def part2(data: Data) -> int:
    max_val = 1_000_000

    current = LinkedCup(data[0])
    cups_map = {data[0]: current}

    c = current
    for value in data[1:]:
        c = add_linked_cup(value, cups_map, c)

    for i in range(10, max_val + 1):
        c = add_linked_cup(i, cups_map, c)

    c.next = current

    for i in range(10_000_000):
        move_cups(current, cups_map, max_val)
        current = current.next

    cup_1 = cups_map[1]
    return cup_1.next.val * cup_1.next.next.val
