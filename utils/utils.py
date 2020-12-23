import os
import time
from functools import reduce, wraps
from operator import mul
from typing import Callable, List, Optional, Union

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
) -> Union[List[T], List[str]]:
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


def timed(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        start = time.monotonic()
        ret = f(*args, **kwargs)
        print(f"Took {time.monotonic() - start} secs")
        return ret

    return decorated
