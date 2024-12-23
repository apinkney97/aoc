from networkx import Graph, find_cliques


def parse_data(data):
    pairs = []
    for line in data:
        pairs.append(tuple(line.split("-")))
    return pairs


def find_triples(edges: dict[str, set[str]]) -> list[tuple[str, str, str]]:
    seen = set()
    for n1 in edges:
        for n2 in edges[n1]:
            for n3 in edges[n2]:
                if n1 in edges[n3]:
                    triple = sorted({n1, n2, n3})
                    if len(triple) == 3:
                        seen.add(tuple(triple))
    return sorted(seen)


def part1(data) -> int:
    edges = {}
    for a, b in data:
        edges.setdefault(a, set()).add(b)
        edges.setdefault(b, set()).add(a)

    result = 0
    for triple in find_triples(edges):
        if any(x.startswith("t") for x in triple):
            result += 1
    return result


def part2(data) -> str:
    graph = Graph()
    for a, b in data:
        graph.add_edge(a, b)

    longest = []
    for clique in find_cliques(graph):
        if len(clique) > len(longest):
            longest = clique

    return ",".join(sorted(longest))
