import typing

import utils

# EXAMPLE = True
EXAMPLE = False


class Ingredient(typing.NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def load_data():
    if EXAMPLE:
        return [
            Ingredient(capacity=-1, durability=-2, flavor=6, texture=3, calories=8),
            Ingredient(capacity=2, durability=3, flavor=-2, texture=-1, calories=3),
        ]

    return [
        Ingredient(capacity=2, durability=0, flavor=-2, texture=0, calories=3),
        Ingredient(capacity=0, durability=5, flavor=-3, texture=0, calories=3),
        Ingredient(capacity=0, durability=0, flavor=5, texture=-1, calories=8),
        Ingredient(capacity=0, durability=-1, flavor=0, texture=5, calories=8),
    ]


DATA = load_data()


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


def part1(calories=None) -> int:
    best = 0
    if len(DATA) == 2:
        for i in range(101):
            j = 100 - i
            score, cals = bake(DATA, i, j)
            if calories is None or cals == calories:
                best = max(best, score)

    else:
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - (i + j)):
                    h = 100 - (i + j + k)
                    score, cals = bake(DATA, i, j, k, h)
                    if calories is None or cals == calories:
                        best = max(best, score)

    return best


def part2() -> int:
    return part1(calories=500)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
