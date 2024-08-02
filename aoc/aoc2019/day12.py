import re
from dataclasses import dataclass
from itertools import combinations
from math import lcm
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


def parse_data(data):
    matcher = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
    parsed = []
    for line in data:
        match = matcher.fullmatch(line)
        parsed.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))
    return parsed


def build_moons(data):
    return [get_moon(*coord) for coord in data]


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


def part1(data):
    moons = build_moons(data)

    for i in range(1000):
        for dimension in "xyz":
            step(moons, dimension)

    return sum(get_energy(moon) for moon in moons)


def part2(data):
    moons = build_moons(data)
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
        len(seen_states["x"]), len(seen_states["y"]), len(seen_states["z"])
    )
    return periodicity
