import pytest

from sensible_types import PositiveInt


def test_add_to_positive_int_returns_positive_int():
    a = PositiveInt(1)
    b = PositiveInt(2)
    res = a + b
    assert isinstance(res, PositiveInt)
    assert res == PositiveInt(3)
