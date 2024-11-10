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
    i = PositiveInt(1.0)
    assert isinstance(i, PositiveInt)


def test_init_from_negative_float_raises():
    with pytest.raises(ValueError):
        PositiveInt(-1.0)


def test_init_from_0_float_succeeds():
    i = PositiveInt(0.0)
    assert isinstance(i, PositiveInt)


def test_init_from_non_integer_float_floors():
    i = PositiveInt(1.9)
    assert i == 1


def test_init_non_integer_float_with_floor_disabled_raises():
    with pytest.raises(ValueError):
        PositiveInt(1.9, floor=False)


def test_eq_to_int():
    i = PositiveInt(1)
    assert i == 1


def test_eq_to_valid_float():
    i = PositiveInt(1)
    assert i == 1.0


def test_eq_to_invalid_float():
    i = PositiveInt(1)
    assert i != 1.5


def test_eq_to_invalid_type_not_implemented():
    i = PositiveInt(1)
    assert i != "1"


def test_eq_to_postive_int_true():
    i = PositiveInt(1)
    j = PositiveInt(1)
    assert i == j


def test_eq_to_positive_int_false():
    i = PositiveInt(1)
    j = PositiveInt(2)
    assert i != j
