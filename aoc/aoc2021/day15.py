from aoc import utils


def parse_data(data):
    data = utils.parse_data(data, fn=lambda line: [int(i) for i in line])

    return data


Coord = tuple[int, int]


def part1(data) -> int:
    edges: dict[Coord, dict[Coord, int]] = {}

    size = len(data)
    if size != len(data[0]):
        raise Exception("Not a square...")
    for y in range(size):
        for x in range(size):
            for nx, ny in utils.neighbours((x, y), include_diagonals=False):
                if not ((0 <= nx < size) and (0 <= ny < size)):
                    continue
                edges.setdefault((x, y), {})[(nx, ny)] = data[nx][ny]

    return dijkstra(edges, (0, 0), (size - 1, size - 1))


def dijkstra(edges: dict[Coord, dict[Coord, int]], start: Coord, end: Coord) -> int:
    unvisited: set[Coord] = set(edges.keys())
    distances: dict[Coord, int] = {node: float("inf") for node in unvisited}
    distances[start] = 0

    pq = utils.PQ()
    for coord, distance in distances.items():
        pq.add_item(coord, distance)

    current = None
    while current != end:
        current = pq.pop_item()
        for neighbour, cost in edges[current].items():
            new_cost = distances[current] + cost
            if neighbour in unvisited and distances[neighbour] > new_cost:
                distances[neighbour] = new_cost
                pq.add_item(neighbour, new_cost)
        unvisited.remove(current)

    return distances[end]


def mod_1(n: int) -> int:
    return 1 + ((n - 1) % 9)


def part2(data) -> int:
    new_data = []
    for row in data:
        new_row = row[:]
        for i in range(4):
            new_row.extend([mod_1(r + i + 1) for r in row])
        new_data.append(new_row)

    new_data_copy = new_data[:]
    for i in range(4):
        for row in new_data_copy:
            new_data.append([mod_1(r + i + 1) for r in row])

    # print("\n".join("".join(str(i) for i in row) for row in new_data))

    return part1(new_data)
