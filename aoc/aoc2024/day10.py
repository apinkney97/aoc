def parse_data(data):
    return [[int(c) for c in line] for line in data]


Coord = tuple[int, int]


def get_neighbours(coord, height, width):
    x, y = coord
    neighbours = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    return set(filter(lambda c: 0 <= c[0] < width and 0 <= c[1] < height, neighbours))


def part1(data) -> int:
    coords_by_height: dict[int, set[Coord]] = {}
    reachable_peaks_by_coord: dict[Coord, set[Coord]] = {}

    for y, line in enumerate(data):
        for x, height in enumerate(line):
            coord = x, y
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


def part2(data) -> int:
    coords_by_height: dict[int, set[Coord]] = {}
    scores_by_coord: dict[Coord, int] = {}

    for y, line in enumerate(data):
        for x, height in enumerate(line):
            coord = x, y
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
