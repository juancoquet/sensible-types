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
