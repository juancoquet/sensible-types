import pytest

from sensible_types import PositiveInt


def test_pos_int_mod_pos_int_returns_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a % b
    assert isinstance(res, int)
    assert res == 1


def test_pos_int_mod_int_returns_int():
    a = PositiveInt(5)
    b = 2
    res = a % b
    assert isinstance(res, int)
    assert res == 1


def test_int_mod_pos_int_returns_int():
    a = 5
    b = PositiveInt(2)
    res = a % b
    assert isinstance(res, int)
    assert res == 1


def test_pos_int_mod_float_returns_int():
    a = PositiveInt(6)
    b = 2.5
    res = a % b
    assert isinstance(res, int)
    assert res == 1


def test_float_mod_pos_int_returns_int():
    a = 5.0
    b = PositiveInt(2)
    res = a % b
    assert isinstance(res, int)
    assert res == 1


def test_pos_int_mod_invalid_type_raises():
    a = PositiveInt(5)
    b = "2"
    with pytest.raises(TypeError):
        a % b  # type: ignore


def test_invalid_type_mod_pos_int_raises():
    a = "5"
    b = PositiveInt(2)
    with pytest.raises(TypeError):
        a % b  # type: ignore


def test_pos_int_imod_pos_int_returns_pos_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    a %= b
    assert isinstance(a, PositiveInt)
    assert a == 1


def test_pos_int_imod_int_raises():
    a = PositiveInt(5)
    b = -2
    with pytest.raises(TypeError):
        a %= b


def test_int_imod_pos_int_returns_int():
    a = 5
    b = PositiveInt(2)
    a %= b
    assert isinstance(a, int)
    assert a == 1


def test_pos_int_imod_float_raises():
    a = PositiveInt(5)
    b = -2.0
    with pytest.raises(TypeError):
        a %= b


def test_float_imod_pos_int_returns_int():
    a = 5.0
    b = PositiveInt(2)
    a %= b
    assert isinstance(a, int)
    assert a == 1


def test_pos_int_imod_invalid_type_raises():
    a = PositiveInt(5)
    b = "2"
    with pytest.raises(TypeError):
        a %= b  # type: ignore
