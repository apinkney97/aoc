DATA = """
0: 3
1: 2
2: 4
4: 6
6: 5
8: 8
10: 6
12: 4
14: 8
16: 6
18: 8
20: 8
22: 6
24: 8
26: 9
28: 12
30: 8
32: 14
34: 10
36: 12
38: 12
40: 10
42: 12
44: 12
46: 12
48: 12
50: 14
52: 12
54: 14
56: 12
60: 14
62: 12
64: 14
66: 14
68: 14
70: 14
72: 14
74: 14
78: 26
80: 18
82: 17
86: 18
88: 14
96: 18
"""

TEST_DATA = """
0: 3
1: 2
4: 4
6: 4
"""


def get_data():
    data = {}
    for line in DATA.split('\n'):
        line = line.strip()
        if not line:
            continue
        layer, depth = line.split(': ')
        data[int(layer)] = int(depth)
    return data


def get_scanner_pos(depth, t):
    t %= (2 * depth - 2)
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


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
