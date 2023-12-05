from collections import Counter
from typing import List, Optional

from more_itertools import chunked

import utils


def part1():
    data = utils.load_data(2019, 8)[0]
    width = 25
    height = 6
    pixels_per_layer = width * height
    min_zero_layer = None

    for layer in chunked(data, pixels_per_layer):
        layer_counter = Counter(layer)
        if min_zero_layer is None or layer_counter["0"] < min_zero_layer["0"]:
            min_zero_layer = layer_counter

    return min_zero_layer["1"] * min_zero_layer["2"]


def part2():
    data = utils.load_data(2019, 8)[0]
    width = 25
    height = 6
    pixels_per_layer = width * height

    output_map = {"0": " ", "1": "#"}

    output: List[Optional[str]] = [None] * pixels_per_layer
    for layer in chunked(data, pixels_per_layer):
        for i, value in enumerate(layer):
            if output[i] is None and value != "2":
                output[i] = output_map[value]

    for row in chunked(output, width):
        print("".join(row))


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
