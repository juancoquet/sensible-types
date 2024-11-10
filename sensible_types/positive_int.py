from typing import List, Self, Sequence, Tuple, TypeVar, Union, overload

T = TypeVar("T")
IF = TypeVar("IF", int, float)
IFP = TypeVar("IFP", int, float, "PositiveInt")
IFPS = TypeVar("IFPS", int, float, "PositiveInt", Sequence)


class PositiveInt:
    def __init__(self, value: Union[int, float], floor: bool = True):
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

    # TODO:
    # truediv
    # itruediv
    # rtruediv
    # floordiv
    # ifloordiv
    # rfloordiv
    # lt
    # gt
    # lte
    # gte
    # for i in range(PostiveInt)

    def __add__(self, other: IFP) -> IFP:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        if isinstance(other, PositiveInt):
            return PositiveInt(self.__value + other.__value)
        return self.__value + other

    def __radd__(self, other: IF) -> IF:
        return other + self.__value

    def __iadd__(self, other: Union[int, float, Self]) -> Self:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        other_val = other.__value if isinstance(other, PositiveInt) else other
        if not other_val.is_integer():
            raise ValueError(
                "Cannot perform in-place addition on a PositiveInt if the added value is "
                f"not a whole number. Added value: {other_val}"
            )
        if self.__value + other_val < 0:
            raise ValueError(
                "Cannot perform in-place addition on a PositiveInt if the result would be a "
                "negative number. "
                f"PositiveInt value: {self.__value}, other value: {other_val}."
            )
        self.__value += other_val
        return self

    @overload
    def __sub__(self, other: int) -> int: ...
    @overload
    def __sub__(self, other: float) -> float: ...
    @overload
    def __sub__(self, other: Self) -> int: ...
    def __sub__(self, other: Union[int, float, Self]) -> Union[int, float]:
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        if isinstance(other, PositiveInt):
            return self.__value - other.__value
        return self.__value - other

    def __rsub__(self, other: IF) -> IF:
        return other - self.__value

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
                f"PositiveInt value: {self.__value}, other value: {other_val}."
            )
        self.__value -= int(other_val)
        return self

    @overload
    def __mul__(self, other: Self) -> Self: ...
    @overload
    def __mul__(self, other: int) -> int: ...
    @overload
    def __mul__(self, other: float) -> float: ...
    @overload
    def __mul__(self, other: str) -> str: ...
    @overload
    def __mul__(self, other: List[T]) -> List[T]: ...
    @overload
    def __mul__(self, other: Tuple[T]) -> Tuple[T]: ...
    def __mul__(self, other: IFPS) -> IFPS:
        if not isinstance(other, (int, float, PositiveInt, Sequence)):
            return NotImplemented
        if isinstance(other, PositiveInt):
            return PositiveInt(self.__value * other.__value)
        return self.__value * other  # type: ignore

    @overload
    def __rmul__(self, other: Self) -> Self: ...
    @overload
    def __rmul__(self, other: int) -> int: ...
    @overload
    def __rmul__(self, other: float) -> float: ...
    @overload
    def __rmul__(self, other: str) -> str: ...
    @overload
    def __rmul__(self, other: List[T]) -> List[T]: ...
    @overload
    def __rmul__(self, other: Tuple[T]) -> Tuple[T]: ...
    def __rmul__(self, other: IFPS) -> IFPS:
        return other * self.__value  # type: ignore

    def __imul__(self, other: Union[int, float, Self]) -> Self:
        if not isinstance(other, (int, float, PositiveInt)):
            raise TypeError(
                "Cannot perform in-pace multiplication between a PositiveInt and type: "
                f"{type(other)}"
            )
        other_val = other.__value if isinstance(other, PositiveInt) else other
        if self.__value * other_val < 0:
            raise ValueError(
                "Cannot perform in-place multiplication on a PositiveInt if the result would be "
                "negative number. "
                f"PositiveInt value: {self.__value}, other value: {other_val}."
            )
        self.__value *= int(other_val)
        return self

    def __truediv__(self, other: Self) -> float:
        return self.__value / other.__value
