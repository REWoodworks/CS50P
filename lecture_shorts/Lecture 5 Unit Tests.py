# %% [markdown]
# <!-- calculator0.py -->
#
# Defines `main` and a `square` function that returns `n * n`, then calls `main()` unconditionally at the bottom. This is the first example, so there is no earlier block to compare it with.

# %%
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()


# %% [markdown]
# <!-- calculator1.py -->
#
# Guards the call to `main()` with `if __name__ == "__main__"` so the file can be imported by a test without prompting for input. Compared with the previous block, `square` is now safely importable elsewhere.

# %%
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator1.py -->
#
# Introduces a separate test file that imports `square` from `calculator1` and checks results with `if` statements, printing a message on failure. This starts the testing topic: code that verifies other code.

# %%
from ref_calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- calculator2.py -->
#
# Identical to `calculator1.py`; it exists as the module imported by the next test file.

# %%
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator2.py -->
#
# Replaces the `if`/`print` checks with `assert`, which raises an `AssertionError` when a condition is false. Compared with the previous test, it is more concise but stops at the first failure with a traceback instead of a friendly message.

# %%
from ref_calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- calculator3.py -->
#
# Identical to `calculator1.py`; it exists as the module imported by the next test file.

# %%
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator3.py -->
#
# Wraps each `assert` in `try`/`except AssertionError` to print a readable message instead of crashing. Compared with the previous test, every check runs even if an earlier one fails, at the cost of more code.

# %%
from ref_calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- calculator4.py -->
#
# Identical to `calculator1.py`; it exists as the module imported by the next test file.

# %%
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator4.py -->
#
# Adds negative numbers and zero as test cases, each in its own `try`/`except`. Compared with the previous test, coverage improves, but the repetitive boilerplate shows why a testing framework is useful.

# %%
from ref_calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- calculator5.py -->
#
# Same calculator code, now intended to be tested with the third-party `pytest` framework. Only the header comment changes from the previous calculator.

# %%
# Tests a function with one function via pytest


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator5.py -->
#
# Uses `pytest` (run with `pytest test_calculator5.py`), so the test file needs only plain `assert` statements inside a `test_` function—no `main`, no `try`/`except`. Compared with the previous test, pytest handles running and reporting, but the first failing assert still stops the rest of that function.

# %%
from ref_calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# %% [markdown]
# <!-- calculator6.py -->
#
# Same calculator code, header comment updated for testing with multiple test functions.

# %%
# Tests a function with multiple functions via pytest


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator6.py -->
#
# Splits the asserts into separate `test_positive`, `test_negative`, and `test_zero` functions. Compared with the previous test, pytest reports each category independently, so one failure doesn't hide the others.

# %%
from ref_calculator import square


def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# %% [markdown]
# <!-- calculator7.py -->
#
# Same calculator code as the previous block; it is the module under test for the next file.

# %%
# Tests a function with multiple functions via pytest


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_calculator7.py -->
#
# Imports `pytest` and uses `pytest.raises(TypeError)` to test that `square("cat")` raises an error. Compared with the previous test, it checks for an expected exception rather than a return value. Note: it imports from `calculator` (no number), as in the original source.

# %%
import pytest

from ref_calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")


# %% [markdown]
# <!-- hello0.py -->
#
# Defines a `hello` function with a default argument that prints its greeting. This starts a new example showing that functions with side effects (printing) are hard to test because they return `None`.

# %%
# Function to be tested


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- hello1.py -->
#
# Changes `hello` to return an f-string instead of printing, and moves the `print` into `main`. Compared with the previous block, the function's output can now be compared in a test.

# %%
# Has function return a str instead


def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()


# %% [markdown]
# <!-- test_hello1a.py -->
#
# Tests `hello` with pytest: once with the default argument and once with `"David"`. This is the first test of a function that returns a string.

# %%
from ref_hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


# %% [markdown]
# <!-- test_hello1b.py -->
#
# Loops over several names in `test_argument` and checks each result against an f-string. Compared with the previous test, it covers more inputs without writing a separate assert for each.

# %%
from ref_hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"


# %% [markdown]
# <!-- test/test_hello1c.py -->
#
# Same tests as `test_hello1a.py`, but stored inside a `test/` folder. Running `pytest test` runs every test file in that folder, which requires the `__init__.py` file shown next.

# %%
from ref_hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


# %% [markdown]
# <!-- test/__init__.py -->
#
# An empty file whose presence tells Python to treat the `test/` folder as a package, so `pytest test` can discover and import the tests inside it.

# %%
# (empty file)
