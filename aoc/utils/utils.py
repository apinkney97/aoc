import enum
import heapq
import itertools
import math
import time
from collections.abc import Sequence
from contextlib import ContextDecorator
from dataclasses import dataclass
from datetime import timedelta
from functools import reduce
from operator import mul
from types import TracebackType
from typing import Any, Iterable, Iterator, Generator

from rich.console import Console
from rich.pretty import Pretty

from aoc import config
from aoc.utils.types import TNum

CONSOLE = Console()


def log(*args: Any, **kwargs: Any) -> None:
    if config.DEBUG:
        CONSOLE.print(*args, **kwargs)


def pprint(*args: Any, **kwargs: Any) -> None:
    if config.DEBUG:
        prettified = Pretty(*args, **kwargs)
        # aside: "pretty" is a dreadful spelling...
        CONSOLE.print(prettified)


def product(nums: Iterable[TNum]) -> TNum:
    """Returns the product of the iterable passed in"""
    return reduce(mul, nums)


def magnitude(*args: TNum) -> float:
    """Returns the magnitude of the vector specified by the orthogonal input vectors"""
    return math.sqrt(sum(a**2 for a in args))


def manhattan(*args: TNum) -> TNum:
    """Returns the manhattan distance between the given orthogonal distances"""
    return sum(abs(a) for a in args)


def triangle(n: int) -> int:
    """Returns the nth triangle number"""
    return n * (n + 1) // 2


class timed(ContextDecorator):
    def __init__(self, text: str = ""):
        self.text = text

    def __enter__(self) -> None:
        self.start = time.perf_counter_ns()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType,
    ) -> None:
        duration_ns = time.perf_counter_ns() - self.start
        duration_td = timedelta(microseconds=duration_ns // 1000)
        if self.text:
            CONSOLE.print(f"Timing {self.text}")
        CONSOLE.print(f"Took {duration_td} ({duration_ns} ns)")


def neighbours(coord: tuple[int, ...], *, include_diagonals: bool) -> Generator[tuple[int, ...]]:
    """Returns the neighbours of the specified coordinate."""
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


class PQUpdates(enum.Enum):
    ANY = enum.auto()
    NONE = enum.auto()
    GREATER = enum.auto()
    LESSER = enum.auto()


class _PQRemoved:
    pass


@dataclass
class _PQEntry[T]:
    priority: int
    count: int
    item: T | _PQRemoved


class PQ[T]:
    """Heavily "borrowed" from
    https://docs.python.org/3/library/heapq.html?highlight=heapq#priority-queue-implementation-notes
    """

    def __init__(
        self, max_heap: bool = False, allow_updates: PQUpdates = PQUpdates.ANY
    ):
        self._pq: list[_PQEntry[T]] = []  # list of entries arranged in a heap
        self._entry_finder: dict[
            T, _PQEntry[T]
        ] = {}  # mapping of each item to its entry
        self._counter = itertools.count()  # unique sequence count
        self._max_heap = max_heap
        self._allow_updates = allow_updates

    def add_item(self, item: T, priority: int = 0) -> None:
        """Add a new item or update the priority of an existing item"""
        if item in self._entry_finder:
            # Prevent updates to existing entries
            if self._allow_updates is PQUpdates.NONE:
                return
            old_priority = self._entry_finder[item].priority
            if self._allow_updates is PQUpdates.GREATER and priority <= old_priority:
                return
            if self._allow_updates is PQUpdates.LESSER and priority >= old_priority:
                return

            self.remove_item(item)

        count = next(self._counter)
        if self._max_heap:
            priority = -priority
        entry = _PQEntry(priority, count, item)
        self._entry_finder[item] = entry
        heapq.heappush(self._pq, entry)

    def remove_item(self, item: T) -> None:
        """Mark an existing item as removed.  Raise KeyError if not found."""
        entry = self._entry_finder.pop(item)
        entry.item = _PQRemoved()

    def pop_item(self) -> T:
        """Remove and return the lowest priority item. Raise KeyError if empty."""
        while self._pq:
            item = heapq.heappop(self._pq).item
            if not isinstance(item, _PQRemoved):
                self._entry_finder.pop(item)
                return item
        raise KeyError("pop from an empty priority queue")

    def peek(self) -> T:
        """Show the item with the lowest priority, but do not remove it. Raise KeyError if empty."""
        while self._pq:
            item = self._pq[0].item
            if not isinstance(item, _PQRemoved):
                return item
            heapq.heappop(self._pq)

        raise KeyError("peek at empty priority queue")

    def __len__(self) -> int:
        return len(self._entry_finder)

    def __repr__(self) -> str:
        return f"PQ({list(self)})"

    def __iter__(self) -> Iterator[T]:
        for entry in sorted(
            self._entry_finder.values(), key=lambda e: e.priority
        ):
            assert not isinstance(entry.item, _PQRemoved)
            yield entry.item


def transpose[T](rows: Sequence[Sequence[T]]) -> list[list[T]]:
    """
    Transposes a sequence of sequences, returning one row per column of input.

    ABCD
    EFGH
    IJKL

    turns into

    AEI
    BFJ
    CGK
    DHL

    Assumes all input rows are of equal length.
    """
    return [[row[column_index] for row in rows] for column_index in range(len(rows[0]))]


def rotate_clockwise[T](rows: Sequence[Sequence[T]]) -> list[list[T]]:
    """
    Rotates a sequence of sequences, returning one row per column of input.

    ABCD
    EFGH
    IJKL

    turns into

    IEA
    JFB
    KGC
    LHD

    Assumes all input rows are of equal length.
    """
    return [row[::-1] for row in transpose(rows)]


def rotate_anticlockwise[T](rows: Sequence[Sequence[T]]) -> list[list[T]]:
    """
    Rotates a sequence of sequences, returning one row per column of input.

    ABCD
    EFGH
    IJKL

    turns into

    DHL
    CGK
    BFJ
    AEI

    Assumes all input rows are of equal length.
    """
    return transpose(rows)[::-1]
