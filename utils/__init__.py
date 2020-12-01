import os
from typing import Callable, List, Optional, TypeVar, Union

T = TypeVar("T")


def load_data(
    day: int, strip: bool = True, fn: Optional[Callable[[str], T]] = None
) -> Union[List[T], List[str]]:
    with open(os.path.join("data", f"day{day:02d}.data")) as f:
        data = f.readlines()
        if strip:
            data = [line.strip() for line in data]
        if fn is not None:
            data = [fn(line) for line in data]
        return data


def _safe_cmp(*args, cmp_fn):
    val = None
    for arg in args:
        if arg is None:
            continue
        if val is None:
            val = arg
        else:
            val = cmp_fn(val, arg)
    return val


def safe_min(*args):
    return _safe_cmp(*args, cmp_fn=min)


def safe_max(*args):
    return _safe_cmp(*args, cmp_fn=max)
