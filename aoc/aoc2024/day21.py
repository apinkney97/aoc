import functools
import itertools
import re

from aoc.utils import Coord2D


def find_dpad_paths() -> dict[tuple[str, str], list[str]]:
    """
     ^A
    <v>
    """
    keys = {
        "^": Coord2D(1, 0),
        "A": Coord2D(2, 0),
        "<": Coord2D(0, 1),
        "v": Coord2D(1, 1),
        ">": Coord2D(2, 1),
    }
    edge_keys = {k for k, coord in keys.items() if coord.x == 0 or coord.y == 0}
    paths = {}
    for start_key, start_pos in keys.items():
        for end_key, end_pos in keys.items():
            dx, dy = end_pos - start_pos
            if dx >= 0:
                x = ">" * dx
            else:
                x = "<" * -dx
            if dy >= 0:
                y = "v" * dy
            else:
                y = "^" * -dy

            if x and y:
                # Multiple paths
                # Disallow ones that go over (0, 0)
                if start_key in edge_keys and end_key in edge_keys:
                    # always up before left
                    # always right before down
                    if x[0] == ">":
                        path = x + y + "A"
                    else:
                        path = y + x + "A"
                    paths[start_key, end_key] = [path]
                else:
                    paths[start_key, end_key] = [y + x + "A", x + y + "A"]
            else:
                paths[start_key, end_key] = [x + y + "A"]
    return paths


def find_numpad_paths() -> dict[tuple[str, str], list[str]]:
    """
    789
    456
    123
     0A
    """
    keys = {
        "7": Coord2D(0, 3),
        "8": Coord2D(1, 3),
        "9": Coord2D(2, 3),
        "4": Coord2D(0, 2),
        "5": Coord2D(1, 2),
        "6": Coord2D(2, 2),
        "1": Coord2D(0, 1),
        "2": Coord2D(1, 1),
        "3": Coord2D(2, 1),
        "0": Coord2D(1, 0),
        "A": Coord2D(2, 0),
    }
    edge_keys = {k for k, coord in keys.items() if coord.x == 0 or coord.y == 0}
    paths = {}
    for start_key, start_pos in keys.items():
        for end_key, end_pos in keys.items():
            dx, dy = end_pos - start_pos
            if dx >= 0:
                x = ">" * dx
            else:
                x = "<" * -dx
            if dy >= 0:
                y = "^" * dy
            else:
                y = "v" * -dy

            if x and y:
                # Multiple paths
                # Disallow ones that go over (0, 0)
                if start_key in edge_keys and end_key in edge_keys:
                    # always up before left
                    # always right before down
                    if x[0] == ">":
                        path = x + y + "A"
                    else:
                        path = y + x + "A"
                    paths[start_key, end_key] = [path]
                else:
                    paths[start_key, end_key] = [y + x + "A", x + y + "A"]
            else:
                paths[start_key, end_key] = [x + y + "A"]
    return paths


DPAD_PATHS = find_dpad_paths()
NUMPAD_PATHS = find_numpad_paths()


@functools.cache
def get_min_path_len(keys: str, depth: int) -> int:
    if depth == 0:
        return len(keys)

    best_len = 0

    parts = re.findall(r"[<>v^]*A", keys)
    for part in parts:
        best_len += min(
            get_min_path_len(ks, depth - 1) for ks in expand(part, DPAD_PATHS)
        )

    return best_len


def expand(keys: str, moves: dict[tuple[str, str], list[str]]) -> list[str]:
    bits = []

    pos = "A"
    for key in keys:
        outs = moves[pos, key]
        bits.append(outs)
        pos = key

    candidates = []
    for keys_ in itertools.product(*bits):
        candidate = "".join(keys_)
        candidates.append(candidate)

    return candidates


def part1(data: list[str], depth: int = 2) -> int:
    result = 0

    for line in data:
        lens = []

        for keys in expand(line, moves=NUMPAD_PATHS):
            lens.append(get_min_path_len(keys, depth=depth))

        result += int(line[:-1]) * min(lens)

    return result


def part2(data: list[str]) -> int:
    return part1(data, 25)
