from __future__ import annotations

import enum
import heapq
import itertools
from dataclasses import dataclass
from typing import Iterator


class PQUpdates(enum.Enum):
    ANY = enum.auto()
    NONE = enum.auto()
    GREATER = enum.auto()
    LESSER = enum.auto()


class _Removed:
    pass


@dataclass
class _Entry[T]:
    priority: int
    count: int
    item: T | _Removed

    def _sort_key(self) -> tuple[int, int]:
        return self.priority, self.count

    def __lt__(self, other: _Entry[T]) -> bool:
        return self._sort_key() < other._sort_key()


class PQ[T]:
    """Heavily "borrowed" from
    https://docs.python.org/3/library/heapq.html?highlight=heapq#priority-queue-implementation-notes
    """

    def __init__(
        self, max_heap: bool = False, allow_updates: PQUpdates = PQUpdates.ANY
    ):
        self._pq: list[_Entry[T]] = []  # list of entries arranged in a heap
        self._entry_finder: dict[T, _Entry[T]] = {}  # mapping of each item to its entry
        self._counter = itertools.count()  # unique sequence count
        self._max_heap = max_heap
        self._allow_updates = allow_updates

    def add_item(self, item: T, priority: float | int = 0) -> None:
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
        entry = _Entry(priority, count, item)
        self._entry_finder[item] = entry
        heapq.heappush(self._pq, entry)

    def remove_item(self, item: T) -> None:
        """Mark an existing item as removed.  Raise KeyError if not found."""
        entry = self._entry_finder.pop(item)
        entry.item = _Removed()

    def pop_item(self) -> T:
        """Remove and return the lowest priority item. Raise KeyError if empty."""
        while self._pq:
            item = heapq.heappop(self._pq).item
            if not isinstance(item, _Removed):
                self._entry_finder.pop(item)
                return item
        raise KeyError("pop from an empty priority queue")

    def peek(self) -> T:
        """Show the item with the lowest priority, but do not remove it. Raise KeyError if empty."""
        while self._pq:
            item = self._pq[0].item
            if not isinstance(item, _Removed):
                return item
            heapq.heappop(self._pq)

        raise KeyError("peek at empty priority queue")

    def __len__(self) -> int:
        return len(self._entry_finder)

    def __repr__(self) -> str:
        return f"PQ({list(self)})"

    def __iter__(self) -> Iterator[T]:
        for entry in sorted(self._entry_finder.values(), key=lambda e: e.priority):
            assert not isinstance(entry.item, _Removed)
            yield entry.item
