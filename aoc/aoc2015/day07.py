import re
from typing import Dict, List, NamedTuple

INSTRUCTIONS_RE = re.compile(r"(?P<input>.*) -> (?P<output>[a-z]+)")

type Data = dict[str, Gate]


class Gate(NamedTuple):
    type: str
    args: List[str]


def parse_data(data: list[str]) -> Data:
    matches = [INSTRUCTIONS_RE.fullmatch(line) for line in data]

    parsed_data: Data = {}
    for match in matches:
        assert match is not None
        raw_input = match["input"]
        parts = raw_input.split()
        if len(parts) == 1:
            gate = Gate(type="LITERAL", args=[parts[0]])
        elif len(parts) == 2:
            gate = Gate(type=parts[0], args=[parts[1]])
        elif len(parts) == 3:
            gate = Gate(type=parts[1], args=[parts[0], parts[2]])
        else:
            raise Exception(f"Bad item: {match}")

        parsed_data[match["output"]] = gate
    return parsed_data


def _get_value(values: Dict[str, int], arg: str) -> int | None:
    if arg.isdigit():
        return int(arg)
    return values.get(arg)


def evaluate(data: Data) -> dict[str, int]:
    data = dict(data)
    values: dict[str, int] = {}
    passes = 0
    while data:
        passes += 1
        # print(f"Pass {passes}")
        for wire in list(data):
            gate = data[wire]

            arg1 = _get_value(values, gate.args[0])
            if arg1 is None:
                continue

            if gate.type == "LITERAL":
                values[wire] = arg1
                data.pop(wire)
                continue

            if gate.type == "NOT":
                values[wire] = (~arg1) & 0xFFFF
                data.pop(wire)
                continue

            if gate.type not in {"AND", "OR", "LSHIFT", "RSHIFT"}:
                raise Exception(f"Don't know how to handle {gate.type}")

            arg2 = _get_value(values, gate.args[1])

            if arg2 is None:
                continue

            if gate.type == "AND":
                values[wire] = arg1 & arg2
            elif gate.type == "OR":
                values[wire] = arg1 | arg2
            elif gate.type == "LSHIFT":
                values[wire] = (arg1 << arg2) & 0xFFFF
            elif gate.type == "RSHIFT":
                values[wire] = (arg1 >> arg2) & 0xFFFF
            else:
                raise Exception(f"Don't know how to handle {gate.type}")

            data.pop(wire)
    return values


def part1(data: Data) -> int:
    values = evaluate(data)
    return values["a"]


def part2(data: Data) -> int:
    values = evaluate(data)
    data = dict(data)
    data["b"] = Gate(type="LITERAL", args=[str(values["a"])])
    return evaluate(data)["a"]
