import utils


def get_data():
    data = {}
    for line in utils.load_data(2017, 12):
        val, _, neighbours = line.split(" ", 2)
        data[val] = {n for n in neighbours.split(", ")}
    return data


def part1():
    data = get_data()

    seen = set()
    to_expand = ["0"]

    while to_expand:
        curr = to_expand.pop()
        seen.add(curr)
        for neighbour in data[curr]:
            if neighbour not in seen:
                to_expand.append(neighbour)

    return len(seen)


def part2():
    data = get_data()

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


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
