from dataclasses import dataclass
from itertools import combinations
from typing import List


@dataclass
class Triple:
    x: int
    y: int
    z: int


@dataclass
class Body:
    position: Triple
    velocity: Triple


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


def get_moon(x, y, z, dx=0, dy=0, dz=0) -> Body:
    return Body(Triple(x, y, z), Triple(dx, dy, dz))


def step(moons: List[Body], dimension: str):
    # Update velocities
    for moon1, moon2 in combinations(moons, 2):
        p1 = getattr(moon1.position, dimension)
        p2 = getattr(moon2.position, dimension)
        if p1 == p2:
            continue

        v1 = getattr(moon1.velocity, dimension)
        v2 = getattr(moon2.velocity, dimension)

        if p1 < p2:
            a1, a2 = 1, -1
        else:
            a1, a2 = -1, 1

        setattr(moon1.velocity, dimension, v1 + a1)
        setattr(moon2.velocity, dimension, v2 + a2)

    # Update positions
    for moon in moons:
        p = getattr(moon.position, dimension)
        v = getattr(moon.velocity, dimension)
        setattr(moon.position, dimension, p + v)


def get_state(moons: List[Body], dimension: str):
    vals = []
    for moon in moons:
        vals.append(getattr(moon.position, dimension))
        vals.append(getattr(moon.velocity, dimension))

    return tuple(vals)


def get_energy(moon: Body):
    dimensions = "xyz"
    potential = sum(abs(getattr(moon.position, d)) for d in dimensions)
    kinetic = sum(abs(getattr(moon.velocity, d)) for d in dimensions)
    return potential * kinetic


def main():
    def input_moons():
        return [
            get_moon(-14, -4, -11),
            get_moon(-9, 6, -7),
            get_moon(4, 1, 4),
            get_moon(2, -14, -9),
        ]

    moons = input_moons()

    for i in range(1000):
        for dimension in "xyz":
            step(moons, dimension)

    print("Part 1:", sum(get_energy(moon) for moon in moons))

    moons = input_moons()
    seen_states = {}
    for dimension in "xyz":
        seen = set()
        seen_states[dimension] = seen
        state = get_state(moons, dimension)
        while state not in seen:
            seen.add(state)
            step(moons, dimension)
            state = get_state(moons, dimension)

    periodicity = lcm(
        len(seen_states["x"]), lcm(len(seen_states["y"]), len(seen_states["z"]))
    )
    print("Part 2:", periodicity)


if __name__ == "__main__":
    main()
