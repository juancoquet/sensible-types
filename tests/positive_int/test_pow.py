import pytest

from sensible_types import PositiveInt

def test_pos_int_pow_pos_int_returns_pos_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a ** b
    assert isinstance(res, PositiveInt)
    assert res == 25


def test_pos_int_pow_int_returns_int():
    a = PositiveInt(5)
    b = 2
    res = a ** b
    assert isinstance(res, int)
    assert res == 25


def test_pos_int_pow_float_returns_float():
    a = PositiveInt(5)
    b = 2.0
    res = a ** b
    assert isinstance(res, float)
    assert res == 25.0


def test_pos_int_pow_invalid_type_raises():
    a = PositiveInt(5)
    b = "2"
    with pytest.raises(TypeError):
        a ** b  # type: ignore
