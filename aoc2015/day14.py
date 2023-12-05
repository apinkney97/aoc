import re

import utils


def _load_data():
    match = re.compile(
        r"(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<time>\d+) "
        r"seconds, but then must rest for (?P<rest>\d+) seconds\."
    )

    return utils.load_data(2015, 14, fn=match.fullmatch)


DATA = _load_data()


class Reindeer:
    def __init__(self, name: str, speed: int, time: int, rest: int):
        self._name = name
        self._speed = speed
        self._move_time = time
        self._rest_time = rest
        self.position = 0

        self.score = 0

    def run(self):
        while True:
            for _ in range(self._move_time):
                self.position += self._speed
                yield self
            for _ in range(self._rest_time):
                yield self


def part1():
    reindeer = []
    for d in DATA:
        reindeer.append(
            Reindeer(
                name=d.group("name"),
                speed=int(d.group("speed")),
                time=int(d.group("time")),
                rest=int(d.group("rest")),
            )
        )

    runners = zip(*(r.run() for r in reindeer))

    for _ in range(2503):
        next(runners)
        reindeer.sort(key=lambda r: r.position, reverse=True)
        for r in reindeer:
            if r.position == reindeer[0].position:
                r.score += 1

    print(f"Part 1: {max(r.position for r in reindeer)}")
    print(f"Part 2: {max(r.score for r in reindeer)}")


def main() -> None:
    part1()


if __name__ == "__main__":
    main()
