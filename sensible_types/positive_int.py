class PositiveInt:
    def __init__(self, value: int | float):
        if value < 0:
            raise ValueError(
                f"A PositiveInt cannot be created from a number < 0. Value passed: {value}."
            )
        self.__value = int(value)

    def __eq__(self, other: object):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return self.__value == other
