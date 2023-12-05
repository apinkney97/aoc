import collections
import itertools
import re

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    matcher = re.compile(
        r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$"
    )
    data = utils.load_data(2022, 16, example=EXAMPLE, fn=matcher.fullmatch)

    valves = {}
    for row in data:
        name = row.group(1)
        flow = int(row.group(2))
        neighbours = row.group(3).split(", ")

        valves[name] = (flow, neighbours)

    dists = get_distances(valves)
    return valves, dists


def get_distances(valves):
    valves_of_interest = sorted(
        [name for name, valve in valves.items() if valve[0] > 0 or name == "AA"]
    )
    dists = {}
    for start, end in itertools.combinations(valves_of_interest, 2):
        visited = set()
        parents = {start: None}
        queue = collections.deque([start])
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current == end:
                break
            for neighbour in valves[current][1]:
                if neighbour in visited:
                    continue
                queue.append(neighbour)
                parents[neighbour] = current

        current = end
        dist = 0
        while current is not None:
            current = parents[current]
            dist += 1
        dists[start, end] = dist

    return dists


DATA = load_data()


def search(time_limit: int) -> dict[frozenset[str], int]:
    valves, dists = DATA

    best_by_valves = {}

    useful_valves = [name for name, valve in valves.items() if valve[0] > 0]

    def step(time: int, flow: int, pos: str, open_valves: frozenset[str]):
        # Open the valve we are on (except AA)
        if time > 0 and pos != "AA":
            flow += time * valves[pos][0]
            open_valves = open_valves.union({pos})

        # Record the highest flow we see for a given set of open valves
        prev_best = best_by_valves.get(open_valves, 0)
        if flow > prev_best:
            best_by_valves[open_valves] = flow

        if time <= 0 or len(useful_valves) == len(open_valves):
            return

        for neighbour in useful_valves:
            if neighbour in open_valves:
                continue
            dist = dists[tuple(sorted([pos, neighbour]))]
            step(
                time=time - dist,
                flow=flow,
                pos=neighbour,
                open_valves=open_valves,
            )

    step(time=time_limit, flow=0, pos="AA", open_valves=frozenset())

    return best_by_valves


def part1() -> int:
    return max(search(30).values())


def part2() -> int:
    # Find all "best" paths by open valves
    best_by_valves = search(26)

    best = 0

    # Check all non-overlapping pairs of paths
    for valves_me, valves_elephant in itertools.combinations(best_by_valves, 2):
        if valves_me & valves_elephant:
            continue
        best_total = best_by_valves[valves_me] + best_by_valves[valves_elephant]
        if best_total > best:
            best = best_total

    return best


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
