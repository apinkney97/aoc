from __future__ import annotations

from typing import NamedTuple, overload


class Vector(NamedTuple):
    """
    A relative offset between two points on a 2d grid
    """

    x: int | float
    y: int | float

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other).__name__} to a Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other).__name__} to a Vector")
        return Vector(self.x - other.x, self.y - other.y)


class Coord(NamedTuple):
    """
    An absolute coordinate on a 2d grid
    """

    x: int | float
    y: int | float

    def __add__(self, other: Vector) -> Coord:
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
