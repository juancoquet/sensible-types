import pytest

from sensible_types import PositiveInt


def test_init_from_int_gt_0_succeeds():
    i = PositiveInt(1)
    assert isinstance(i, PositiveInt)


def test_init_from_int_0_succeeds():
    i = PositiveInt(0)
    assert isinstance(i, PositiveInt)


def test_init_from_negative_int_raises():
    with pytest.raises(ValueError):
        PositiveInt(-1)


def test_init_from_float_whole_number_gt_0_succeeds():
    i = PositiveInt(2.0)
    assert isinstance(i, PositiveInt)


def test_init_from_non_integer_float_floors():
    i = PositiveInt(1.9)
    assert i == 1


def test_eq_to_int():
    i = PositiveInt(1)
    assert i == 1


def test_eq_to_valid_float():
    i = PositiveInt(1)
    assert i == 1.0


def test_eq_to_invalid_float():
    i = PositiveInt(1)
    assert not i == 1.5


def test_eq_to_invalid_type_not_implemented():
    i = PositiveInt(1)
    assert not i == "1"
