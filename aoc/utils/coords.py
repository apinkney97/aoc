from __future__ import annotations

import itertools
import typing
from typing import Generator, Iterable, Iterator, NamedTuple, overload

from aoc.utils.utils import manhattan


class Vector2D(NamedTuple):
    """
    A relative offset between two points on a 2d grid
    """

    x: int
    y: int

    def __add__(self, other: Vector2D) -> Vector2D:  # type: ignore[override]
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector2D) -> Vector2D:
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int) -> Vector2D:  # type: ignore[override]
        if isinstance(other, int):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __neg__(self) -> Vector2D:
        return self * -1

    @property
    def manhattan(self) -> int:
        return manhattan(self.x, self.y)


class Coord2D(NamedTuple):
    """
    An absolute coordinate on a 2d grid
    """

    x: int
    y: int

    def __add__(self, other: Vector2D) -> Coord2D:  # type: ignore[override]
        if isinstance(other, Vector2D):
            return Coord2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    @overload
    def __sub__(self, other: Coord2D) -> Vector2D: ...

    @overload
    def __sub__(self, other: Vector2D) -> Coord2D: ...

    def __sub__(self, other: Vector2D | Coord2D) -> Coord2D | Vector2D:
        if isinstance(other, Vector2D):
            return Coord2D(self.x - other.x, self.y - other.y)
        if isinstance(other, Coord2D):
            return Vector2D(self.x - other.x, self.y - other.y)

        return NotImplemented

    def __mod__(self, other: Vector2D | Coord2D) -> Coord2D:
        return Coord2D(self.x % other.x, self.y % other.y)

    def neighbours(self, include_diagonals: bool = False) -> Generator[Coord2D]:
        for neighbour in neighbours(
            (self.x, self.y), include_diagonals=include_diagonals
        ):
            yield Coord2D(neighbour[0], neighbour[1])

    def in_bounds(self, corner_1: Coord2D, corner_2: Coord2D) -> bool:
        max_x = max(corner_1.x, corner_2.y)
        min_x = min(corner_1.x, corner_2.y)
        max_y = max(corner_1.y, corner_2.y)
        min_y = min(corner_1.y, corner_2.y)

        return (min_x <= self.x <= max_x) and (min_y <= self.y <= max_y)


class Coord3D(NamedTuple):
    x: int
    y: int
    z: int


class Coord4D(NamedTuple):
    x: int
    y: int
    z: int
    w: int


def manhattan_border(centre: Coord2D, radius: int) -> Iterator[Coord2D]:
    """
    Returns an iterator of coordinates the specified radius away from the centre coordinate.

    This effectively describes a diamond shape.
    """
    if radius == 0:
        yield centre

    for r in range(radius):
        yield Coord2D(centre.x + r, centre.y - r + radius)
        yield Coord2D(centre.x - r + radius, centre.y - r)
        yield Coord2D(centre.x - r, centre.y + r - radius)
        yield Coord2D(centre.x + r - radius, centre.y + r)


def manhattan_limit(centre: Coord2D, radius: int) -> Iterator[Coord2D]:
    """
    Returns an iterator of coordinates within the specified radius of the centre coordinate.

    This effectively describes a filled diamond shape.
    """
    for r in range(radius + 1):
        yield from manhattan_border(centre, r)


@typing.overload
def neighbours(coord: Coord2D, *, include_diagonals: bool) -> Generator[Coord2D]: ...
@typing.overload
def neighbours(
    coord: Iterable[int], *, include_diagonals: bool
) -> Generator[tuple[int, ...]]: ...


def neighbours(
    coord: Iterable[int], *, include_diagonals: bool
) -> Generator[tuple[int, ...]] | Generator[Coord2D]:
    neighbours_ = _neighbours(coord, include_diagonals)
    if isinstance(coord, Coord2D):
        for neighbour in neighbours_:
            yield Coord2D(*neighbour)
        return
    yield from neighbours_


def _neighbours(
    coord: Iterable[int], include_diagonals: bool
) -> Generator[tuple[int, ...]]:
    """Returns the neighbours of the specified coordinate."""
    coord_tuple = tuple(coord)
    dimensions = len(coord_tuple)
    if not include_diagonals:
        # +-1 on each dimension
        for d in range(dimensions):
            unpacked = list(coord_tuple)
            unpacked[d] -= 1
            yield tuple(unpacked)
            unpacked[d] += 2
            yield tuple(unpacked)
    else:
        # cartesian product of (-1, 0, +1) on each dimension, excluding original coord
        ranges = [
            (coord_tuple[d] - 1, coord_tuple[d], coord_tuple[d] + 1)
            for d in range(dimensions)
        ]
        for new_coord in itertools.product(*ranges):
            if new_coord != coord_tuple:
                yield new_coord
