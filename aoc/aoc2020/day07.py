import re
from typing import NamedTuple

type Data = dict[str, list[ContainedBags]]


class ContainedBags(NamedTuple):
    bag_count: int
    name: str


def parse_data(data: list[str]) -> Data:
    line_re = re.compile(r"(?P<outer>.*) bags contain (?P<inner>.*)")
    inner_re = re.compile(r"(?P<count>\d+) (?P<name>.*) bags?\.?")

    parsed_data = {}
    for line in data:
        line_match = line_re.fullmatch(line)
        assert line_match is not None
        outer = line_match["outer"]
        inner = line_match["inner"]
        contains: list[ContainedBags] = []
        parsed_data[outer] = contains
        if inner == "no other bags.":
            continue

        for part in inner.split(", "):
            match = inner_re.fullmatch(part)
            assert match is not None
            contains.append(ContainedBags(int(match["count"]), match["name"]))

    return parsed_data


def part1(data: Data) -> int:
    """
    This sounds like a graph traversal problem:

    The rules specify a directed graph - we must traverse backwards from
    the specified bag and find all reachable nodes. May need to check for cycles?
    """
    inverted: dict[str, list[str]] = {}  # Maps from bags to those that can contain them
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


def part2(data: Data) -> int:
    expanded: dict[str, int] = {}
    to_expand = {"shiny gold"}
    while to_expand:
        passes = 0
        for bag in list(to_expand):
            passes += 1
            if all(cb.name in expanded for cb in data[bag]):
                expanded[bag] = 1 + sum(
                    cb.bag_count * expanded[cb.name] for cb in data[bag]
                )
                to_expand.remove(bag)
                continue

            for contained_bag in data[bag]:
                if contained_bag.name in expanded:
                    continue
                to_expand.add(contained_bag.name)
    return expanded["shiny gold"] - 1
