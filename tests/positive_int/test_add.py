import pytest

from sensible_types import PositiveInt


def test_add_to_positive_int_returns_positive_int():
    a = PositiveInt(1)
    b = PositiveInt(2)
    res = a + b
    assert isinstance(res, PositiveInt)
    assert res == PositiveInt(3)


def test_add_to_int_returns_int():
    a = PositiveInt(1)
    b = 2
    res = a + b
    assert isinstance(res, int)
    assert res == 3


def test_add_to_float_returns_float():
    a = PositiveInt(1)
    b = 2.0
    res = a + b
    assert isinstance(res, float)
    assert res == 3.0


def test_add_to_invalid_type_raises():
    a = PositiveInt(1)
    b = "2"
    with pytest.raises(TypeError):
        a + b  # type: ignore


def test_add_to_neg_int_returns_neg_int():
    a = PositiveInt(1)
    b = -2
    res = a + b
    assert isinstance(res, int)
    assert res == -1
def test_add_to_neg_float_returns_neg_float():
    a = PositiveInt(1)
    b = -2.0
    res = a + b
    assert isinstance(res, float)
    assert res == -1.0
