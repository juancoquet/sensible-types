import pytest

from sensible_types import PositiveInt


def test_pos_int_mul_pos_int_returns_pos_int():
    a = PositiveInt(2)
    b = PositiveInt(3)
    res = a * b
    assert isinstance(res, PositiveInt)
    assert res == 6


def test_pos_int_mul_int_returns_int():
    a = PositiveInt(2)
    b = 3
    res = a * b
    assert isinstance(res, int)
    assert res == 6


def test_pos_int_mul_float_returns_float():
    a = PositiveInt(2)
    b = 3.0
    res = a * b
    assert isinstance(res, float)
    assert res == 6.0
