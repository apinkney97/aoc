import json
from functools import singledispatch


def parse_data(data):
    return json.loads(data[0])


@singledispatch
def totalise(json_item):
    return 0


@totalise.register(list)
def _(list_):
    return sum(totalise(i) for i in list_)


@totalise.register(dict)
def _(dict_):
    return sum(totalise(val) for val in dict_.values())


@totalise.register(int)
@totalise.register(float)
def _(num):
    return num


@singledispatch
def totalise_no_red(json_item):
    return 0


@totalise_no_red.register(list)
def _(list_):
    return sum(totalise_no_red(i) for i in list_)


@totalise_no_red.register(dict)
def _(dict_):
    if any(val == "red" for val in dict_.values()):
        return 0
    return sum(totalise_no_red(val) for val in dict_.values())


@totalise_no_red.register(int)
@totalise_no_red.register(float)
def _(num):
    return num


def part1(data) -> int:
    return totalise(data)


def part2(data) -> int:
    return totalise_no_red(data)
