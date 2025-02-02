from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from _typeshed import SupportsRichComparisonT

NullableComparable = typing.Optional["SupportsRichComparisonT"]


class CmpFn(typing.Protocol):
    def __call__(
        self, *args: NullableComparable[typing.Any]
    ) -> NullableComparable[typing.Any]: ...


def safe_min(*args: NullableComparable[typing.Any]) -> NullableComparable[typing.Any]:
    filtered = [arg for arg in args if arg is not None]
    if not filtered:
        return None
    return min(filtered)


def safe_max(*args: NullableComparable[typing.Any]) -> NullableComparable[typing.Any]:
    filtered = [arg for arg in args if arg is not None]
    if not filtered:
        return None
    return max(filtered)
