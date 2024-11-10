class PositiveInt:
    def __init__(self, value: int | float, floor: bool = True):
        if value < 0:
            raise ValueError(
                f"A PositiveInt cannot be created from a number < 0. Value passed: {value}."
            )
        if not floor and not value.is_integer():
            raise ValueError(
                f"Expected a whole number to be passed. Given: {value}."
                "Use `floor=True` to perform a `math.floor` operation on input values."
            )
        self.__value = int(value)

    def __eq__(self, other: object):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return self.__value == other
