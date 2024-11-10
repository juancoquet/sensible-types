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


def test_init_from_infinity_raises():
    with pytest.raises(ValueError):
        PositiveInt(float("inf"))


def test_init_from_neg_infinity_raises():
    with pytest.raises(ValueError):
        PositiveInt(float("-inf"))


def test_init_from_invalid_type_raises():
    with pytest.raises(TypeError):
        PositiveInt("1")  # type: ignore
