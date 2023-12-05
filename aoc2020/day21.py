import operator
from functools import reduce

import utils


def load_data():
    data = utils.load_data(2020, 21, example=False)

    parsed = []

    for line in data:
        ingredients, allergens = line.split(" (contains ")
        ingredients = set(ingredients.split())
        allergens = set(allergens[:-1].split(", "))
        parsed.append((ingredients, allergens))

    return parsed


DATA = load_data()


def part1() -> int:
    # Each allergen is found in exactly one ingredient.

    allergen_to_recipes = {}
    all_ingredients = set()

    for recipe, allergens in DATA:
        all_ingredients.update(recipe)
        for allergen in allergens:
            allergen_to_recipes.setdefault(allergen, []).append(recipe)

    allergen_to_potential_ingredients = {
        allergen: reduce(operator.and_, allergen_to_recipes[allergen])
        for allergen in allergen_to_recipes
    }

    confirmed = {}

    changed = True
    while changed:
        changed = False
        for allergen, ingredients in allergen_to_potential_ingredients.items():
            if len(ingredients) == 1:
                ingredient = ingredients.pop()
                confirmed[allergen] = ingredient

                allergen_to_potential_ingredients.pop(allergen)
                for ings in allergen_to_potential_ingredients.values():
                    ings.discard(ingredient)

                changed = True
                break

    dangerous_list = []
    for allergen in sorted(confirmed):
        dangerous_list.append(confirmed[allergen])

    print("Part 2:", ",".join(dangerous_list))

    no_allergens = all_ingredients - set(confirmed.values())

    count = 0
    for ingredient in no_allergens:
        for recipe, _ in DATA:
            if ingredient in recipe:
                count += 1

    return count


def main() -> None:
    print(f"Part 1: {part1()}")


if __name__ == "__main__":
    main()
