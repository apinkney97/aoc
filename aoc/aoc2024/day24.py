from __future__ import annotations

import itertools

from aoc import utils

GATES: dict[str, Gate] = {}


class Gate:
    _left = "None"
    _right = "None"

    def value(self) -> int:
        raise NotImplementedError


class Wire(Gate):
    def __init__(self, value: int):
        self._value = value

    def value(self) -> int:
        return self._value


class OR(Gate):
    def __init__(self, left: str, right: str):
        self._left = left
        self._right = right

    def value(self) -> int:
        left = GATES[self._left].value()
        right = GATES[self._right].value()
        return left or right


class AND(Gate):
    def __init__(self, left: str, right: str):
        self._left = left
        self._right = right

    def value(self) -> int:
        left = GATES[self._left].value()
        right = GATES[self._right].value()
        return left and right


class XOR(Gate):
    def __init__(self, left: str, right: str):
        self._left = left
        self._right = right

    def value(self) -> int:
        left = GATES[self._left].value()
        right = GATES[self._right].value()
        return int((left or right) and not (left and right))


type Data = list[tuple[str, Gate]]


def parse_data(data: list[str]) -> Data:
    wires, gates = utils.split_by_blank_lines(data)
    for wire in wires:
        name, value = wire.split(": ")
        GATES[name] = Wire(int(value))
    z_gates = []
    for gate in gates:
        left, op, right, _, name = gate.split()
        g = globals()[op](left, right)
        GATES[name] = g
        if name.startswith("z"):
            z_gates.append((name, g))
    return sorted(z_gates, reverse=True)


def part1(data: Data) -> int:
    result = 0
    for name, gate in data:
        result <<= 1
        result += gate.value()
    return result


def to_dot() -> None:
    print("digraph g {")
    for name, gate in GATES.items():
        gate_type = type(gate).__name__
        color = {"OR": "yellow", "AND": "green", "XOR": "lightblue", "Wire": "pink"}[
            gate_type
        ]
        if name.startswith("z"):
            color = "purple"
        shape = {"OR": "circle", "AND": "square", "XOR": "triangle", "Wire": "ellipse"}[
            gate_type
        ]
        print(
            rf'    {name}[label="{name}\n{gate_type}", style=filled, fillcolor={color}, shape={shape}];'
        )
        if not name.startswith(("x", "y")):
            print(f"    {gate._left} -> {name};")
            print(f"    {gate._right} -> {name};")
    print("}")


def part2(data: Data) -> str:
    # I did this by eyeballing the output graph rendered with graphviz, and filling in the pairs to swap below.
    swaps = [  # type: ignore[var-annotated]
        # ("xxx", "yyy"),
        # ("aaa", "bbb"),
        # ("ppp", "qqq"),
        # ("mmm", "nnn"),
    ]
    for a, b in swaps:
        GATES[a], GATES[b] = GATES[b], GATES[a]

    # to_dot()

    return ",".join(sorted(itertools.chain(*swaps)))
