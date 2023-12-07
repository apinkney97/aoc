from __future__ import annotations

import dataclasses
from enum import Enum

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


class MapType(str, Enum):
    seed_to_soil = "seed-to-soil"
    soil_to_fertilizer = "soil-to-fertilizer"
    fertilizer_to_water = "fertilizer-to-water"
    water_to_light = "water-to-light"
    light_to_temperature = "light-to-temperature"
    temperature_to_humidity = "temperature-to-humidity"
    humidity_to_location = "humidity-to-location"


@dataclasses.dataclass
class Range:
    start: int  # inclusive
    end: int  # exclusive

    def __post_init__(self):
        if self.start >= self.end:
            raise ValueError(
                f"Start must be strictly less than end ({self.start = }, {self.end = })"
            )

    def __contains__(self, value: int) -> bool:
        return self.start <= value < self.end

    def overlaps(self, other: Range) -> bool:
        other_in_this = self.start <= other.start < self.end
        this_in_other = other.start <= self.start < other.end
        return other_in_this or this_in_other

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __lt__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.start < other.start

    def __hash__(self) -> int:
        return hash(f"{self.start}:{self.end}")

    def split(self, other, offset=0) -> tuple[Range | None, Range | None, Range | None]:
        # Split this range into sections that entirely overlap or don't overlap
        start_before = self.start < other.start
        start_after = self.start >= other.end
        end_before = self.end <= other.start
        end_after = self.end > other.end

        if end_before:
            return Range(start=self.start, end=self.end), None, None

        if start_after:
            return None, None, Range(start=self.start, end=self.end)

        if not (start_before or end_after):
            return None, Range(start=self.start + offset, end=self.end + offset), None

        # Here we know we must have some overlap
        before = None
        after = None

        if start_before:
            before = Range(start=self.start, end=other.start)

        if end_after:
            after = Range(start=other.end, end=self.end)

        middle = Range(
            start=max(self.start, other.start) + offset,
            end=min(self.end, other.end) + offset,
        )

        return before, middle, after


@dataclasses.dataclass
class MapRange(Range):
    dst: int

    def map(self, value: int) -> int:
        if value not in self:
            raise ValueError(f"Can't map {value}; not in range: {self}")
        return value + self.offset

    @property
    def offset(self):
        return self.dst - self.start


def load_data():
    data = utils.load_data(2023, 5, example=EXAMPLE)

    seeds = []
    maps = {}
    mode = None
    for line in data:
        if line.startswith("seeds:"):
            _, seeds_str = line.split(":")
            seeds = [int(s) for s in seeds_str.split()]
        elif not line:
            mode = None
        elif ":" in line:
            mode = MapType(line.split()[0])
        else:
            dst, src, size = [int(n) for n in line.split()]
            map_range = MapRange(start=src, dst=dst, end=src + size)
            maps.setdefault(mode, []).append(map_range)

    for map_list in maps.values():
        map_list.sort()

    return seeds, maps


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    locations = []
    # utils.enable_logging()
    seeds, maps = DATA
    for seed in seeds:
        for map_type in MapType:
            for map_range in maps[map_type]:
                if seed in map_range:
                    seed = map_range.map(seed)
                    break
        locations.append(seed)
    return min(locations)


def part2() -> int:
    # Seeds are now ranges
    seeds, maps = DATA

    seed_ranges = utils.PQ()
    while seeds:
        size = seeds.pop()
        start = seeds.pop()
        seed_ranges.add_item(Range(start, start + size), priority=start)

    # Split each seed range into more ranges
    for map_type in MapType:
        new_ranges = utils.PQ()

        # Find which seed ranges overlap which map ranges
        overlapping = {}
        for seed_range in seed_ranges:
            for map_range in maps[map_type]:
                if seed_range.overlaps(map_range):
                    overlapping.setdefault(seed_range, []).append(map_range)
            if seed_range not in overlapping:
                new_ranges.add_item(seed_range)
                seed_ranges.remove_item(seed_range)

        for seed_range, map_ranges in overlapping.items():
            for map_range in sorted(map_ranges):
                before, middle, after = seed_range.split(map_range, map_range.offset)

                if before:
                    new_ranges.add_item(before, priority=before.start)
                if middle:
                    new_ranges.add_item(middle, priority=middle.start)
                if after:
                    seed_range = after

        seed_ranges = new_ranges
    return seed_ranges.pop_item().start


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
    # tests()
