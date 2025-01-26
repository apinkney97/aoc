from __future__ import annotations

from typing import Iterator, NamedTuple, overload, Generator

from aoc.utils.utils import manhattan, neighbours


class Vector(NamedTuple):
    """
    A relative offset between two points on a 2d grid
    """

    x: int | float
    y: int | float

    def __add__(self, other: Vector) -> Vector:  # type: ignore[override]
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other).__name__} to a Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other).__name__} to a Vector")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector:  # type: ignore[override]
        if not isinstance(other, int | float):
            raise TypeError(f"Can't multiply Vector by a {type(other).__name__}")
        return Vector(self.x * other, self.y * other)

    def __neg__(self) -> Vector:
        return self * -1

    @property
    def manhattan(self) -> int | float:
        return manhattan(self.x, self.y)


class Coord(NamedTuple):
    """
    An absolute coordinate on a 2d grid
    """

    x: int | float
    y: int | float

    def __add__(self, other: Vector) -> Coord:  # type: ignore[override]
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other).__name__} to a Coord")
        return Coord(self.x + other.x, self.y + other.y)

    @overload
    def __sub__(self, other: Vector) -> Coord: ...

    @overload
    def __sub__(self, other: Coord) -> Vector: ...

    def __sub__(self, other: Vector | Coord) -> Coord | Vector:
        if isinstance(other, Vector):
            return Coord(self.x - other.x, self.y - other.y)
        if isinstance(other, Coord):
            return Vector(self.x - other.x, self.y - other.y)

        raise TypeError(f"Can't subtract {type(other).__name__} from a Coord")

    def __mod__(self, other: Vector | Coord) -> Coord:
        return Coord(self.x % other.x, self.y % other.y)

    def neighbours(self, include_diagonals: bool = False) -> Generator[Coord]:
        for neighbour in neighbours((self.x, self.y), include_diagonals=include_diagonals):
            yield Coord(neighbour[0], neighbour[1])


def manhattan_border(centre: Coord, radius: int) -> Iterator[Coord]:
    """
    Returns an iterator of coordinates the specified radius away from the centre coordinate.

    This effectively describes a diamond shape.
    """
    if radius == 0:
        yield centre

    for r in range(radius):
        yield Coord(centre.x + r, centre.y - r + radius)
        yield Coord(centre.x - r + radius, centre.y - r)
        yield Coord(centre.x - r, centre.y + r - radius)
        yield Coord(centre.x + r - radius, centre.y + r)


def manhattan_limit(centre: Coord, radius: int) -> Iterator[Coord]:
    """
    Returns an iterator of coordinates within the specified radius of the centre coordinate.

    This effectively describes a filled diamond shape.
    """
    for r in range(radius + 1):
        yield from manhattan_border(centre, r)
