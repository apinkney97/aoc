import itertools

from aoc import utils
from aoc.utils.coords import Coord, Vector

EMPTY = 0
BOX = 1
WALL = 2
ROBOT = 3

BOX_LEFT = 4
BOX_RIGHT = 5


DIRECTIONS = {
    "^": Vector(0, -1),
    ">": Vector(1, 0),
    "v": Vector(0, 1),
    "<": Vector(-1, 0),
}


def parse_data(data):
    grid_lines, moves_lines = utils.split_by_blank_lines(data)

    return grid_lines, moves_lines


def part1(data) -> int:
    grid_lines, moves_lines = data
    robot = Coord(-1, -1)
    grid = utils.Grid2D(display_map={EMPTY: ".", BOX: "O", WALL: "#", ROBOT: "@"})
    for y, line in enumerate(grid_lines):
        for x, char in enumerate(line):
            match char:
                case "O":
                    grid[Coord(x, y)] = BOX
                case "#":
                    grid[Coord(x, y)] = WALL
                case "@":
                    grid[Coord(x, y)] = ROBOT
                    robot = Coord(x, y)

    for i, move in enumerate(itertools.chain(*moves_lines)):
        vector = DIRECTIONS[move]

        # Step until we find an empty space or a wall
        pos = robot + vector
        while grid[pos] not in {WALL, EMPTY}:
            pos += vector

        # If it's wall, no need to do anything, nothing moves

        if grid[pos] == EMPTY:
            # Robot's space becomes empty
            # Next space becomes robot
            # Any box moves from next to end
            next_pos = robot + vector
            if next_pos != pos:
                grid[pos] = BOX
            grid[robot] = EMPTY
            grid[next_pos] = ROBOT
            robot = next_pos

            utils.log(
                f"Move {i}, {move}: Went from {robot} to {pos}, found {grid[pos]}"
            )
            utils.log(grid)
        else:
            utils.log(f"Move {i}, {move}: No move")

    result = 0
    for coord in grid:
        if grid[coord] == BOX:
            result += 100 * coord.y + coord.x

    return result


class WallError(Exception):
    pass


def find_affected_cells(grid: utils.Grid2D, coord: Coord, vector: Vector) -> set[Coord]:
    # Up and down are more complicated.
    # Aligned boxes work the same as before
    # For misaligned boxes, need to check all boxes in a pyramid shape
    # If any are touching a wall, none move
    # Otherwise, all move

    # Names in this function assume we're pushing up, but should work equivalently for down

    this_cell = grid[coord]

    if this_cell == EMPTY:
        return set()
    if this_cell == WALL:
        raise WallError

    if this_cell == ROBOT:
        return {coord} | find_affected_cells(grid, coord + vector, vector)

    if this_cell in {BOX_LEFT, BOX_RIGHT}:
        if this_cell == BOX_LEFT:
            left_coord = coord
            right_coord = coord + DIRECTIONS[">"]
        else:
            right_coord = coord
            left_coord = coord + DIRECTIONS["<"]

        affected = {left_coord, right_coord}
        affected_left = find_affected_cells(grid, left_coord + vector, vector=vector)
        affected_right = find_affected_cells(grid, right_coord + vector, vector=vector)

        return affected | affected_left | affected_right

    raise ValueError(f"Can't move cell {coord=}: {this_cell=}")


def part2(data) -> int:
    grid_lines, moves_lines = data
    robot = Coord(-1, -1)
    grid = utils.Grid2D(
        display_map={EMPTY: ".", BOX_LEFT: "[", BOX_RIGHT: "]", WALL: "#", ROBOT: "@"}
    )
    for y, line in enumerate(grid_lines):
        for x, char in enumerate(line):
            left = Coord(2 * x, y)
            right = left + DIRECTIONS[">"]
            match char:
                case "O":
                    grid[left] = BOX_LEFT
                    grid[right] = BOX_RIGHT
                case "#":
                    grid[left] = WALL
                    grid[right] = WALL
                case "@":
                    grid[left] = ROBOT
                    robot = left

    for i, move in enumerate(itertools.chain(*moves_lines)):
        vector = DIRECTIONS[move]

        if move in {"<", ">"}:
            # Left and right are broadly the same as before.
            # Step until we find an empty space or a wall
            pos = robot
            affected = set()
            while grid[pos] not in {WALL, EMPTY}:
                affected.add(pos)
                pos += vector

            if grid[pos] == WALL:
                continue

        else:
            try:
                affected = find_affected_cells(grid, robot, vector)
            except WallError:
                continue

        for coord in sorted(
            affected, key=lambda c: (c.y, c.x), reverse=move in {"v", ">"}
        ):
            grid[coord + vector] = grid[coord]
            grid[coord] = EMPTY

        robot += vector

    result = 0
    for coord in grid:
        if grid[coord] == BOX_LEFT:
            result += 100 * coord.y + coord.x

    return result
