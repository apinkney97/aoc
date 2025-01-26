from collections import deque
from typing import Deque, Dict, Generic, Iterable

from aoc.utils.types import T


class SetDeque(Generic[T]):
    def __init__(self, iterable: Iterable[T] | None = None):
        self._dict: Dict[T, int] = {}
        self._deque: Deque[T] = deque()
        if iterable is not None:
            self.extend(iterable)

    def __add_to_dict(self, item: T) -> None:
        try:
            self._dict[item] += 1
        except KeyError:
            self._dict[item] = 1

    def __remove_from_dict(self, item: T) -> None:
        if self._dict[item] == 1:
            self._dict.pop(item)
        else:
            self._dict[item] -= 1

    def __contains__(self, item: T) -> bool:
        return item in self._dict

    def __len__(self) -> int:
        return len(self._deque)

    def append(self, item: T) -> None:
        self.__add_to_dict(item)
        self._deque.append(item)

    def appendleft(self, item: T) -> None:
        self.__add_to_dict(item)
        self._deque.appendleft(item)

    def pop(self) -> T:
        item = self._deque.pop()
        self.__remove_from_dict(item)
        return item

    def popleft(self) -> T:
        item = self._deque.popleft()
        self.__remove_from_dict(item)
        return item

    def extend(self, iterable: Iterable[T]) -> None:
        for item in iterable:
            self.append(item)

    def extendleft(self, iterable: Iterable[T]) -> None:
        for item in iterable:
            self.appendleft(item)

    def rotate(self, n: int) -> None:
        self._deque.rotate(n)
