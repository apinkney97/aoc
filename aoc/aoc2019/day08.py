from collections import Counter
from typing import List, Optional

from more_itertools import chunked

from aoc import utils


def part1(data):
    width = 25
    height = 6
    pixels_per_layer = width * height
    min_zero_layer = None

    for layer in chunked(data[0], pixels_per_layer):
        layer_counter = Counter(layer)
        if min_zero_layer is None or layer_counter["0"] < min_zero_layer["0"]:
            min_zero_layer = layer_counter

    return min_zero_layer["1"] * min_zero_layer["2"]


def part2(data):
    width = 25
    height = 6
    pixels_per_layer = width * height

    output_map = {"0": utils.BACKGROUND_BLOCK, "1": utils.FOREGROUND_BLOCK}

    output: List[Optional[str]] = [None] * pixels_per_layer
    for layer in chunked(data[0], pixels_per_layer):
        for i, value in enumerate(layer):
            if output[i] is None and value != "2":
                output[i] = output_map[value]

    for row in chunked(output, width):
        print("".join(row))
