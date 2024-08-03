import re

CANCEL_RE = re.compile("!.")
GARBAGE_RE = re.compile("<[^>]*>")


def parse_data(data):
    return data[0]


def part1(data):
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


def part2(data):
    data = CANCEL_RE.sub("", data)
    total = 0

    for garbage in GARBAGE_RE.findall(data):
        total += len(garbage) - 2

    return total
