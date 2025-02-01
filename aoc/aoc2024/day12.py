from aoc.utils.coords import Coord2D, Vector2D

UP = Vector2D(0, -1)
LEFT = Vector2D(-1, 0)
DOWN = Vector2D(0, 1)
RIGHT = Vector2D(1, 0)

DIRECTIONS = [UP, LEFT, DOWN, RIGHT]


def parse_data(data):
    grid = {}
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            grid[Coord2D(x, y)] = cell
    return grid


def get_regions(data) -> list[set[Coord2D]]:
    unvisited = set(data)

    regions = []
    while unvisited:
        coord = unvisited.pop()
        colour = data[coord]

        this_region = {coord}
        queue = [coord]

        # print(colour, coord)
        while queue:
            curr = queue.pop()
            for direction in DIRECTIONS:
                neighbour = curr + direction
                if neighbour in unvisited and data[neighbour] == colour:
                    unvisited.remove(neighbour)
                    queue.append(neighbour)
                    this_region.add(neighbour)
        regions.append(this_region)

    return regions


def part1(data) -> int:
    regions = get_regions(data)

    result = 0

    for region in regions:
        area = len(region)
        perimiter = 0
        for coord in region:
            colour = data[coord]
            for direction in DIRECTIONS:
                neighbour = coord + direction
                if data.get(neighbour) != colour:
                    perimiter += 1
        result += area * perimiter
    return result


def part2(data) -> int:
    """
    Number of sides == number of vertices

    - Each cell has 4 vertices
    - Each vertex can be convex or concave, or neither
    - Convex if both neighbours are out
    - Concave if both neighbours are in AND diagonal is out

    - Convex:
      ?A
      AX

    - Concave
      AX
      XX

    """
    regions = get_regions(data)

    pairs = list(zip(DIRECTIONS, DIRECTIONS[1:] + DIRECTIONS[:1]))

    result = 0
    for region in regions:
        vertices = 0
        for coord in region:
            for v1, v2 in pairs:
                n1 = coord + v1
                n2 = coord + v2
                if n1 not in region and n2 not in region:
                    # Convex
                    vertices += 1
                elif n1 in region and n2 in region and n1 + v2 not in region:
                    # Concave
                    vertices += 1
        area = len(region)
        result += area * vertices

    return result
