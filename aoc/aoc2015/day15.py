import re
import typing

from aoc import utils


class Ingredient(typing.NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse_data(data):
    # Example:
    # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    ingredient_re = re.compile(
        r".*: \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)"
    )
    data = utils.parse_data(data, fn=ingredient_re.fullmatch)

    return [
        Ingredient(
            capacity=int(match.group(1)),
            durability=int(match.group(2)),
            flavor=int(match.group(3)),
            texture=int(match.group(4)),
            calories=int(match.group(5)),
        )
        for match in data
    ]


def bake(ingredients, *quantity):
    zipped = list(zip(ingredients, quantity))

    score = utils.product(
        [
            max(0, sum(i.capacity * q for i, q in zipped)),
            max(0, sum(i.durability * q for i, q in zipped)),
            max(0, sum(i.flavor * q for i, q in zipped)),
            max(0, sum(i.texture * q for i, q in zipped)),
        ]
    )

    calories = sum(i.calories * q for i, q in zipped)

    return score, calories


def part1(data, calories=None) -> int:
    best = 0
    if len(data) == 2:
        for i in range(101):
            j = 100 - i
            score, cals = bake(data, i, j)
            if calories is None or cals == calories:
                best = max(best, score)

    else:
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - (i + j)):
                    h = 100 - (i + j + k)
                    score, cals = bake(data, i, j, k, h)
                    if calories is None or cals == calories:
                        best = max(best, score)

    return best


def part2(data) -> int:
    return part1(data, calories=500)
