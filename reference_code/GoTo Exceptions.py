# %% [markdown]
# # Exceptions Reference (`try` / `except` / `raise`)
#
# An **exception** is Python saying "I can't do this", for example `int("cat")` or `10 / 0`.
# If nothing handles it, the program stops and prints a **traceback**.
# - `try` / `except` lets you **catch** an exception and decide what to do instead.
# - `raise` lets **your** code signal a problem.
#
# `# -> result` shows what a line returns or prints.
#
# **Run the SETUP cell first.** It lets examples that use `input()` run without you typing anything.
# `simulate_input("cat", "5")` pretends the user typed `cat`, then `5`. When the answers run out, it acts like Ctrl-D.
#
# 1. Cheat sheet
# 2. Reading a traceback
# 3. `try` / `except` basics
# 4. `else` and `finally`
# 5. Catching more than one kind of exception
# 6. The re-prompt loop with `try`
# 7. Ctrl-D and Ctrl-C (`EOFError`, `KeyboardInterrupt`)
# 8. Common exceptions: what causes them, how to fix or handle them
# 9. Raising exceptions
# 10. `sys.exit`
# 11. Testing for exceptions with `pytest.raises`
# 12. Check first, or try first?
# 13. Pitfalls
# 14. What should I do with this error?
#
# Sources: CS50P Lecture 3 (Exceptions), Lecture 4 (`sys.exit`), Lecture 5 (`pytest.raises`), and problem sets
# (fuel, grocery, taqueria, outdated, game, professor, bitcoin), Python docs ("Errors and Exceptions" tutorial, "Built-in Exceptions").
# Related: `GoTo Loops and Conditionals.py` §11 (re-prompt loops), `GoTo API JSON.py` §9 (`requests` errors).


# %% [markdown]
# ### SETUP: run this cell first
# You don't need to understand this cell. It replaces `input()` so the examples can "type" their own answers.
# To get the real `input()` back in Jupyter, restart the kernel.

# %%
# SETUP
import builtins

_real_input = builtins.input

def simulate_input(*answers):
    remaining = list(answers)

    def fake_input(prompt=""):
        if not remaining:                  # out of answers: act like the user pressed Ctrl-D
            print(prompt + "^D")
            builtins.input = _real_input
            raise EOFError
        answer = remaining.pop(0)
        print(prompt + answer)             # show it like a terminal would
        return answer

    builtins.input = fake_input


# %% [markdown]
# ## 1. Cheat sheet

# %%
try:                                   # code that might fail
    x = int("cat")
except ValueError:                     # runs only if that exception happened
    print("Not a number")
else:                                  # runs only if NO exception happened
    print("Got", x)
finally:                               # ALWAYS runs (cleanup)
    print("done")
# -> Not a number
# -> done

try:
    result = 10 / 0
except (ValueError, ZeroDivisionError) as e:   # catch several; e holds the details
    print(type(e).__name__, "-", e)
# -> ZeroDivisionError - division by zero

def set_level(n):
    if n not in [1, 2, 3]:
        raise ValueError("level must be 1, 2, or 3")   # signal a problem yourself
    return n

try:
    set_level(7)
except ValueError as e:
    print(e)
# -> level must be 1, 2, or 3

import sys
# sys.exit("Too few arguments")        # end the whole program with a message (§10)


# %% [markdown]
# ## 2. Reading a traceback
# When an exception isn't caught, Python prints something like this:
#
# ```
# Traceback (most recent call last):
#   File "number.py", line 1, in <module>
#     x = int(input("What's x? "))
#         ^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'cat'
# ```
#
# **Read it bottom-up:**
# 1. **Last line**: the exception **type** (`ValueError`) and **message**. This is what went wrong.
# 2. **Lines above**: **where**: file, line number, and the code on that line.
# 3. With several functions, the **lowest** `File ...` entry is where it finally broke. The entries above it show how the program got there.
#
# The type name (`ValueError`) is exactly what you write after `except`.

# %%
try:
    int("cat")
except ValueError as e:
    print(type(e).__name__)    # the kind of exception
    print(e)                   # the message
# -> ValueError
# -> invalid literal for int() with base 10: 'cat'


# %% [markdown]
# ## 3. `try` / `except` basics
# Put the line that **might fail** in `try`. Put what to do **instead** in `except`.
# If `try` succeeds, `except` is skipped. If a line in `try` fails, Python jumps straight to `except`
# and the rest of the `try` block is **skipped**.

# %%
def to_int(text):
    try:
        return int(text)
    except ValueError:
        print(f"{text!r} is not an integer")
        return None

to_int("42")                   # -> 42
to_int("cat")                  # returns None
# -> 'cat' is not an integer

# %% [markdown]
# ### Keep `try` small
# Only put the risky line(s) in `try`. You wrote this yourself in `professor.py`:
# *"try should handle the only risk and let the if conditionals take care of the rest."*
# A big `try` block can hide which line actually failed.

# %%
simulate_input("12")

try:
    answer = int(input("3 + 9 = "))   # the only risky line
except ValueError:
    print("EEE")
else:
    if answer == 12:                  # normal logic lives outside the try
        print("Correct")
# -> 3 + 9 = 12
# -> Correct

# %% [markdown]
# ### `as e` gives you the exception object
# `str(e)` (or `print(e)`) is the message. `type(e).__name__` is the kind of exception.

# %%
try:
    [1, 2, 3][10]
except IndexError as e:
    print(f"Problem: {e}")
# -> Problem: list index out of range


# %% [markdown]
# ## 4. `else` and `finally`
#
# | Block | Runs when... |
# |---|---|
# | `try` | always attempted first |
# | `except` | an exception of that type happened in `try` |
# | `else` | `try` finished with **no** exception |
# | `finally` | **always**, success or failure (even after `return` or `break`) |
#
# Use `else` for "what to do with the good result" (Lecture 3). Use `finally` for cleanup that must happen no matter what.

# %%
def check(text):
    try:
        x = int(text)
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")
    finally:
        print("(checked)")

check("50")
# -> x is 50
# -> (checked)
check("fifty")
# -> x is not an integer
# -> (checked)


# %% [markdown]
# ## 5. Catching more than one kind of exception
# - Use **separate `except` blocks** when each problem needs its own message (as in `fuel.py`).
# - Use a **tuple** when they all get the same handling.
# Python uses the **first** `except` that matches, top to bottom.

# %%
def fuel(fraction):
    try:
        x, y = fraction.split("/")
        percent = int(x) / int(y) * 100
    except ValueError:                           # "cat", "1.5/2", "1/2/3", "12"
        return "X and Y must be integers"
    except ZeroDivisionError:                    # "1/0"
        return "Y can't be zero"
    return f"{round(percent)}%"

fuel("3/4")          # -> '75%'
fuel("three/four")   # -> 'X and Y must be integers'
fuel("12")           # -> 'X and Y must be integers'  # split gave one piece: can't unpack into x, y
fuel("1/0")          # -> "Y can't be zero"

def fuel_short(fraction):
    try:
        x, y = fraction.split("/")
        return f"{round(int(x) / int(y) * 100)}%"
    except (ValueError, ZeroDivisionError):      # same handling for both
        return "Invalid fraction"

fuel_short("1/0")    # -> 'Invalid fraction'

# %% [markdown]
# ### Try one way, then another (`outdated.py`)
# A second `try` inside an `except` lets you attempt a backup approach.

# %%
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

def to_iso(date):
    try:                                               # first try: 9/8/1636
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        try:                                           # backup: September 8, 1636
            month, day, year = date.split(" ")
            month = months.index(month) + 1            # .index raises ValueError if not found
            day, year = int(day.rstrip(",")), int(year)
        except ValueError:
            return None
    return f"{year}-{month:02}-{day:02}"

to_iso("9/8/1636")                # -> '1636-09-08'
to_iso("September 8, 1636")       # -> '1636-09-08'
to_iso("Smarch 8, 1636")          # -> None


# %% [markdown]
# ## 6. The re-prompt loop with `try`
# Combine `while True` with `try` to **keep asking until the input works**.
# This is the Lecture 3 `get_int` progression. Each version below does the same job.

# %%
simulate_input("cat", "5")

while True:                                    # version 1: break in else
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
# -> What's x? cat
# -> x is not an integer
# -> What's x? 5
# -> x is 5

# %%
simulate_input("dog", "", "7")

def get_int(prompt):                           # version 2: return from inside try (the final Lecture 3 version)
    while True:
        try:
            return int(input(prompt))          # return ends the loop and the function
        except ValueError:
            pass                               # say nothing; just ask again

n = get_int("What's n? ")
# -> What's n? dog
# -> What's n?
# -> What's n? 7
n                                              # -> 7

# %% [markdown]
# ### `try` for the type, `if` for the range (`game.py`, `professor.py`)
# `try` catches "not a number". An `if` then checks "is the number allowed?".

# %%
simulate_input("three", "0", "5", "2")

def get_level():
    while True:
        try:
            level = int(input("Level 1-3: "))
        except ValueError:
            print("Not a number")
            continue                           # skip the range check, ask again
        if 1 <= level <= 3:
            return level
        print("Out of range")

level = get_level()
# -> Level 1-3: three
# -> Not a number
# -> Level 1-3: 0
# -> Out of range
# -> Level 1-3: 5
# -> Out of range
# -> Level 1-3: 2
level                                          # -> 2

# %% [markdown]
# ### Several checks in one loop (`fuel.py`)
# Parse in `try`. Check the rules in `else`. `break` only when everything passes.

# %%
simulate_input("cat/dog", "3/0", "5/4", "3/4")

while True:
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)
        percent = x / y
    except ValueError:
        print("Numbers must be integers")
    except ZeroDivisionError:
        print("Y must not be zero")
    else:
        if 0 <= x <= y:
            break
        print("X must be between 0 and Y")
print(f"{percent:.0%}")
# -> Fraction: cat/dog
# -> Numbers must be integers
# -> Fraction: 3/0
# -> Y must not be zero
# -> Fraction: 5/4
# -> X must be between 0 and Y
# -> Fraction: 3/4
# -> 75%


# %% [markdown]
# ## 7. Ctrl-D and Ctrl-C
#
# | Keys | Exception | Meaning |
# |---|---|---|
# | **Ctrl-D** (Mac/Linux) | `EOFError` | "I'm done typing" (end of input). Catch it to finish a list. |
# | **Ctrl-C** | `KeyboardInterrupt` | "Stop the program!" Usually **don't** catch it. |
#
# `grocery.py`, `taqueria.py`, and `adieu.py` all read until Ctrl-D.

# %%
simulate_input("taco", "bowl", "pizza")

menu = {"Taco": 3.00, "Bowl": 8.50}
total = 0
while True:
    try:
        item = input("Item: ").title()
    except EOFError:
        print()                                # newline after ^D
        break
    try:
        total += menu[item]
    except KeyError:                           # not on the menu: ignore it
        pass
    else:
        print(f"Total: ${total:.2f}")
# -> Item: taco
# -> Total: $3.00
# -> Item: bowl
# -> Total: $11.50
# -> Item: pizza
# -> Item: ^D


# %% [markdown]
# ## 8. Common exceptions
#
# | Exception | Usually means | Common fix |
# |---|---|---|
# | `ValueError` | right type, **bad value**: `int("cat")` | validate, or `try/except` + re-prompt |
# | `TypeError` | **wrong type** for the operation: `"a" + 1` | convert with `int()`/`str()` |
# | `NameError` | variable/function **not defined** (typo, or never assigned) | check spelling and order |
# | `IndexError` | list/string position **doesn't exist** | check `len()`; remember indexes start at 0 |
# | `KeyError` | dict **key doesn't exist** | `in` check or `.get()` |
# | `ZeroDivisionError` | divided by zero | check the divisor, or catch it |
# | `AttributeError` | object doesn't have that method/attribute: `5.upper()` | check the type and spelling |
# | `EOFError` | input ended (Ctrl-D) | catch it to finish an input loop |
# | `KeyboardInterrupt` | user pressed Ctrl-C | usually let it stop the program |
# | `FileNotFoundError` | file path doesn't exist | check the path/name |
# | `ModuleNotFoundError` | import failed | `pip install ...` / check the name / check the venv |
# | `SyntaxError` / `IndentationError` | code isn't valid Python | fix the code; you **can't** catch these in the same file |
# | `AssertionError` | an `assert` was False (Lecture 5 tests) | fix the code, or the test |
# | `requests.RequestException` | network/API failure | see `GoTo API JSON.py` §9 |
# | `json.JSONDecodeError` | text isn't valid JSON | see `GoTo API JSON.py` §6 |

# %% [markdown]
# ### Seeing each one
# The helper `show()` runs a small piece of code and prints which exception happened and its message.

# %%
def show(code):
    try:
        exec(code, {})
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

show('int("cat")')                  # -> ValueError: invalid literal for int() with base 10: 'cat'
show('int("3.5")')                  # -> ValueError: invalid literal for int() with base 10: '3.5'
show('"a" + 1')                     # -> TypeError: can only concatenate str (not "int") to str
show('len(5)')                      # -> TypeError: object of type 'int' has no len()
show('int(None)')                   # -> TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
show('print(totl)')                 # -> NameError: name 'totl' is not defined
show('[1, 2, 3][3]')                # -> IndexError: list index out of range
show('"hi"[5]')                     # -> IndexError: string index out of range
show('{"a": 1}["b"]')               # -> KeyError: 'b'
show('10 / 0')                      # -> ZeroDivisionError: division by zero
show('(5).upper()')                 # -> AttributeError: 'int' object has no attribute 'upper'
show('open("no_such_file.txt")')    # -> FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'
show('import no_such_module')       # -> ModuleNotFoundError: No module named 'no_such_module'
show('assert 1 + 1 == 3, "math is broken"')   # -> AssertionError: math is broken
show('x, y = "1/2/3".split("/")')   # -> ValueError: too many values to unpack (expected 2, got 3)
show('["a", "b"].index("z")')       # -> ValueError: list.index(x): x not in list

# %% [markdown]
# ### Syntax errors happen before the code runs
# Python reads the whole file first. If it isn't valid Python, **nothing** runs, so a `try` in that file can't catch it.
# (They're shown here with `compile()`, which checks code without running it.)

# %%
def check_syntax(code):
    try:
        compile(code, "example.py", "exec")
        print("valid")
    except SyntaxError as e:                     # IndentationError is a kind of SyntaxError
        print(f"{type(e).__name__} on line {e.lineno}: {e.msg}")

check_syntax('print("hello, world)')             # -> SyntaxError on line 1: unterminated string literal (detected at line 1)
check_syntax('if x = 5:\n    pass')              # -> SyntaxError on line 1: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
check_syntax('if True:\nprint("hi")')            # -> IndentationError on line 2: expected an indented block after 'if' statement on line 1
check_syntax('print("hello")')                   # -> valid

# %% [markdown]
# ### Exceptions come in families
# Every exception is a kind of `Exception`. Some are more specific kinds of others.
# Catching a parent also catches its children.

# %%
issubclass(ZeroDivisionError, ArithmeticError)   # -> True
issubclass(FileNotFoundError, OSError)           # -> True
issubclass(ModuleNotFoundError, ImportError)     # -> True
issubclass(IndentationError, SyntaxError)        # -> True
issubclass(ValueError, Exception)                # -> True
issubclass(KeyboardInterrupt, Exception)         # -> False  # so `except Exception` won't swallow Ctrl-C
issubclass(SystemExit, Exception)                # -> False  # ...or sys.exit


# %% [markdown]
# ## 9. Raising exceptions
# `raise SomeError("message")` stops the function right there and sends the problem **up to whoever called it**.
#
# **Why raise instead of print or return?** (the "no idea why, it's per spec" question from `professor.py`)
# - A function like `generate_integer(level)` has **no sensible answer** for `level=7`.
#   - `print` would let the program carry on with bad data.
#   - `return None` would crash somewhere later, which is harder to trace.
# - Raising makes the problem **impossible to ignore**, and lets the **caller** decide what to do: re-prompt, skip, or quit.
# - It also makes the function **testable**: a test can check that bad input raises (§11).

# %%
import random

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    raise ValueError(f"level must be 1, 2, or 3, not {level}")

0 <= generate_integer(1) <= 9          # -> True

try:
    generate_integer(7)
except ValueError as e:
    print(e)                           # -> level must be 1, 2, or 3, not 7

# %% [markdown]
# ### Pick the exception that fits
# - `ValueError`: right type, wrong value. This is the most common one to raise.
# - `TypeError`: wrong type entirely.
# Always include a helpful message.
#
# This `convert` is the shape CS50P Problem Set 5 asks for in `fuel.py`: it **raises** instead of printing, so `main` can re-prompt and tests can check it.

# %%
def convert(fraction):
    x, y = fraction.split("/")              # a bad format raises ValueError on its own
    x, y = int(x), int(y)                   # so does a non-integer
    if y == 0:
        raise ZeroDivisionError("Y can't be zero")
    if x > y or x < 0:
        raise ValueError("X must be between 0 and Y")
    return round(x / y * 100)

convert("3/4")                              # -> 75

for bad in ["4/3", "1/0", "cat"]:
    try:
        convert(bad)
    except (ValueError, ZeroDivisionError) as e:
        print(f"{bad}: {type(e).__name__}: {e}")
# -> 4/3: ValueError: X must be between 0 and Y
# -> 1/0: ZeroDivisionError: Y can't be zero
# -> cat: ValueError: not enough values to unpack (expected 2, got 1)

# %% [markdown]
# ### Re-raise: do something, then pass the error along
# A bare `raise` inside `except` sends the **same** exception onward.

# %%
def load_number(text):
    try:
        return int(text)
    except ValueError:
        print(f"(logging) bad value: {text!r}")
        raise                               # still an error for the caller

try:
    load_number("oops")
except ValueError:
    print("caller handled it")
# -> (logging) bad value: 'oops'
# -> caller handled it

# %% [markdown]
# ### Your own exception type (optional)
# Make a class that inherits from an existing exception. Catching by name then reads like plain English.

# %%
class InvalidPlateError(ValueError):
    pass

def check_plate(plate):
    if not 2 <= len(plate) <= 6:
        raise InvalidPlateError(f"{plate!r} must be 2-6 characters")
    return plate

try:
    check_plate("C")
except InvalidPlateError as e:
    print(e)                                # -> 'C' must be 2-6 characters


# %% [markdown]
# ## 10. `sys.exit`
# Ends the **whole program** right away. Used in command-line programs when there's nothing sensible to do next
# (Lecture 4 `name.py`, `bitcoin.py`).
# - `sys.exit("message")` prints the message (to stderr) and exits with an error code.
# - `sys.exit()` exits quietly.
#
# Under the hood it **raises `SystemExit`**. That's why a bare `except:` can accidentally catch it (§13).
#
# | Use | When |
# |---|---|
# | `raise ValueError(...)` | inside a **function**: let the caller decide |
# | `sys.exit("...")` | in `main()` / top level: the program **can't continue** |

# %%
import sys

def main(argv):
    if len(argv) != 2:
        sys.exit("Usage: python bitcoin.py n")
    try:
        n = float(argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    print(f"Buying {n} bitcoin")

main(["bitcoin.py", "1.5"])                # -> Buying 1.5 bitcoin

for argv in (["bitcoin.py"], ["bitcoin.py", "cat"]):
    try:
        main(argv)                         # these would end a real program
    except SystemExit as e:                # caught here ONLY to show what happens
        print("exit:", e)
# -> exit: Usage: python bitcoin.py n
# -> exit: Command-line argument is not a number


# %% [markdown]
# ## 11. Testing for exceptions with `pytest.raises` (Lecture 5)
# A test can check that bad input **raises** the right exception. The test **passes** only if that exception happens.
# `match=` also checks the message.
#
# In a test file (`test_fuel.py`), run with `pytest test_fuel.py`:
# ```
# import pytest
# from fuel import convert
#
# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         convert("1/0")
#
# def test_x_greater_than_y():
#     with pytest.raises(ValueError):
#         convert("4/3")
# ```
# `pytest.raises` also works outside a test file, as below:

# %%
import pytest

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError("Y can't be zero")
    if x > y:
        raise ValueError("X must not be greater than Y")
    return round(x / y * 100)

with pytest.raises(ZeroDivisionError):
    convert("1/0")
with pytest.raises(ValueError, match="greater than Y"):
    convert("4/3")
with pytest.raises(ValueError):
    convert("cat")
print("all exception checks passed")       # -> all exception checks passed

try:
    with pytest.raises(ValueError):
        convert("1/2")                     # does NOT raise, so pytest.raises fails the test
except BaseException as e:
    print(type(e).__name__)                # -> Failed


# %% [markdown]
# ## 12. Check first, or try first?
# - **Check first** ("look before you leap"): `if text.isdigit(): int(text)`
# - **Try first** ("easier to ask forgiveness"): `try: int(text) except ValueError: ...`
#
# Both are fine. In Python, **try first** is often simpler and more complete, because the check can miss cases.

# %%
text = "-5"
text.isdigit()                     # -> False  # the check rejects a valid integer!
try:
    number = int(text)             # try-first handles it
except ValueError:
    number = None
number                             # -> -5

scores = {"Alice": 95}
if "Bob" in scores:                # check first: fine for dicts
    print(scores["Bob"])
scores.get("Bob", 0)               # -> 0      # often simplest (see GoTo Dict.py §7)


# %% [markdown]
# ## 13. Pitfalls

# %% [markdown]
# ### Bare `except:` catches too much
# It even catches Ctrl-C and `sys.exit()`, so the program may refuse to quit.
# Name the exception you expect.

# %%
import sys

try:
    sys.exit("goodbye")
except:                                    # BAD: caught the exit
    print("sys.exit was swallowed!")
# -> sys.exit was swallowed!

try:
    int("cat")
except ValueError:                         # GOOD: only what you expect
    print("not a number")
# -> not a number

# %% [markdown]
# ### `except Exception` can hide real bugs
# A typo becomes a misleading "invalid input" message. Catch the **specific** exception instead.

# %%
total = 10
try:
    print(totl / 2)                        # typo: NameError, not bad input
except Exception:
    print("Invalid input")                 # misleading!
# -> Invalid input

try:
    print(totl / 2)
except ZeroDivisionError:
    print("Invalid input")
except NameError as e:
    print("Bug found:", e)                 # a specific except lets the real problem show
# -> Bug found: name 'totl' is not defined

# %% [markdown]
# ### Order of `except` blocks: specific before general
# Python uses the **first** match. A general one listed first catches everything, and the specific one never runs.

# %%
try:
    10 / 0
except Exception:
    print("general")                       # this wins
except ZeroDivisionError:
    print("specific")                      # never reached
# -> general

try:
    10 / 0
except ZeroDivisionError:
    print("specific")                      # specific first: correct
except Exception:
    print("general")
# -> specific

# %% [markdown]
# ### A variable from a failed `try` may not exist (Lecture 3)
# If the line that assigns `x` fails, `x` is never created. Use `else`, or give it a starting value.

# %%
try:
    y = int("cat")
except ValueError:
    print("y is not an integer")
try:
    print(f"y is {y}")
except NameError as e:
    print("NameError:", e)
# -> y is not an integer
# -> NameError: name 'y' is not defined

# %% [markdown]
# ### Risky code outside the `try` still crashes
# In `game.py`, the **level** prompt is inside `try`, but the **guess** prompt isn't, so typing "cat" as a guess crashes.
# Every `int(input(...))` needs its own protection.

# %%
simulate_input("cat")
try:
    guess = int(input("Guess: "))
except ValueError:
    print("Not a number")                  # protected: re-prompt instead of crashing
# -> Guess: cat
# -> Not a number

# %% [markdown]
# ### `except ...: pass` hides problems
# It's fine when ignoring really is the plan, like skipping unknown menu items in `taqueria.py`.
# Anywhere else, at least print something while you're developing.

# %% [markdown]
# ### Catching the wrong type
# Test in the Python shell to see which exception actually happens before writing the `except`.

# %%
try:
    int(None)                              # it's a TypeError, not a ValueError
except ValueError:
    print("never printed")
except TypeError:
    print("TypeError: need a string or number")
# -> TypeError: need a string or number


# %% [markdown]
# ## 14. What should I do with this error?
#
# | Situation | Do this |
# |---|---|
# | User typed something unusable | `try/except` inside a `while True` loop; re-prompt (§6) |
# | User pressed Ctrl-D to finish | `except EOFError: break` (§7) |
# | Missing dict key is normal | `.get(key, default)` or `if key in d` |
# | Optional item to ignore (e.g., not on the menu) | `except KeyError: pass` |
# | Your function got a value it can't handle | `raise ValueError("clear message")` (§9) |
# | Command-line program can't continue | `sys.exit("message")` (§10) |
# | Network/API call | `except requests.RequestException` (`GoTo API JSON.py` §9) |
# | It's a bug in your code (typo, wrong type) | **don't** catch it; read the traceback and fix it (§2) |
# | Want a test to confirm bad input fails | `with pytest.raises(...)` (§11) |
