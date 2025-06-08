import typing
from collections import defaultdict
from collections.abc import Callable

type Data = list[str]

CMP_FNS: dict[str, Callable[[int, int], bool]] = {
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
}

GLOBAL_MAX = 0


def part1(data: Data) -> int:
    global GLOBAL_MAX
    cells: typing.DefaultDict[str, int] = defaultdict(int)
    for line in data:
        this_name, action, val, _, that, cmp_op, cmp_val = line.split(" ")
        if CMP_FNS[cmp_op](cells[that], int(cmp_val)):
            if action == "inc":
                cells[this_name] += int(val)
            elif action == "dec":
                cells[this_name] -= int(val)

            if cells[this_name] > GLOBAL_MAX:
                GLOBAL_MAX = cells[this_name]

    return max(cells.values())


def part2(data: Data) -> int:
    return GLOBAL_MAX
