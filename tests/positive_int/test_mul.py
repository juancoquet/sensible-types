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


def test_int_mul_pos_int_returns_int():
    a = PositiveInt(2)
    b = 3
    res = b * a
    assert isinstance(res, int)
    assert res == 6


def test_pos_int_mul_neg_int_returns_neg_int():
    a = PositiveInt(2)
    b = -3
    res = a * b
    assert isinstance(res, int)
    assert res == -6


def test_pos_int_mul_float_returns_float():
    a = PositiveInt(2)
    b = 3.0
    res = a * b
    assert isinstance(res, float)
    assert res == 6.0


def test_float_mul_pos_int_returns_float():
    a = PositiveInt(2)
    b = 3.0
    res = b * a
    assert isinstance(res, float)
    assert res == 6.0


def test_pos_int_mul_neg_float_returns_neg_float():
    a = PositiveInt(2)
    b = -3.0
    res = a * b
    assert isinstance(res, float)
    assert res == -6.0


def test_pos_int_mul_str_returns_str():
    a = PositiveInt(2)
    b = "3"
    res = a * b
    assert isinstance(res, str)
    assert res == "33"


def test_str_mul_pos_int_returns_str():
    a = PositiveInt(2)
    b = "3"
    res = b * a
    assert isinstance(res, str)
    assert res == "33"


def test_pos_int_mul_list_returns_repeated_list():
    a = PositiveInt(2)
    b = ["3"]
    res = a * b
    assert res == ["3", "3"]


def test_typle_mul_pos_int_returns_repeated_tuple():
    a = PositiveInt(2)
    b = ("3",)
    res = b * a
    assert res == ("3", "3")


def test_pos_int_mul_invalid_type_raises():
    a = PositiveInt(2)
    b = {}
    with pytest.raises(TypeError):
        a * b  # type: ignore


def test_pos_int_imul_pos_int_returns_pos_int():
    a = PositiveInt(2)
    b = PositiveInt(3)
    a *= b
    assert isinstance(a, PositiveInt)
    assert a == 6


def test_pos_int_imul_valid_int_returns_pos_int():
    a = PositiveInt(2)
    b = 3
    a *= b
    assert isinstance(a, PositiveInt)
    assert a == 6


def test_pos_int_imul_neg_int_raises():
    a = PositiveInt(2)
    b = -3
    with pytest.raises(ValueError):
        a *= b


def test_pos_int_imul_valid_float_returns_pos_int():
    a = PositiveInt(2)
    b = 3.0
    a *= b
    assert isinstance(a, PositiveInt)
    assert a == 6.0


def test_pos_int_imul_neg_float_raises():
    a = PositiveInt(2)
    b = -3.0
    with pytest.raises(ValueError):
        a *= b


def test_pos_int_imul_str_raises():
    a = PositiveInt(2)
    b = "3"
    with pytest.raises(TypeError):
        a *= b


def test_pos_int_imul_list_raises():
    a = PositiveInt(2)
    b = ["3"]
    with pytest.raises(TypeError):
        a *= b


def test_pos_int_imul_tuple_raises():
    a = PositiveInt(2)
    b = ("3",)
    with pytest.raises(TypeError):
        a *= b
