import pytest
from sensible_types import PositiveInt


def test_pos_int_truediv_pos_int_returns_float():
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


def test_pos_int_itrue_div_int_raises():
    a = PositiveInt(6)
    b = 2
    with pytest.raises(TypeError):
        a /= b  # type: ignore


def test_int_itruediv_pos_int_returns_float():
    a = 5
    b = PositiveInt(2)
    a /= b
    assert isinstance(a, float)
    assert a == 2.5


def test_float_itruediv_pos_int_returns_float():
    a = 5.0
    b = PositiveInt(2)
    a /= b
    assert isinstance(a, float)
    assert a == 2.5


def test_pos_int_floordiv_pos_int_returns_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a // b
    assert isinstance(res, PositiveInt)
    assert res == 2


def test_pos_int_floordiv_int_returns_int():
    a = PositiveInt(5)
    b = 2
    res = a // b
    assert isinstance(res, int)
    assert res == 2


def test_int_floordiv_pos_int_returns_int():
    a = PositiveInt(2)
    b = 5
    res = b // a
    assert isinstance(res, int)
    assert res == 2


def test_pos_int_floordiv_float_returns_int():
    a = PositiveInt(5)
    b = 2.0
    res = a // b
    assert isinstance(res, int)
    assert res == 2


def test_float_floordiv_pos_int_returns_int():
    a = PositiveInt(2)
    b = 5.0
    res = b // a
    assert isinstance(res, int)
    assert res == 2


def test_pos_int_floordiv_invalid_type_raises():
    a = PositiveInt(5)
    b = "3.0"
    with pytest.raises(TypeError):
        a // b  # type: ignore


def test_invalid_type_floordiv_posint_raises():
    a = PositiveInt(5)
    b = "3.0"
    with pytest.raises(TypeError):
        b // a  # type: ignore


def test_pos_int_ifloordiv_pos_int_returns_pos_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    a //= b
    assert isinstance(a, PositiveInt)
    assert a == 2
    c = PositiveInt(5)
    d = PositiveInt(6)
    c //= d
    assert isinstance(c, PositiveInt)
    assert c == 0


def test_pos_int_ifloordiv_valid_int_returns_pos_int():
    a = PositiveInt(5)
    b = 2
    a //= b
    assert isinstance(a, PositiveInt)
    assert a == 2


def test_int_ifloordiv_pos_int_returns_int():
    a = 5
    b = PositiveInt(2)
    a //= b
    assert isinstance(a, int)
    assert a == 2


def test_float_ifloordiv_pos_int_returns_int():
    a = 5.0
    b = PositiveInt(2)
    a //= b
    assert isinstance(a, int)
    assert a == 2


def test_pos_int_ifloordiv_invalid_int_raises():
    a = PositiveInt(5)
    b = -2
    with pytest.raises(ValueError):
        a //= b


def test_pos_int_ifloordiv_valid_float_returns_pos_int():
    a = PositiveInt(5)
    b = 2.0
    a //= b
    assert isinstance(a, PositiveInt)
    assert a == 2


def test_pos_int_ifloordiv_invalid_float_raises():
    a = PositiveInt(5)
    b = -2.0
    with pytest.raises(ValueError):
        a //= b
