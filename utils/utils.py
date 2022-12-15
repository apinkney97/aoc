import heapq
import itertools
import math
import os
import time
from contextlib import ContextDecorator
from functools import reduce
from operator import mul
from typing import Callable, Iterable, Optional

from utils.types import T, TNum

DEBUG = False


def enable_logging():
    global DEBUG
    DEBUG = True


def disable_logging():
    global DEBUG
    DEBUG = False


def log(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def load_data(
    day: int,
    strip: bool = True,
    *,
    fn: Optional[Callable[[str], T]] = None,
    example: bool = False,
) -> list[T] | list[str]:
    suffix = "-example" if example else ""
    with open(os.path.join("data", f"day{day:02d}{suffix}.data")) as f:
        data = f.readlines()
        if strip:
            data = [line.strip() for line in data]
        if fn is not None:
            data = [fn(line) for line in data]
        return data


def product(nums: Iterable[TNum]) -> TNum:
    return reduce(mul, nums)


def magnitude(*args: TNum) -> float:
    return math.sqrt(sum(a**2 for a in args))


def manhattan(*args: int) -> int:
    return sum(abs(a) for a in args)


def manhattan_border(centre: tuple[int, int], radius: int):
    cx, cy = centre

    for i in range(radius):
        yield cx + i, cy - i + radius
        yield cx - i + radius, cy - i
        yield cx - i, cy + i - radius
        yield cx + i - radius, cy + i


def triangle(n: int) -> int:
    return n * (n + 1) // 2


class timed(ContextDecorator):
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Took {time.monotonic() - self.start:.6f} secs")


def neighbours(coord: tuple[int, ...], include_diagonals: bool):
    dimensions = len(coord)
    if not include_diagonals:
        # +-1 on each dimension
        for d in range(dimensions):
            unpacked = list(coord)
            unpacked[d] -= 1
            yield tuple(unpacked)
            unpacked[d] += 2
            yield tuple(unpacked)
    else:
        # cartesian product of (-1, 0, +1) on each dimension, excluding original coord
        ranges = [(coord[d] - 1, coord[d], coord[d] + 1) for d in range(dimensions)]
        for new_coord in itertools.product(*ranges):
            if new_coord != coord:
                yield new_coord


class PQ:
    """Heavily "borrowed" from
    https://docs.python.org/3/library/heapq.html?highlight=heapq#priority-queue-implementation-notes
    """

    def __init__(self, max_heap: bool = False):
        self._pq = []  # list of entries arranged in a heap
        self._entry_finder = {}  # mapping of item to entries
        self._REMOVED = object()  # sentinel for a removed item
        self._counter = itertools.count()  # unique sequence count
        self._max_heap = max_heap

    def add_item(self, item, priority=0):
        """Add a new item or update the priority of an existing item"""
        if item in self._entry_finder:
            self.remove_item(item)
        count = next(self._counter)
        if self._max_heap:
            priority = -priority
        entry = [priority, count, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._pq, entry)

    def remove_item(self, item):
        """Mark an existing item as removed.  Raise KeyError if not found."""
        entry = self._entry_finder.pop(item)
        entry[-1] = self._REMOVED

    def pop_item(self):
        """Remove and return the lowest priority item. Raise KeyError if empty."""
        while self._pq:
            priority, count, item = heapq.heappop(self._pq)
            if item is not self._REMOVED:
                self._entry_finder.pop(item)
                return item
        raise KeyError("pop from an empty priority queue")
