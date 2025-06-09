import typing
from collections.abc import Callable

from aoc import config, utils


class Throw(typing.NamedTuple):
    item: int
    to: int


class Monkey:
    def __init__(
        self,
        number: int,
        items: list[int],
        op: Callable[[int], int],
        divisor: int,
        if_true: int,
        if_false: int,
    ) -> None:
        self.number = number
        self.items = items
        self.op = op
        self.divisor = divisor
        self.if_true = if_true
        self.if_false = if_false

        self.inspect_count = 0

    def take_turn(self, modulo: int = 0) -> list[Throw]:
        throws = []
        for item in self.items:
            item = self.op(item)
            self.inspect_count += 1

            if modulo:
                item = item % modulo
            else:
                item = item // 3

            to = self.if_true if item % self.divisor == 0 else self.if_false
            throws.append(Throw(item=item, to=to))
        self.items = []
        return throws


def get_monkeys(example: bool = False) -> list[Monkey]:
    if example:
        return [
            Monkey(
                number=0,
                items=[79, 98],
                op=lambda old: old * 19,
                divisor=23,
                if_true=2,
                if_false=3,
            ),
            Monkey(
                number=1,
                items=[54, 65, 75, 74],
                op=lambda old: old + 6,
                divisor=19,
                if_true=2,
                if_false=0,
            ),
            Monkey(
                number=2,
                items=[79, 60, 97],
                op=lambda old: old * old,
                divisor=13,
                if_true=1,
                if_false=3,
            ),
            Monkey(
                number=3,
                items=[74],
                op=lambda old: old + 3,
                divisor=17,
                if_true=0,
                if_false=1,
            ),
        ]
    else:
        return [
            Monkey(
                number=0,
                items=[61],
                op=lambda old: old * 11,
                divisor=5,
                if_true=7,
                if_false=4,
            ),
            Monkey(
                number=1,
                items=[76, 92, 53, 93, 79, 86, 81],
                op=lambda old: old + 4,
                divisor=2,
                if_true=2,
                if_false=6,
            ),
            Monkey(
                number=2,
                items=[91, 99],
                op=lambda old: old * 19,
                divisor=13,
                if_true=5,
                if_false=0,
            ),
            Monkey(
                number=3,
                items=[58, 67, 66],
                op=lambda old: old * old,
                divisor=7,
                if_true=6,
                if_false=1,
            ),
            Monkey(
                number=4,
                items=[94, 54, 62, 73],
                op=lambda old: old + 1,
                divisor=19,
                if_true=3,
                if_false=7,
            ),
            Monkey(
                number=5,
                items=[59, 95, 51, 58, 58],
                op=lambda old: old + 3,
                divisor=11,
                if_true=0,
                if_false=4,
            ),
            Monkey(
                number=6,
                items=[87, 69, 92, 56, 91, 93, 88, 73],
                op=lambda old: old + 8,
                divisor=3,
                if_true=5,
                if_false=2,
            ),
            Monkey(
                number=7,
                items=[71, 57, 86, 67, 96, 95],
                op=lambda old: old + 7,
                divisor=17,
                if_true=3,
                if_false=1,
            ),
        ]


def part1(data: typing.Any) -> int:
    monkeys = get_monkeys(config.EXAMPLE)
    for _ in range(20):
        for monkey in monkeys:
            throws = monkey.take_turn()
            for throw in throws:
                monkeys[throw.to].items.append(throw.item)

    return utils.product(sorted([m.inspect_count for m in monkeys])[-2:])


def part2(data: typing.Any) -> int:
    monkeys = get_monkeys(config.EXAMPLE)
    modulo = utils.product([m.divisor for m in monkeys])
    for _ in range(10000):
        for monkey in monkeys:
            throws = monkey.take_turn(modulo=modulo)
            for throw in throws:
                monkeys[throw.to].items.append(throw.item)

    return utils.product(sorted([m.inspect_count for m in monkeys])[-2:])
