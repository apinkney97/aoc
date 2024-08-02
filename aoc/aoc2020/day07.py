import re
from typing import NamedTuple

from aoc import utils


class ContainedBags(NamedTuple):
    count: int
    name: str


def parse_data(data):
    line_re = re.compile(r"(?P<outer>.*) bags contain (?P<inner>.*)")
    raw_data = utils.parse_data(data, fn=line_re.fullmatch)
    inner_re = re.compile(r"(?P<count>\d+) (?P<name>.*) bags?\.?")
    data = {}
    for line in raw_data:
        outer = line["outer"]
        inner = line["inner"]
        contains = []
        data[outer] = contains
        if inner == "no other bags.":
            continue

        for part in inner.split(", "):
            match = inner_re.fullmatch(part)
            contains.append(ContainedBags(int(match["count"]), match["name"]))

    return data


def part1(data) -> int:
    """
    This sounds like a graph traversal problem:

    The rules specify a directed graph - we must traverse backwards from
    the specified bag and find all reachable nodes. May need to check for cycles?
    """
    inverted = {}  # Maps from bags to those that can contain them
    for src, dests in data.items():
        for dest in dests:
            inverted.setdefault(dest.name, []).append(src)

    queue = ["shiny gold"]
    seen = set()

    while queue:
        bag = queue.pop()
        for neighbour in inverted.get(bag, []):
            if neighbour not in seen:
                queue.append(neighbour)
                seen.add(neighbour)

    return len(seen)


def part2(data) -> int:
    expanded = {}
    to_expand = {"shiny gold"}
    while to_expand:
        passes = 0
        for bag in list(to_expand):
            passes += 1
            if all(cb.name in expanded for cb in data[bag]):
                expanded[bag] = 1 + sum(
                    cb.count * expanded[cb.name] for cb in data[bag]
                )
                to_expand.remove(bag)
                continue

            for contained_bag in data[bag]:
                if contained_bag.name in expanded:
                    continue
                to_expand.add(contained_bag.name)
    return expanded["shiny gold"] - 1
