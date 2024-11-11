import pytest

from sensible_types import PositiveInt


def test_pos_int_pow_pos_int_returns_pos_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a**b
    assert isinstance(res, PositiveInt)
    assert res == 25


def test_pos_int_pow_int_returns_int():
    a = PositiveInt(5)
    b = 2
    res = a**b
    assert isinstance(res, int)
    assert res == 25


def test_int_pow_pos_int_returns_int():
    a = 5
    b = PositiveInt(2)
    res = a**b
    assert isinstance(res, int)
    assert res == 25


def test_pos_int_pow_float_returns_float():
    a = PositiveInt(5)
    b = 2.0
    res = a**b
    assert isinstance(res, float)
    assert res == 25.0


def test_float_pow_pos_int_returns_float():
    a = 5.0
    b = PositiveInt(2)
    res = a**b
    assert isinstance(res, float)
    assert res == 25.0


def test_pos_int_pow_invalid_type_raises():
    a = PositiveInt(5)
    b = "2"
    with pytest.raises(TypeError):
        a**b  # type: ignore


def test_invalid_type_pow_pos_int_raies():
    a = "5"
    b = PositiveInt(2)
    with pytest.raises(TypeError):
        a**b  # type: ignore


def test_pos_int_ipow_pos_int_returns_pos_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    a **= b
    assert isinstance(a, PositiveInt)
    assert a == 25


def test_pos_int_ipow_valid_int_returns_pos_int():
    a = PositiveInt(5)
    b = 2
    a **= b
    assert isinstance(a, PositiveInt)
    assert a == 25


def test_pos_int_ipow_invalid_int_raises():
    a = PositiveInt(5)
    b = -2
    with pytest.raises(ValueError):
        a **= b


def test_pos_int_ipow_valid_float_returns_pos_int():
    a = PositiveInt(5)
    b = 2.0
    a **= b
    assert isinstance(a, PositiveInt)
    assert a == 25


def test_pos_int_ipow_invalid_float_raises():
    a = PositiveInt(5)
    b = 2.5
    with pytest.raises(ValueError):
        a **= b


def test_int_ipow_pos_int_returns_int():
    a = 5
    b = PositiveInt(2)
    a **= b
    assert isinstance(a, int)
    assert a == 25


def test_float_ipow_pos_int_returns_float():
    a = 5.0
    b = PositiveInt(2)
    a **= b
    assert isinstance(a, float)
    assert a == 25.0
