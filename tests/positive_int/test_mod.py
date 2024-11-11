from sensible_types import PositiveInt


def test_pos_int_mod_pos_int_returns_int():
    a = PositiveInt(5)
    b = PositiveInt(2)
    res = a % b
    assert isinstance(res, int)
    assert res == 1
