import itertools

from aoc.utils.coords import Coord


def parse_data(data):
    nodes = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != ".":
                nodes.setdefault(c, []).append(Coord(x, y))

    width = len(data[0])
    height = len(data)
    return nodes, width, height


def find_antinodes(nodes: list[Coord], max_x: int, max_y: int) -> set[Coord]:
    antinodes = set()

    for node_1, node_2 in itertools.combinations(nodes, 2):
        diff = node_1 - node_2

        antinode_1 = node_1 + diff
        if 0 <= antinode_1.x < max_x and 0 <= antinode_1.y < max_y:
            antinodes.add(antinode_1)

        antinode_2 = node_2 - diff
        if 0 <= antinode_2.x < max_x and 0 <= antinode_2.y < max_y:
            antinodes.add(antinode_2)

    return antinodes


def find_all_antinodes(nodes: list[Coord], max_x: int, max_y: int) -> set[Coord]:
    antinodes = set()

    for node_1, node_2 in itertools.combinations(nodes, 2):
        diff = node_1 - node_2

        antinode = node_1
        while 0 <= antinode.x < max_x and 0 <= antinode.y < max_y:
            antinodes.add(antinode)
            antinode += diff

        antinode = node_2
        while 0 <= antinode.x < max_x and 0 <= antinode.y < max_y:
            antinodes.add(antinode)
            antinode -= diff

    return antinodes


def part1(data) -> int:
    nodes, width, height = data
    all_antinodes = set()
    for node_name, coords in nodes.items():
        all_antinodes.update(find_antinodes(coords, width, height))

    return len(all_antinodes)


def part2(data) -> int:
    nodes, width, height = data
    all_antinodes = set()
    for node_name, coords in nodes.items():
        all_antinodes.update(find_all_antinodes(coords, width, height))

    return len(all_antinodes)
