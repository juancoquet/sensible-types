from sensible_types import PositiveInt


def test_range_operation():
    times = PositiveInt(10)
    sum = 0
    for _ in range(times):
        sum += 1
    assert sum == times
