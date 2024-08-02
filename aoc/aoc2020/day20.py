import operator
import re
from collections import Counter
from functools import reduce
from itertools import chain
from typing import Dict, List, NamedTuple, NewType

TileId = NewType("TileId", int)
Edge = NewType("Edge", str)


class Edges(NamedTuple):
    top: Edge
    right: Edge
    bottom: Edge
    left: Edge


class Tile:
    def __init__(self, tile_id: int, data: List[str]):
        self.tile_id = TileId(tile_id)
        self._data = data

        self._rotation = 0
        self._flipped = False

        self.is_corner = False
        self.is_edge = False

    @property
    def flipped(self):
        return self.flipped

    def flip(self):
        self._flipped = not self._flipped

    def rotate(self):
        self._rotation = (self._rotation + 1) % 4

    @property
    def edges(self) -> Edges:
        top = self._data[0]
        right = "".join(d[-1] for d in self._data)
        bottom = self._data[-1][::-1]
        left = "".join(d[0] for d in reversed(self._data))

        # Flip about the Y axis
        if self._flipped:
            top = top[::-1]
            bottom = bottom[::-1]
            right, left = left[::-1], right[::-1]

        # Then apply rotations
        edges = [Edge(top), Edge(right), Edge(bottom), Edge(left)]
        rotated_edges = edges[self._rotation :] + edges[: self._rotation]

        return Edges(*rotated_edges)

    def _get_transformed_data(self, data):
        if self._flipped:
            data = [line[::-1] for line in data]

        if self._rotation == 2:
            data = [line[::-1] for line in data[::-1]]
        elif self._rotation % 2 == 1:
            # transpose the lists
            new_rows = [[] for _ in range(len(data[0]))]
            for row in reversed(data):
                for i, col in enumerate(row):
                    new_rows[i].append(col)
            data = ["".join(row) for row in new_rows]
            if self._rotation == 1:
                data = [line[::-1] for line in data[::-1]]
        return data

    @property
    def centre(self):
        data = [line[1:-1] for line in self._data[1:-1]]
        data = self._get_transformed_data(data)
        return data

    @property
    def data(self):
        return self._get_transformed_data(self._data)

    def __repr__(self):
        return f"Tile(id={self.tile_id})"


def parse_data(data) -> List[Tile]:
    tiles = []

    tile_data = []
    tile_id = 0
    for line in data:
        if not line:
            tiles.append(Tile(tile_id, tile_data))
            tile_data = []

        elif line.startswith("Tile"):
            tile_id = int(line.split()[1][:-1])

        else:
            tile_data.append(line)

    if tile_data:
        tiles.append(Tile(tile_id, tile_data))

    return tiles


def edges_to_tiles(data: List[Tile]) -> Dict[Edge, List[TileId]]:
    # map edges (and their reflections) to tiles they belong to
    edges = {}
    for tile in data:
        for edge in tile.edges:
            edges.setdefault(edge, []).append(tile.tile_id)
            edges.setdefault(Edge(edge[::-1]), []).append(tile.tile_id)

    return edges


def get_counts(edges: Dict[Edge, List[TileId]]) -> Dict[TileId, int]:
    # count the number of edges for each tile that have no matching pair
    counts = Counter()
    for edge in edges:
        n_edges = len(edges[edge])
        if n_edges == 1:
            tile_id = edges[edge][0]
            counts[tile_id] += 1

    return dict(counts)


def part1(data) -> int:
    edges = edges_to_tiles(data)
    counts = get_counts(edges)

    # Empirically it seems that there are no duplicated edges (ie 2 or more pairs the same)
    # or any palindromic edges. This makes things easier!

    # Find the tiles with 4 unique edges (4 because we double count each edge due to reflections).
    # These must be the corner tiles.

    result = 1
    for tile_id, count in counts.items():
        if count == 4:
            result *= tile_id

    return result


def _add_match(tiles, row, other, horizontal):
    # need to match top to bottom of above
    to_match = other.edges.right if horizontal else other.edges.bottom
    to_match = to_match[::-1]

    for tile in tiles.values():
        tile_edges = set(tile.edges)
        all_edges = set(chain(tile_edges, (e[::-1] for e in tile_edges)))

        if to_match in all_edges:
            if to_match not in tile_edges:
                tile.flip()

            while (tile.edges.left if horizontal else tile.edges.top) != to_match:
                tile.rotate()

            row.append(tile)
            tiles.pop(tile.tile_id)
            break
    else:
        print(f"No match found for {to_match}")
        for tile in tiles.values():
            print(tile, tile.edges)


def part2(data) -> int:
    edge_length = int(len(data) ** 0.5)
    # print(edge_length)
    edges = edges_to_tiles(data)
    counts = get_counts(edges)

    tiles = {tile.tile_id: tile for tile in data}

    corners = []

    for tile_id, count in counts.items():
        tile = tiles[tile_id]
        if count == 4:
            tile.is_corner = True
            corners.append(tile)
        elif count == 2:
            tile.is_edge = True

    some_corner = corners[0]
    tiles.pop(some_corner.tile_id)

    for _ in range(4):
        # Rotate until the non-matching edges are on the top left
        e = some_corner.edges
        if len(edges[e.left]) == 1 and len(edges[e.top]) == 1:
            break
        some_corner.rotate()

    # All edges only have one match, so if we find any match that must be it

    grid = []

    for r in range(edge_length):
        row = []
        grid.append(row)
        for c in range(edge_length):
            if r == c == 0:
                row.append(some_corner)
            elif c == 0:
                # need to match top to bottom of above
                above = grid[-2][0]
                _add_match(tiles, row, above, horizontal=False)
            else:
                # match left to right of previous
                prev = row[-1]
                _add_match(tiles, row, prev, horizontal=True)

    full_grid = []
    for row in grid:
        new_rows = ["" for _ in range(8)]
        for tile in row:
            for i, line in enumerate(tile.centre):
                new_rows[i] += line
        full_grid.extend(new_rows)

    total_hashes = sum(line.count("#") for line in full_grid)

    monster_parts = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]

    hashes_per_monster = sum(line.count("#") for line in monster_parts)

    monster_res = [
        re.compile(r"(?=(" + part.replace(" ", ".") + r"))")
        for part in reversed(monster_parts)
    ]

    t = Tile(0, full_grid)

    # Got this through trial and error:
    # t.flip()
    for _ in range(3):
        t.rotate()

    data = t.data

    monsters = 0

    for three_lines in zip(data, data[1:], data[2:]):
        all_indexes = []
        for re_, line in zip(monster_res, three_lines):
            all_indexes.append({match.start() for match in re_.finditer(line)})
        matches = reduce(operator.and_, all_indexes)
        if matches:
            # print(f"Found {len(matches)}")
            monsters += len(matches)

    return total_hashes - (monsters * hashes_per_monster)
