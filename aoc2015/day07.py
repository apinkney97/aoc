import re
from typing import Dict, List, NamedTuple

import utils

INSTRUCTIONS_RE = re.compile(r"(?P<input>.*) -> (?P<output>[a-z]+)")


class Gate(NamedTuple):
    type: str
    args: List[str]


def _load_data() -> Dict[str, Gate]:
    raw_data = utils.load_data(7, fn=INSTRUCTIONS_RE.fullmatch)

    data: Dict[str, Gate] = {}
    for item in raw_data:
        raw_input = item["input"]
        parts = raw_input.split()
        if len(parts) == 1:
            gate = Gate(type="LITERAL", args=[parts[0]])
        elif len(parts) == 2:
            gate = Gate(type=parts[0], args=[parts[1]])
        elif len(parts) == 3:
            gate = Gate(type=parts[1], args=[parts[0], parts[2]])
        else:
            raise Exception(f"Bad item: {item}")

        data[item["output"]] = gate
    return data


DATA = _load_data()


def _get_value(values: Dict[str, int], arg: str):
    if arg.isdigit():
        return int(arg)
    return values.get(arg)


def evaluate(data):
    values = {}
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


def part1() -> int:
    values = evaluate(dict(DATA))
    return values["a"]


def part2() -> int:
    values = evaluate(dict(DATA))
    data = dict(DATA)
    data["b"] = Gate(type="LITERAL", args=[str(values["a"])])
    return evaluate(data)["a"]


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
