type Data = dict[str, set[str]]


def parse_data(data: list[str]) -> Data:
    parsed_data = {}
    for line in data:
        val, _, neighbours = line.split(" ", 2)
        parsed_data[val] = {n for n in neighbours.split(", ")}
    return parsed_data


def part1(data: Data) -> int:
    seen = set()
    to_expand = ["0"]

    while to_expand:
        curr = to_expand.pop()
        seen.add(curr)
        for neighbour in data[curr]:
            if neighbour not in seen:
                to_expand.append(neighbour)

    return len(seen)


def part2(data: Data) -> int:
    seen = set()
    not_seen = set(data.keys())
    to_expand = {"0"}

    subgraphs = 1
    while to_expand:
        curr = to_expand.pop()
        seen.add(curr)
        not_seen.remove(curr)
        for neighbour in data[curr]:
            if neighbour not in seen:
                to_expand.add(neighbour)

        if not to_expand and not_seen:
            to_expand.add(next(iter(not_seen)))
            subgraphs += 1

    return subgraphs
