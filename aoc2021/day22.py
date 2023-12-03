import re
from itertools import product
from typing import NamedTuple

import utils

EXAMPLE = True
EXAMPLE = False


class Action(NamedTuple):
    action: str
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int


def load_data():
    # on x=-34154..-5635,y=-24345..11649,z=71769..88510
    r = re.compile(
        r"""
        (?P<action>on|off)\s
        x=(?P<x1>-?\d+)\.\.(?P<x2>-?\d+),
        y=(?P<y1>-?\d+)\.\.(?P<y2>-?\d+),
        z=(?P<z1>-?\d+)\.\.(?P<z2>-?\d+)
        """,
        re.VERBOSE,
    )
    data = utils.load_data(22, example=EXAMPLE, fn=r.fullmatch)

    return [
        Action(
            action=d.group("action"),
            x1=int(d.group("x1")),
            x2=int(d.group("x2")),
            y1=int(d.group("y1")),
            y2=int(d.group("y2")),
            z1=int(d.group("z1")),
            z2=int(d.group("z2")),
        )
        for d in data
    ]


DATA = load_data()


def part1() -> int:
    g = utils.Grid3D(default_val=0)
    for action in DATA:
        if any(
            abs(c) > 50
            for c in (action.x1, action.x2, action.y1, action.y2, action.z1, action.z2)
        ):
            continue
        value = 0 if action.action == "off" else 1
        for coord in product(
            range(action.x1, action.x2 + 1),
            range(action.y1, action.y2 + 1),
            range(action.z1, action.z2 + 1),
        ):
            g[coord] = value
    return len(g)


def part2() -> int:
    g = utils.Grid3D(default_val=0)
    for action in DATA:
        value = 0 if action.action == "off" else 1
        for coord in product(
            range(action.x1, action.x2 + 1),
            range(action.y1, action.y2 + 1),
            range(action.z1, action.z2 + 1),
        ):
            g[coord] = value
    return len(g)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
