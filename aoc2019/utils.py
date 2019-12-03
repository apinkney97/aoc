import os
from typing import List


def load_data(day: int, strip: bool = True) -> List[str]:
    with open(os.path.join("data", f"day{day:02d}.data")) as f:
        if strip:
            return [l.strip() for l in f.readlines()]
        return f.readlines()


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
