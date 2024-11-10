from sensible_types import PositiveInt


def test_eq_to_int():
    a = PositiveInt(1)
    assert a == 1


def test_eq_to_valid_float():
    a = PositiveInt(1)
    assert a == 1.0


def test_eq_to_invalid_float():
    a = PositiveInt(1)
    assert a != 1.5


def test_eq_to_invalid_type_not_implemented():
    a = PositiveInt(1)
    assert a != "1"


def test_eq_to_postive_int_true():
    a = PositiveInt(1)
    b = PositiveInt(1)
    assert a == b


def test_eq_to_positive_int_false():
    a = PositiveInt(1)
    b = PositiveInt(2)
    assert a != b


def test_gt_positive_int():
    a = PositiveInt(2)
    b = PositiveInt(1)
    assert a > b

def test_lt_positive_int():
    a = PositiveInt(2)
    b = PositiveInt(1)
    assert b < a
