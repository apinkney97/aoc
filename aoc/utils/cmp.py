from typing import Callable, Optional

from aoc.utils.types import TNum


def _safe_cmp(
    *args: Optional[TNum], cmp_fn: Callable[[TNum, TNum], TNum]
) -> Optional[TNum]:
    val = None
    for arg in args:
        if arg is None:
            continue
        if val is None:
            val = arg
        else:
            val = cmp_fn(val, arg)
    return val


def safe_min(*args: Optional[TNum]) -> Optional[TNum]:
    return _safe_cmp(*args, cmp_fn=min)


def safe_max(*args: Optional[TNum]) -> Optional[TNum]:
    return _safe_cmp(*args, cmp_fn=max)
