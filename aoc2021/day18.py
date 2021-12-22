from __future__ import annotations

import math
from itertools import permutations

import utils

EXAMPLE = True
EXAMPLE = False

# utils.enable_logging()


def load_data():
    data = utils.load_data(18, example=EXAMPLE, fn=eval)

    return data


DATA = load_data()


class SnailPair:
    @classmethod
    def from_list(cls, number_list, parent=None) -> SnailPair:
        pair = cls(0, 0, parent)

        left, right = number_list

        if isinstance(left, list):
            left = cls.from_list(left, parent=pair)
        if isinstance(right, list):
            right = cls.from_list(right, parent=pair)

        pair.left = left
        pair.right = right

        return pair

    def __init__(
        self,
        left: SnailPair | int,
        right: SnailPair | int,
        parent: SnailPair | None = None,
    ):
        if isinstance(left, SnailPair):
            left.parent = self
        if isinstance(right, SnailPair):
            right.parent = self

        self.parent = parent
        self.left = left
        self.right = right

    def __add__(self, other):
        if not isinstance(other, SnailPair):
            return NotImplemented
        new = SnailPair(self, other)
        new.reduce()
        return new

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def reduce(self):
        """
        To reduce a snailfish number, you must repeatedly do the first
        action in this list that applies to the snailfish number:

        If any pair is nested inside four pairs, the leftmost such pair explodes.
        If any regular number is 10 or greater, the leftmost such regular number splits.


        """
        while True:
            utils.log(f"R: {self}")
            for pair in self.traverse_pairs():
                if pair.depth == 4:
                    # To explode a pair, the pair's left value is added to the first
                    # regular number to the left of the exploding pair (if any), and the
                    # pair's right value is added to the first regular number to the
                    # right of the exploding pair (if any). Exploding pairs will always
                    # consist of two regular numbers. Then, the entire exploding pair is
                    # replaced with the regular number 0.
                    utils.log(f"explode {pair}")

                    # first regular number to the left:
                    # traverse upwards until we find we're a right child (or hit the root)
                    # find the rightmost descendent of the left sibling
                    curr = pair
                    while curr.parent is not None:
                        if curr is curr.parent.left:
                            curr = curr.parent
                        else:
                            break
                    if curr.parent is None:
                        utils.log("no left add")
                    else:
                        # we know that curr must be a right child
                        if isinstance(curr.parent.left, int):
                            curr.parent.left += pair.left
                            utils.log(f"left add l {pair.left}")
                        else:
                            curr = curr.parent.left
                            while isinstance(curr.right, SnailPair):
                                curr = curr.right
                            curr.right += pair.left
                            utils.log(f"left add r {pair.left}")

                    # first regular number to the right:
                    # traverse upwards until we find we're a left child (or hit the root)
                    # find the leftmost descendent of the right sibling
                    curr = pair
                    # traverse up
                    while curr.parent is not None:
                        if curr is curr.parent.right:
                            curr = curr.parent
                        else:
                            # utils.log("found left child")
                            break
                    if curr.parent is None:
                        utils.log("no right add")
                    else:
                        # we know that curr must be a left child
                        if isinstance(curr.parent.right, int):
                            curr.parent.right += pair.right
                            utils.log(f"right add r {pair.right}")
                        else:
                            curr = curr.parent.right
                            while isinstance(curr.left, SnailPair):
                                curr = curr.left
                            curr.left += pair.right
                            utils.log(f"right add l {pair.right}")

                    if pair is pair.parent.left:
                        pair.parent.left = 0
                    else:
                        pair.parent.right = 0

                    break
            else:
                # no pair exploded, check for splits

                # To split a regular number, replace it with a pair; the left element
                # of the pair should be the regular number divided by two and rounded
                # down, while the right element of the pair should be the regular
                # number divided by two and rounded up. For example, 10 becomes
                # [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.
                for pair in self.traverse_pairs():
                    if isinstance(pair.left, int) and pair.left >= 10:
                        utils.log(f"left split {pair.left}")
                        pair.left = SnailPair(
                            math.floor(pair.left / 2),
                            math.ceil(pair.left / 2),
                            parent=pair,
                        )
                        break
                    if isinstance(pair.right, int) and pair.right >= 10:
                        utils.log(f"right split {pair.right}")
                        pair.right = SnailPair(
                            math.floor(pair.right / 2),
                            math.ceil(pair.right / 2),
                            parent=pair,
                        )
                        break
                else:
                    # no explodes and no splits; stop checking
                    break

    @property
    def depth(self):
        if self.parent is None:
            return 0
        return self.parent.depth + 1

    def traverse_pairs(self):
        if isinstance(self.left, SnailPair):
            yield from self.left.traverse_pairs()
        yield self
        if isinstance(self.right, SnailPair):
            yield from self.right.traverse_pairs()

    def traverse(self):
        if isinstance(self.left, SnailPair):
            yield from self.left.traverse()
        else:
            yield self.left
        yield self
        if isinstance(self.right, SnailPair):
            yield from self.right.traverse()
        else:
            yield self.right

    @property
    def magnitude(self):
        left = self.left if isinstance(self.left, int) else self.left.magnitude
        right = self.right if isinstance(self.right, int) else self.right.magnitude
        return 3 * left + 2 * right


def part1() -> int:
    initial = SnailPair.from_list(DATA[0])

    for n in DATA[1:]:
        num = SnailPair.from_list(n)
        initial = initial + num

    return initial.magnitude


def part2() -> int:
    max_ = 0
    for a, b in permutations(DATA, 2):
        n1 = SnailPair.from_list(a)
        n2 = SnailPair.from_list(b)
        max_ = max(max_, (n1 + n2).magnitude)
    return max_


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
