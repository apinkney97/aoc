import json
from functools import singledispatch

type Data = int | list[Data] | dict[str, Data]


def parse_data(data: list[str]) -> Data:
    return json.loads(data[0])  # type: ignore[no-any-return]


@singledispatch
def totalise(val: Data) -> int:
    return 0


@totalise.register(list)
def _(val: list[Data]) -> int:
    return sum(totalise(i) for i in val)


@totalise.register(dict)
def _(val: dict[str, Data]) -> int:
    return sum(totalise(val) for val in val.values())


@totalise.register
def _(val: int) -> int:
    return val


@singledispatch
def totalise_no_red(val: Data) -> int:
    return 0


@totalise_no_red.register(list)
def _(val: list[Data]) -> int:
    return sum(totalise_no_red(i) for i in val)


@totalise_no_red.register(dict)
def _(val: dict[str, Data]) -> int:
    if any(isinstance(v, str) and v == "red" for v in val.values()):
        return 0
    return sum(totalise_no_red(v) for v in val.values())


@totalise_no_red.register
def _(val: int) -> int:
    return val


def part1(data: Data) -> int:
    return totalise(data)


def part2(data: Data) -> int:
    return totalise_no_red(data)
