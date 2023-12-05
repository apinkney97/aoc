import re

import utils

CANCEL_RE = re.compile("!.")
GARBAGE_RE = re.compile("<[^>]*>")


def get_data():
    return utils.load_data(2017,9)[0]


def part1():
    data = get_data()
    data = CANCEL_RE.sub("", data)
    data = GARBAGE_RE.sub("", data)

    depth = 0
    total = 0

    for c in data:
        if c == "{":
            depth += 1
        elif c == "}":
            total += depth
            depth -= 1

    return total


def part2():
    data = get_data()
    data = CANCEL_RE.sub("", data)
    total = 0

    for garbage in GARBAGE_RE.findall(data):
        total += len(garbage) - 2

    return total


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
