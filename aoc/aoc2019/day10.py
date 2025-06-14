import collections
import math
from fractions import Fraction
from itertools import product

type Data = list[str]
type Coord = tuple[int, int]


class Vector:
    def __init__(self, origin: Coord, destination: Coord) -> None:
        self.origin = origin
        self.destination = destination

        self._x1 = origin[0]
        self._y1 = origin[1]
        self._x2 = destination[0]
        self._y2 = destination[1]

        self.dx = self._x1 - self._x2
        self.dy = self._y1 - self._y2

        sign_x = self.dx // abs(self.dx) if self.dx else 0
        sign_y = self.dy // abs(self.dy) if self.dy else 0

        if self.dx == 0 or self.dy == 0:
            self.direction = (sign_x, sign_y)
        else:
            # simplify the ratio
            f = Fraction(abs(self.dx), abs(self.dy))
            self.direction = (f.numerator * sign_x, f.denominator * sign_y)

        # SOH CAH TOA...
        self.angle = math.atan2(-self.dx, self.dy)
        # atan2 gives us angles in the interval [-pi, pi], but we want [0, 2*pi]
        if self.angle < 0:
            self.angle += 2 * math.pi

        self.manhattan = abs(self.dx) + abs(self.dy)
        self.magnitude = math.sqrt(self.dx**2 + self.dy**2)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.origin}, {self.destination})"

    def __str__(self) -> str:
        direction = str(self.direction)
        manhattan = self.manhattan
        angle = self.angle * 180 / math.pi
        return f"{repr(self):30s} {direction=:10s} {manhattan = :3d}   {angle = :3.0f}"


def calculate_visibility(data: Data) -> tuple[dict[Coord, list[Vector]], int, Coord]:
    asteroid_coords = []
    for y, row in enumerate(data):
        for x, sector in enumerate(row):
            if sector == "#":
                asteroid_coords.append((x, y))

    visible_asteroids: dict[Coord, set[Coord]] = {}
    all_vectors: dict[Coord, list[Vector]] = {}

    for origin, destination in product(asteroid_coords, asteroid_coords):
        if origin == destination:
            continue

        vector = Vector(origin, destination)

        visible_asteroids.setdefault(origin, set()).add(vector.direction)
        all_vectors.setdefault(origin, []).append(vector)

    max_visible, max_coord = max(
        (len(directions), coord) for coord, directions in visible_asteroids.items()
    )
    return all_vectors, max_visible, max_coord


def part1(data: Data) -> int:
    _, max_visible, _ = calculate_visibility(data)
    return max_visible


def part2(data: Data) -> int:
    all_vectors, _, max_coord = calculate_visibility(data)
    other_asteroids = sorted(all_vectors[max_coord], key=lambda x: x.magnitude)
    asteroids_by_angle: dict[float, collections.deque[Coord]] = {}
    for asteroid in other_asteroids:
        asteroids_by_angle.setdefault(asteroid.angle, collections.deque()).append(
            asteroid.destination
        )

    count = 0
    while asteroids_by_angle:
        for angle in list(sorted(asteroids_by_angle.keys())):
            coords = asteroids_by_angle[angle]
            count += 1
            coord = coords.popleft()
            if count == 200:
                return 100 * coord[0] + coord[1]
            if not len(coords):
                asteroids_by_angle.pop(angle)

    return -1
