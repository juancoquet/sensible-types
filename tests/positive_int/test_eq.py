from sensible_types import PositiveInt


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
