import itertools
import math
import os
import time
from functools import reduce, wraps
from operator import mul
from typing import Callable, Optional

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


def product(*args: TNum) -> TNum:
    return reduce(mul, args)


def magnitude(*args: TNum) -> float:
    return math.sqrt(sum(a ** 2 for a in args))


def manhattan(*args: int) -> int:
    return sum(abs(a) for a in args)


def triangle(n: int) -> int:
    return n * (n + 1) // 2


def timed(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        start = time.monotonic()
        ret = f(*args, **kwargs)
        print(f"Took {time.monotonic() - start} secs")
        return ret

    return decorated


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
