import pytest

from sensible_types import PositiveInt


def test_pos_int_sub_pos_int_returns_int():
    a = PositiveInt(1)
    b = PositiveInt(2)
    res = b - a
    assert isinstance(res, int)
    assert res == 1
    res = a - b
    assert isinstance(res, int)
    assert res == -1


def test_pos_int_sub_int_returns_int():
    a = PositiveInt(2)
    b = 1
    res = a - b
    assert isinstance(res, int)
    assert res == 1
    a = PositiveInt(1)
    b = 2
    res = a - b
    assert isinstance(res, int)
    assert res == -1


def test_pos_int_sub_float_returns_float():
    a = PositiveInt(2)
    b = 1.0
    res = a - b
    assert isinstance(res, float)
    assert res == 1.0
    a = PositiveInt(1)
    b = 2.0
    res = a - b
    assert isinstance(res, float)
    assert res == -1.0


def test_pos_int_sub_invalid_type_raises():
    a = PositiveInt(2)
    b = "1"
    with pytest.raises(TypeError):
        a - b  # type: ignore


def test_isub_pos_int_that_would_cause_neg_value_raises():
    a = PositiveInt(1)
    b = PositiveInt(2)
    with pytest.raises(ValueError):
        a -= b


# TODO: int/float - PositiveInt
