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


def test_isub_valid_pos_int_succeeds():
    a = PositiveInt(2)
    b = PositiveInt(1)
    a -= b
    assert isinstance(a, PositiveInt)
    assert a == 1


def test_isub_valid_int_succeeds():
    a = PositiveInt(2)
    b = 1
    a -= b
    assert isinstance(a, PositiveInt)
    assert a == 1


def test_isub_valid_float_succeeds():
    a = PositiveInt(2)
    b = 1.0
    a -= b
    assert isinstance(a, PositiveInt)
    assert a == 1


def test_isub_to_0_succeeds():
    a = PositiveInt(1)
    a -= 1
    assert isinstance(a, PositiveInt)
    assert a == 0


def test_isub_invalid_float_raises():
    a = PositiveInt(2)
    b = 1.5
    with pytest.raises(ValueError):
        a -= b


def test_isub_pos_int_that_would_cause_neg_value_raises():
    a = PositiveInt(1)
    b = PositiveInt(2)
    with pytest.raises(ValueError):
        a -= b


def test_isub_int_that_would_cause_neg_value_raises():
    a = PositiveInt(1)
    b = 2
    with pytest.raises(ValueError):
        a -= b


def test_isub_float_that_would_cause_neg_value_raises():
    a = PositiveInt(1)
    b = 2.0
    with pytest.raises(ValueError):
        a -= b


def test_isub_invalid_type_raises():
    a = PositiveInt(1)
    b = "1"
    with pytest.raises(TypeError):
        a -= b  # type: ignore


def test_rsub_float_succeeds():
    a = 1.0
    b = PositiveInt(2)
    res = a - b
    assert isinstance(res, float)
    assert res == -1.0


def test_rsub_int_succeeds():
    a = 1
    b = PositiveInt(2)
    res = a - b
    assert isinstance(res, int)
    assert res == -1
