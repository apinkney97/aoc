import utils


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
    for l in layers:
        if get_scanner_pos(layers[l], l) == 0:
            severity += l * layers[l]
    return severity


def part2():
    layers = get_data()
    delay = 0

    while True:
        for l in layers:
            if get_scanner_pos(layers[l], l + delay) == 0:
                break
        else:
            return delay
        delay += 1


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
