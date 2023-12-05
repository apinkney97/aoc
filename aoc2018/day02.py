from collections import Counter

import utils


def part1():
    data = utils.load_data(2018, 2)

    twos = 0
    threes = 0

    for id_ in data:
        # This probably does more counting than is necessary but it
        # means I don't have to implement Counter myself.
        counts = Counter(id_)
        if any(v == 2 for v in counts.values()):
            twos += 1
        if any(v == 3 for v in counts.values()):
            threes += 1

    return twos * threes


def part2():
    data = utils.load_data(2018, 2)

    seen = set()

    for id_ in data:
        for i, _ in enumerate(id_):
            parts = id_[:i], id_[i + 1 :]
            if parts in seen:
                return "".join(parts)
            seen.add(parts)
    return None


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
