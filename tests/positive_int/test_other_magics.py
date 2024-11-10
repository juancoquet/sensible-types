from sensible_types import PositiveInt


def test_range_operation():
    times = PositiveInt(10)
    sum = 0
    for _ in range(times):
        sum += 1
    assert sum == times


def test_sequence_indexing():
    some_list = [1, 2, 3]
    a = PositiveInt(0)
    assert some_list[a] == 1

def test_hash():
    a = PositiveInt(1)
    b = PositiveInt(2)
    s = {a, b}
    assert s == {1, 2}
