import math
import time
from collections.abc import Sequence
from contextlib import ContextDecorator
from datetime import timedelta
from functools import reduce
from operator import mul
from types import TracebackType
from typing import Any, Iterable

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
