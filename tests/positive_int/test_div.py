from sensible_types import PositiveInt


def test_pos_int_div_pos_int_returns_float():
    a = PositiveInt(6)
    b = PositiveInt(2)
    res = a / b
    assert isinstance(res, float)
    assert res == 3.0
