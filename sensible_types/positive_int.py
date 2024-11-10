class PositiveInt:
    def __init__(self, value: int | float):
        if value < 0:
            raise ValueError(
                f"A PositiveInt cannot be created from a number < 0. Value passed: {value}."
            )
        self.__value = value
