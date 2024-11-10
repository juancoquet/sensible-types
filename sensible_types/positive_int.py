from typing import Self, TypeVar, Union, overload

T = TypeVar("T", int, float, "PositiveInt")


class PositiveInt:
    def __init__(self, value: int | float, floor: bool = True):
        """
        Create a new instance of `PostiveInt`.

        By default non-integer input values will be floored, much like how `int(1.5)` behaves. E.g.
        `PositiveInt(1.5) == 1  # True`.
        If you do not wish for the input `value` to be floored, passing `floor = False` will raise a
        `ValueError` if an invalid (non-integer) `value` is passed.

        Parameters:
        - `value: int | float` - The `value` to be converted into a `PositiveInt`. Must be >= 0.
        - `floor: bool` - Whether or not to perform a floor operation on the input `value`. Defaults
          to `True`.

        Raises:
        - `ValueError`:
          - If the input `value` is < 0.
          - If `floor` is `False` and the input `value` is not a whole number. Note that whole number
            `float` types such as `2.0` are valid.
        """

        if not isinstance(value, (int, float)):
            raise TypeError(
                f"PositiveInt can only be created from `int` and `float`. Type passed: {type(value)}"
            )
        if value < 0:
            raise ValueError(
                f"A PositiveInt cannot be created from a number < 0. Value passed: {value}."
            )
        if not floor and not value.is_integer():
            raise ValueError(
                f"Expected a whole number to be passed. Given: {value}."
                "Use `floor=True` to perform a `math.floor` operation on input values."
            )
        if value == float("inf") or value == float("-inf"):
            raise ValueError("PositiveInt cannot be created from Infinity.")
        self.__value = int(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        return self.__value == other

    # TODO: sub, mul, div, iadd, isub, imul, idiv lt, gt, lte, gte, for i in range(PostiveInt)

    def __add__(self, other: T) -> T:
        # TODO: int/float + PositiveInt
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        if isinstance(other, PositiveInt):
            return PositiveInt(self.__value + other.__value)
        return self.__value + other

    def __iadd__(self, other: Self) -> Self:
        # TODO: relax
        if not isinstance(other, PositiveInt):
            raise TypeError(
                "PositiveInt in-place addition is only supported with another PositiveInt. "
                f"Type passed: {type(other)}"
            )
        self.__value += other.__value
        return self

    # TODO: radd

    @overload
    def __sub__(self, other: int) -> int: ...
    @overload
    def __sub__(self, other: float) -> float: ...
    @overload
    def __sub__(self, other: Self) -> int: ...

    def __sub__(self, other: T) -> Union[int, float]:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        if isinstance(other, PositiveInt):
            return self.__value - other.__value
        return self.__value - other

    def __isub__(self, other: Union[int, float, Self]) -> Self:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        other_val = other.__value if isinstance(other, PositiveInt) else other
        if not other_val.is_integer():
            raise ValueError(
                "Cannot perform in-place subtraction on a PositiveInt if the subtracted value is "
                f"not a whole number. Subtracted value: {other_val}"
            )
        if other_val > self.__value:
            raise ValueError(
                "Cannot perform in-place subtraction on a PositiveInt if the result would be a "
                "negative number. "
                f"PositiveInt value: {self.__value} subtracted value: {other_val}."
            )
        self.__value -= other_val
        return self

    # TODO: rsub
