from aoc import utils


def get_data():
    data = {}
    for line in utils.load_data(2017, 13):
        layer, depth = line.split(": ")
        data[int(layer)] = int(depth)
    return data


def get_scanner_pos(depth, t):
    t %= 2 * depth - 2
    if t < depth:
        return t
    return depth - (t % depth) - 2


def part1():
    layers = get_data()
    severity = 0
    for layer in layers:
        if get_scanner_pos(layers[layer], layer) == 0:
            severity += layer * layers[layer]
    return severity


def part2():
    layers = get_data()
    delay = 0

    while True:
        for layer in layers:
            if get_scanner_pos(layers[layer], layer + delay) == 0:
                break
        else:
            return delay
        delay += 1


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
