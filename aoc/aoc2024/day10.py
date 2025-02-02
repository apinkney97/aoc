from aoc.utils import Coord2D, neighbours

type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    return [[int(c) for c in line] for line in data]


def get_neighbours(coord: Coord2D, height: int, width: int) -> set[Coord2D]:
    return set(
        filter(
            lambda c: c.in_bounds(Coord2D(0, 0), Coord2D(width, height)),
            neighbours(coord, include_diagonals=False),
        )
    )


def part1(data: Data) -> int:
    coords_by_height: dict[int, set[Coord2D]] = {}
    reachable_peaks_by_coord: dict[Coord2D, set[Coord2D]] = {}

    for y, line in enumerate(data):
        for x, height in enumerate(line):
            coord = Coord2D(x, y)
            coords_by_height.setdefault(height, set()).add(coord)
            if height == 9:
                reachable_peaks_by_coord[coord] = {coord}

    for height in range(8, -1, -1):
        for coord in coords_by_height[height]:
            reachable_peaks = set()
            for neighbour in get_neighbours(coord, len(data), len(data[0])):
                # Union of reachable peaks of neighbours of h+1
                if neighbour in coords_by_height[height + 1]:
                    reachable_peaks |= reachable_peaks_by_coord[neighbour]
            reachable_peaks_by_coord[coord] = reachable_peaks

    result = 0
    for coord in coords_by_height[0]:
        result += len(reachable_peaks_by_coord[coord])

    return result


def part2(data: Data) -> int:
    coords_by_height: dict[int, set[Coord2D]] = {}
    scores_by_coord: dict[Coord2D, int] = {}

    for y, line in enumerate(data):
        for x, height in enumerate(line):
            coord = Coord2D(x, y)
            coords_by_height.setdefault(height, set()).add(coord)
            if height == 9:
                scores_by_coord[coord] = 1

    for height in range(8, -1, -1):
        for coord in coords_by_height[height]:
            score = 0
            for neighbour in get_neighbours(coord, len(data), len(data[0])):
                # Sum of scores of neighbours of h+1
                if neighbour in coords_by_height[height + 1]:
                    score += scores_by_coord[neighbour]
            scores_by_coord[coord] = score

    result = 0
    for coord in coords_by_height[0]:
        result += scores_by_coord[coord]

    return result
