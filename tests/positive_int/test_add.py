import pytest

from sensible_types import PositiveInt


def test_add_pos_int_to_pos_int_returns_pos_int():
    a = PositiveInt(1)
    b = PositiveInt(2)
    res = a + b
    assert isinstance(res, PositiveInt)
    assert res == PositiveInt(3)


def test_add_int_to_pos_int_returns_int():
    a = PositiveInt(1)
    b = 2
    res = a + b
    assert isinstance(res, int)
    assert res == 3


def test_add_pos_int_to_int_returns_int():
    a = PositiveInt(1)
    b = 2
    res = b + a
    assert isinstance(res, int)
    assert res == 3


def test_add_pos_int_to_neg_int_returns_neg_int():
    a = PositiveInt(1)
    b = -2
    res = b + a
    assert isinstance(res, int)
    assert res == -1


def test_add_pos_int_to_float_returns_float():
    a = PositiveInt(1)
    b = 2.0
    res = b + a
    assert isinstance(res, float)
    assert res == 3.0


def test_add_float_to_pos_int_returns_float():
    a = PositiveInt(1)
    b = 2.0
    res = a + b
    assert isinstance(res, float)
    assert res == 3.0


def test_add_invalid_type_to_pos_int_raises():
    a = PositiveInt(1)
    b = "2"
    with pytest.raises(TypeError):
        a + b  # type: ignore


def test_add_neg_int_to_pos_int_returns_neg_int():
    a = PositiveInt(1)
    b = -2
    res = a + b
    assert isinstance(res, int)
    assert res == -1


def test_add_neg_float_to_pos_int_returns_neg_float():
    a = PositiveInt(1)
    b = -2.0
    res = a + b
    assert isinstance(res, float)
    assert res == -1.0


def test_iadd_pos_int_succeeds():
    a = PositiveInt(1)
    a += PositiveInt(2)
    assert isinstance(a, PositiveInt)
    assert a == 3


def test_iadd_int_raises():
    a = PositiveInt(1)
    with pytest.raises(TypeError):
        a += 2


def test_iadd_float_raises():
    a = PositiveInt(1)
    with pytest.raises(TypeError):
        a += 2.0


# def test_iadd_pos_int_to_int_returns_int():
#     a = 1
#     b = PositiveInt(2)
#     a += b
