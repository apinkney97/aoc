import re
from dataclasses import dataclass
from typing import List

from aoc import utils


@dataclass
class Vector:
    x: int
    y: int
    z: int

    def as_tuple(self):
        return self.x, self.y, self.z


@dataclass
class Particle:
    p: Vector
    v: Vector
    a: Vector


def load_data():
    particle_re = re.compile(
        r"p=<(?P<px>-?\d+),(?P<py>-?\d+),(?P<pz>-?\d+)>, "
        r"v=<(?P<vx>-?\d+),(?P<vy>-?\d+),(?P<vz>-?\d+)>, "
        r"a=<(?P<ax>-?\d+),(?P<ay>-?\d+),(?P<az>-?\d+)>"
    )

    def process(line: str):
        match = particle_re.fullmatch(line)
        return Particle(
            p=Vector(int(match["px"]), int(match["py"]), int(match["pz"])),
            v=Vector(int(match["vx"]), int(match["vy"]), int(match["vz"])),
            a=Vector(int(match["ax"]), int(match["ay"]), int(match["az"])),
        )

    data = utils.load_data(2017, 20, fn=process)

    return data


def tick(particle: Particle):
    particle.v.x += particle.a.x
    particle.v.y += particle.a.y
    particle.v.z += particle.a.z

    particle.p.x += particle.v.x
    particle.p.y += particle.v.y
    particle.p.z += particle.v.z


def part1() -> int:
    # It will be one of the particles with the smallest acceleration
    # However it appears there are 3 of them

    data = load_data()
    min_a = None
    min_accels = {}

    for i, particle in enumerate(data):
        mag = utils.magnitude(*particle.a.as_tuple())
        if mag == min_a:
            min_accels[i] = particle
        else:
            old_min = min_a
            min_a = utils.safe_min(min_a, mag)
            if old_min != min_a:
                min_accels = {i: particle}

    while True:
        # run simulation until all particles have all position,velocity, and
        # acceleration components with the same signs (or zero)

        should_break = True

        for particle in min_accels.values():
            tick(particle)
            for dim in "xyz":
                a = getattr(particle.a, dim)
                v = getattr(particle.v, dim)
                p = getattr(particle.p, dim)

                if a != 0 and not (
                    (a > 0 and v > 0 and p > 0) or (a < 0 and v < 0 and p < 0)
                ):
                    should_break = False
                    break

        if should_break:
            # do some more steps just in case
            for _ in range(1000):
                for particle in min_accels.values():
                    tick(particle)

            break

    min_dist = None
    min_i = None

    for i, particle in min_accels.items():
        dist = utils.manhattan(*particle.p.as_tuple())
        min_dist = utils.safe_min(min_dist, dist)
        if min_dist == dist:
            min_i = i

    return min_i


def remove_collisions(particles: List[Particle]) -> List[Particle]:
    seen = {}
    dupes = set()
    for particle in particles:
        key = particle.p.as_tuple()
        if key in seen:
            dupes.add(key)
        else:
            seen[key] = particle

    for dupe in dupes:
        seen.pop(dupe)

    return list(seen.values())


def part2() -> int:
    particles = load_data()

    ticks_since_collision = 0
    while True:
        old_len = len(particles)
        particles = remove_collisions(particles)
        new_len = len(particles)
        if old_len > new_len:
            ticks_since_collision = 0
        else:
            ticks_since_collision += 1

        for particle in particles:
            tick(particle)

        if ticks_since_collision > 100:
            break

    return len(particles)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
