import pytest
from sensible_types import PositiveInt


def test_pos_int_truediv_valid_pos_int_returns_float():
    a = PositiveInt(6)
    b = PositiveInt(2)
    res = a / b
    assert isinstance(res, float)
    assert res == 3.0


def test_pos_int_truediv_int_returns_float():
    a = PositiveInt(6)
    b = 2
    res = a / b
    assert isinstance(res, float)
    assert res == 3.0


def test_int_truediv_pos_int_returns_float():
    a = PositiveInt(2)
    b = 6
    res = b / a
    assert isinstance(res, float)
    assert res == 3.0


def test_pos_int_truediv_float_returns_float():
    a = PositiveInt(6)
    b = 2.0
    res = a / b
    assert isinstance(res, float)
    assert res == 3.0


def test_float_truediv_pos_int_returns_float():
    a = PositiveInt(2)
    b = 6.0
    res = b / a
    assert isinstance(res, float)
    assert res == 3.0


def test_pos_int_truediv_invalid_type_raises():
    a = PositiveInt(6)
    b = "2.0"
    with pytest.raises(TypeError):
        a / b  # type: ignore


def test_invaid_type_truediv_pos_int_raises():
    a = PositiveInt(6)
    b = "2.0"
    with pytest.raises(TypeError):
        b / a  # type: ignore


def test_pos_int_itruediv_pos_int_raises():
    a = PositiveInt(6)
    b = PositiveInt(2)
    with pytest.raises(TypeError):
        a /= b  # type: ignore


def test_pos_int_floordiv_pos_int_returns_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a // b
    assert isinstance(res, int)
    assert res == 2


def test_pos_int_floordiv_int_returns_int():
    a = PositiveInt(5)
    b = 2
    res = a // b
    assert isinstance(res, int)
    assert res == 2


def test_pos_int_floordiv_float_returns_int():
    a = PositiveInt(5)
    b = 2.0
    res = a // b
    assert isinstance(res, int)
    assert res == 2

def test_pos_int_floordiv_invalid_type_raises():
    a = PositiveInt(5)
    b = "3.0"
    with pytest.raises(TypeError):
        a // b  # type: ignore
