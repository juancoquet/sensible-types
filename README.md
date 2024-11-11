# Sensible Types
A collection of useful types for Python, to drive correctness in your programs.

## Installation

```
pip3 install sensible-types  # with pip
poetry add sensible-types    # with poetry
uv add sensible-types        # with uv
```

[View on PyPI.](https://pypi.org/project/sensible-types/)

## Why?

> Parse, don't validate.

How many times have you written code of this nature?

```python3
def foo(a: int):
    if a < 0:
        raise ValueError(f"The input `a` should be positive. Actual value: {a}")

    # actual logic
    ...
```

The requirement for input validation indicates an error in your type system.

It _should not be possible_ to pass a negative `int` to a function that can only work with a positive `int` — that is an invalid state that your program should never find itself in.

Unfortunately, Python doesn't make this easy. We should ideally be able to do something like this:

```python3
def foo(a: uint):
    # straight into the logic, as the input comes pre-validated
    ...
```

But of course, Python does not have an unsigned integer type.

[Type-driven design](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) leads to more correct, reliable software, where tests only have to focus on verifying that your business logic works rather than verifying that your inputs are valid. To borrow a phrase from Rust 🦀, it makes invalid states unrepresentable.

This package aims to provide new primitive types with additional constraints that are commonly required.

For now, it only contains `PositiveInt`, but it may be extended in the future as new use cases arise.

## But Python doesn't care about types at runtime

You're right.

But that doesn't mean that _you_, the developer, should not care about the correctness and reliability of your program.

You should be using strict type checking tools like [Pyright](https://github.com/microsoft/pyright) to analyse your code. Without such tools, all the type-driven design in the world won't save you from Python.

There still won't be anything stopping your program from running if you pass in an incorrect type, but at least you'll see errors in you IDE if you've written incorrect code.
