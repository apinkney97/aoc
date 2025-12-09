from itertools import combinations

from networkx import Graph, connected_components, has_path

from aoc import config
from aoc.utils import PQ, Coord3D, product

type Data = list[Coord3D]


def parse_data(data: list[str]) -> Data:
    coords = []
    for line in data:
        x, y, z = line.split(",")
        coords.append(Coord3D(int(x), int(y), int(z)))
    return coords


def part1(data: Data) -> int:
    limit = 10 if config.EXAMPLE else 1000

    graph: Graph[int] = Graph()
    graph.add_nodes_from(range(len(data)))

    queue: PQ[tuple[int, int]] = PQ()
    for (i1, c1), (i2, c2) in combinations(enumerate(data), 2):
        queue.add_item(item=(i1, i2), priority=(c2 - c1).magnitude)

    added = 0
    while queue and added < limit:
        added += 1
        i1, i2 = queue.pop_item()
        if has_path(graph, i1, i2):
            continue
        graph.add_edge(i1, i2)

    ccs = connected_components(graph)
    top_three = sorted(ccs, key=len)[-3:]

    return product(len(cc) for cc in top_three)


def part2(data: Data) -> int:
    result = 0
    graph: Graph[int] = Graph()
    graph.add_nodes_from(range(len(data)))

    queue: PQ[tuple[int, int]] = PQ()
    for (i1, c1), (i2, c2) in combinations(enumerate(data), 2):
        queue.add_item(item=(i1, i2), priority=(c2 - c1).magnitude)

    while queue:
        i1, i2 = queue.pop_item()
        if has_path(graph, i1, i2):
            continue
        graph.add_edge(i1, i2)
        if len(list(connected_components(graph))) == 1:
            result = data[i1].x * data[i2].x
            break

    return result
