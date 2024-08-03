def parse_data(data):
    parsed_data = {}
    for line in data:
        layer, depth = line.split(": ")
        parsed_data[int(layer)] = int(depth)
    return parsed_data


def get_scanner_pos(depth, t):
    t %= 2 * depth - 2
    if t < depth:
        return t
    return depth - (t % depth) - 2


def part1(data):
    layers = data
    severity = 0
    for layer in layers:
        if get_scanner_pos(layers[layer], layer) == 0:
            severity += layer * layers[layer]
    return severity


def part2(data):
    layers = data
    delay = 0

    while True:
        for layer in layers:
            if get_scanner_pos(layers[layer], layer + delay) == 0:
                break
        else:
            return delay
        delay += 1
