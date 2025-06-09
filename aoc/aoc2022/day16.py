import collections
import itertools
import re

type Valve = tuple[int, list[str]]
type Distances = dict[tuple[str, str], int]
type Data = tuple[dict[str, Valve], Distances]


def parse_data(data: list[str]) -> Data:
    matcher = re.compile(
        r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)$"
    )
    matches = [matcher.fullmatch(line) for line in data]

    valves = {}
    for match in matches:
        assert match is not None
        name = match.group(1)
        flow = int(match.group(2))
        neighbours = match.group(3).split(", ")

        valves[name] = (flow, neighbours)

    dists = get_distances(valves)
    return valves, dists


def get_distances(valves: dict[str, Valve]) -> Distances:
    valves_of_interest = sorted(
        [name for name, valve in valves.items() if valve[0] > 0 or name == "AA"]
    )
    dists: Distances = {}
    for start, end in itertools.combinations(valves_of_interest, 2):
        visited = set()
        parents: dict[str, str | None] = {start: None}
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

        curr: str | None = end
        dist = 0
        while curr is not None:
            curr = parents[curr]
            dist += 1
        dists[start, end] = dist

    return dists


def search(
    valves: dict[str, Valve], dists: Distances, time_limit: int
) -> dict[frozenset[str], int]:
    best_by_valves: dict[frozenset[str], int] = {}

    useful_valves = [name for name, valve in valves.items() if valve[0] > 0]

    def step(time: int, flow: int, pos: str, open_valves: frozenset[str]) -> None:
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
            key = (pos, neighbour) if pos <= neighbour else (neighbour, pos)
            dist = dists[key]
            step(
                time=time - dist,
                flow=flow,
                pos=neighbour,
                open_valves=open_valves,
            )

    step(time=time_limit, flow=0, pos="AA", open_valves=frozenset())

    return best_by_valves


def part1(data: Data) -> int:
    valves, dists = data
    return max(search(valves, dists, 30).values())


def part2(data: Data) -> int:
    valves, dists = data
    # Find all "best" paths by open valves
    best_by_valves = search(valves, dists, 26)

    best = 0

    # Check all non-overlapping pairs of paths
    for valves_me, valves_elephant in itertools.combinations(best_by_valves, 2):
        if valves_me & valves_elephant:
            continue
        best_total = best_by_valves[valves_me] + best_by_valves[valves_elephant]
        if best_total > best:
            best = best_total

    return best
