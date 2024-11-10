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

    def __eq__(self, other: object):
        if not isinstance(other, (int, float, PositiveInt)):
            return NotImplemented
        return self.__value == other
