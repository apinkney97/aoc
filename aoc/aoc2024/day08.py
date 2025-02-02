import itertools

from aoc.utils.coords import Coord2D

type Data = tuple[dict[str, list[Coord2D]], int, int]


def parse_data(data: list[str]) -> Data:
    nodes: dict[str, list[Coord2D]] = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != ".":
                nodes.setdefault(c, []).append(Coord2D(x, y))

    width = len(data[0])
    height = len(data)
    return nodes, width, height


def find_antinodes(nodes: list[Coord2D], max_x: int, max_y: int) -> set[Coord2D]:
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


def find_all_antinodes(nodes: list[Coord2D], max_x: int, max_y: int) -> set[Coord2D]:
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


def part1(data: Data) -> int:
    nodes, width, height = data
    all_antinodes = set()
    for node_name, coords in nodes.items():
        all_antinodes.update(find_antinodes(coords, width, height))

    return len(all_antinodes)


def part2(data: Data) -> int:
    nodes, width, height = data
    all_antinodes = set()
    for node_name, coords in nodes.items():
        all_antinodes.update(find_all_antinodes(coords, width, height))

    return len(all_antinodes)
