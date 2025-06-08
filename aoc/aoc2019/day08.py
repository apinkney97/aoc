from collections import Counter

from more_itertools import chunked

from aoc import utils

type Data = list[str]


def part1(data: Data) -> int:
    width = 25
    height = 6
    pixels_per_layer = width * height
    layers = []

    for layer in chunked(data[0], pixels_per_layer):
        layer_counter = Counter(layer)
        layers.append(layer_counter)

    min_zero_layer = min(layers, key=lambda x: x["0"])
    return min_zero_layer["1"] * min_zero_layer["2"]


def part2(data: Data) -> None:
    width = 25
    height = 6
    pixels_per_layer = width * height

    output_map = {"0": utils.BACKGROUND_BLOCK, "1": utils.FOREGROUND_BLOCK}

    output = ["X"] * pixels_per_layer
    for layer in chunked(data[0], pixels_per_layer):
        for i, value in enumerate(layer):
            if output[i] == "X" and value != "2":
                output[i] = output_map[value]

    for row in chunked(output, width):
        print("".join(row))
