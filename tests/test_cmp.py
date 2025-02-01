import pytest

from aoc.utils.cmp import safe_max, safe_min


@pytest.mark.parametrize(
    ["values", "expected"],
    [((1, 2, 3), 3), ((1, None, 3), 3), ((), None), ((None, None), None)],
)
def test_safe_max(values, expected):
    assert safe_max(*values) == expected


@pytest.mark.parametrize(
    ["values", "expected"],
    [((1, 2, 3), 1), ((1, None, 3), 1), ((), None), ((None, None), None)],
)
def test_safe_min(values, expected):
    assert safe_min(*values) == expected
