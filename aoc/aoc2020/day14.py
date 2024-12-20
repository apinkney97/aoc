import re
from itertools import combinations

from aoc import utils


def parse_data(data):
    data = utils.parse_data(data, fn=lambda s: s.partition(" = "))
    mem_re = re.compile(r"mem\[(?P<loc>\d+)]")

    parsed_data = []
    for command, _, val in data:
        if command == "mask":
            parsed_data.append(val)
        else:
            match = mem_re.fullmatch(command)
            parsed_data.append((int(match["loc"]), int(val)))
    return parsed_data


class ValueMask:
    def __init__(self, mask: str):
        self.mask = mask

        self._and_mask = int(mask.replace("X", "1"), 2)
        self._or_mask = int(mask.replace("X", "0"), 2)

    def __and__(self, other):
        return self._and_mask & other

    def __or__(self, other):
        return self._or_mask | other

    def __rand__(self, other):
        return self & other

    def __ror__(self, other):
        return self | other

    def apply(self, other):
        return self & (self | other)

    def __repr__(self):
        return f"Mask({self.mask!r})"


class AddressMask:
    # bitmask is bitwise OR'd with the address
    # any X takes on all values of 0 or 1
    def __init__(self, mask: str):
        self.mask = mask

        self._or_mask = int(mask.replace("X", "0"), 2)

        self.x_indexes = []
        for i, c in enumerate(mask):
            if c == "X":
                self.x_indexes.append(i)

    def get_addresses(self, address: int):
        base_address = address | self._or_mask

        for i in range(len(self.x_indexes) + 1):
            for comb in combinations(self.x_indexes, r=i):
                mask = ["X"] * 36
                for bit in self.x_indexes:
                    mask[bit] = "1" if bit in comb else "0"

                m = ValueMask("".join(mask))
                yield m.apply(base_address)


def part1(data) -> int:
    mem = {}
    mask = None
    for command in data:
        if isinstance(command, str):
            mask = ValueMask(command)
        else:
            loc, val = command
            mem[loc] = mask.apply(val)

    return sum(mem.values())


def part2(data) -> int:
    mem = {}
    mask = None
    for command in data:
        if isinstance(command, str):
            mask = AddressMask(command)
        else:
            loc, val = command
            for address in mask.get_addresses(loc):
                mem[address] = val

    return sum(mem.values())
