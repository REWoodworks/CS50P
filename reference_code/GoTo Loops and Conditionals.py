# %% [markdown]
# # Conditionals and Loops Reference
#
# **Conditionals** (`if`, `elif`, `else`, `match`) let a program make decisions.
# **Loops** (`for`, `while`) let it repeat work.
# Almost every CS50P program uses both.
#
# `# -> result` shows what a line returns or prints.
#
# **Run the SETUP cell first.** It lets examples that use `input()` run without you typing anything.
# `simulate_input("cat", "5")` pretends the user typed `cat`, then `5`.
#
# **Part 1: Conditionals**
# 1. Cheat sheet
# 2. Comparisons and True/False
# 3. `if` / `elif` / `else`
# 4. `and`, `or`, `not`, `in`
# 5. Conditions inside functions
# 6. `match` / `case`
#
# **Part 2: Loops**
# 7. `for` loops
# 8. `range()`
# 9. `while` loops
# 10. `break`, `continue`, `pass`
# 11. The re-prompt loop (checking user input)
# 12. Loop patterns you'll use again and again
# 13. Nested loops
# 14. Pitfalls
# 15. Which one do I use?
#
# Sources: CS50P Lectures 1–4 and problem sets (bank, deep, extensions, interpreter, meal,
# camel, coke, twttr, plates, nutrition, fuel, grocery, taqueria, outdated, game, professor),
# Python docs ("More Control Flow Tools" tutorial).
# Related: `GoTo List.py` and `GoTo Dict.py` (looping over collections), `GoTo Exceptions.py` (try/except).


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
x = 7

if x > 10:                     # if: test a condition
    print("big")
elif x > 5:                    # elif: only checked if everything above was False
    print("medium")
else:                          # else: runs if nothing above was True
    print("small")
# -> medium

x == 7                         # -> True   # == compares; = assigns
x != 7                         # -> False
1 <= x <= 10                   # -> True   # chained comparison: "between"
x > 5 and x < 10               # -> True   # both must be True
x < 0 or x > 5                 # -> True   # at least one must be True
not x > 5                      # -> False  # flips True/False
"a" in "cat"                   # -> True   # membership
"small" if x < 5 else "big"    # -> 'big'  # one-line if/else

for letter in "hi":            # for: once per item
    print(letter)
# -> h
# -> i

for i in range(3):             # range(3) gives 0, 1, 2
    print(i)
# -> 0
# -> 1
# -> 2

n = 3
while n > 0:                   # while: repeat as long as the condition is True
    print(n)
    n -= 1                     # something must change, or it loops forever
# -> 3
# -> 2
# -> 1

for n in [1, 2, 3, 4, 5]:
    if n == 2:
        continue               # continue: skip to the next item
    if n == 4:
        break                  # break: leave the loop now
    print(n)
# -> 1
# -> 3


# %% [markdown]
# # Part 1: Conditionals
#
# ## 2. Comparisons and True/False
# Every condition ends up `True` or `False` (a **boolean**).
#
# | Operator | Means |
# |---|---|
# | `==` | equal to |
# | `!=` | not equal to |
# | `<`  `>` | less than, greater than |
# | `<=`  `>=` | less/greater than **or equal to** |

# %%
5 == 5                  # -> True
5 != 5                  # -> False
3 < 5                   # -> True
5 <= 5                  # -> True
"apple" == "Apple"      # -> False  # capitals matter
"apple" < "banana"      # -> True   # strings compare alphabetically
"5" == 5                # -> False  # input() gives a str; convert with int() first
type(3 < 5)             # -> <class 'bool'>

time = 7.5
7 <= time <= 8          # -> True   # chained: "time is between 7 and 8" (meal.py)

# %% [markdown]
# ### Truthy and falsy
# `if` works with any value, not only True/False.
# These count as **False**: `0`, `0.0`, `""` (empty string), `[]`, `{}`, `None`. Everything else counts as True.
# `bool(value)` shows how Python sees a value.

# %%
bool(0)                 # -> False
bool(42)                # -> True
bool("")                # -> False
bool("hi")              # -> True
bool([])                # -> False
bool(None)              # -> False

name = ""
if name:
    print(f"hello, {name}")
else:
    print("no name given")
# -> no name given

result = None
result is None          # -> True   # use `is None` to check for None


# %% [markdown]
# ## 3. `if` / `elif` / `else`
# Three shapes:
# - `if` alone does something **or nothing**.
# - `if/else` picks one of **two** paths.
# - `if/elif/.../else` picks one of **many** paths.
#
# Python checks from the top and runs **only the first** branch that's True, then skips the rest.
# The indented lines (4 spaces) under each branch are its **block**.

# %%
score = 85

if score >= 60:                    # if alone
    print("pass")
# -> pass

if score >= 90:                    # if / else
    print("A")
else:
    print("not an A")
# -> not an A

if score >= 90:                    # if / elif / else (Lecture 1 grade.py)
    print("Grade: A")
elif score >= 80:                  # no need for "and score < 90": we only get here if the line above was False
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# -> Grade: B

# %% [markdown]
# ### Separate `if`s vs an `elif` chain
# Separate `if` statements are **all** checked, so more than one can run.
# An `elif` chain stops at the first match.

# %%
x = 15

if x > 5:
    print("more than 5")
if x > 10:
    print("more than 10")          # also runs
# -> more than 5
# -> more than 10

if x > 5:
    print("more than 5")
elif x > 10:
    print("more than 10")          # skipped: the first branch already matched
# -> more than 5

# %% [markdown]
# ### Order matters in an `elif` chain
# Put the **most specific** test first.
# In `bank.py`, testing `== "hello"` must come before `.startswith("h")`, because "hello" also starts with "h".

# %%
def bank(greeting):
    greeting = greeting.strip().lower()
    if greeting == "hello":
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

bank("Hello")           # -> '$0'
bank("hey there")       # -> '$20'
bank("What's up")       # -> '$100'


# %% [markdown]
# ## 4. `and`, `or`, `not`, `in`
#
# | Operator | True when... |
# |---|---|
# | `a and b` | **both** are True |
# | `a or b` | **at least one** is True |
# | `not a` | `a` is False |
# | `x in collection` | `x` is inside the string/list/dict |
#
# Each side of `and`/`or` must be a **full comparison** (see §14 for the classic mistake).

# %%
age = 20
has_ticket = True

age >= 18 and has_ticket          # -> True
age < 13 or age > 65              # -> False
not has_ticket                    # -> False

answer = "forty two"
answer == "42" or answer == "forty-two" or answer == "forty two"   # -> True  # deep.py
answer in ["42", "forty-two", "forty two"]                       # -> True  # same test, shorter

"a" in "banana"                   # -> True   # in a string: substring
"z" not in "banana"               # -> True
3 in [1, 2, 3]                    # -> True   # in a list: an item
"apple" in {"apple": 130}         # -> True   # in a dict: a key (nutrition.py)

# %% [markdown]
# ### Grouping with parentheses
# `not` applies to what comes right after it. Use parentheses to be clear.
# This is the pattern from the Lecture 1 short `recommendations.py`.

# %%
difficulty = "Hard"
not (difficulty == "Difficult" or difficulty == "Casual")    # -> True   # "not one of the valid choices"
difficulty not in ["Difficult", "Casual"]                     # -> True   # same, easier to read

# %% [markdown]
# ### String methods that return True/False
# These are handy in conditions (bank, extensions, plates, camel, twttr).

# %%
"hello".startswith("h")           # -> True
"cat.gif".endswith(".gif")        # -> True
"CS50".isalnum()                  # -> True   # letters or digits only
"CS".isalpha()                    # -> True   # letters only
"50".isdigit()                    # -> True   # digits only
"a".islower()                     # -> True
"A".isupper()                     # -> True

file = "Photo.JPG".lower()
if file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
# -> image/jpeg
file.endswith((".jpg", ".jpeg"))  # -> True   # endswith accepts a tuple of options


# %% [markdown]
# ## 5. Conditions inside functions
#
# ### Return True/False directly
# A comparison already **is** True or False, so you can return it. (Lecture 1 `is_even`)

# %%
def is_even_long(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even(n):
    return n % 2 == 0              # same result, one line

is_even(4)                         # -> True
is_even(7)                         # -> False

if is_even(10):
    print("Even")
# -> Even

# %% [markdown]
# ### Early return ("guard clauses")
# Check for bad cases first and `return` right away. The rest of the function doesn't need extra indentation.
# This is how `plates.py` and `interpreter.py` are structured.

# %%
def is_valid(plate):
    if not 2 <= len(plate) <= 6:       # rule 1: 2 to 6 characters
        return False
    if not plate[:2].isalpha():        # rule 2: starts with two letters
        return False
    if not plate.isalnum():            # rule 3: no punctuation or spaces
        return False
    return True                        # passed every check

is_valid("CS50")                       # -> True
is_valid("C")                          # -> False
is_valid("PI3.14")                     # -> False

# %% [markdown]
# ### One-line if/else (conditional expression)
# `value_if_true if condition else value_if_false` picks a **value**. Use it for simple choices only.

# %%
n = 7
parity = "even" if n % 2 == 0 else "odd"
parity                                 # -> 'odd'
count = 1
f"{count} item{'s' if count != 1 else ''}"    # -> '1 item'


# %% [markdown]
# ## 6. `match` / `case`
# Compares one value against several options. It's cleaner than a long `elif` chain of `==` tests.
# - `|` means "or".
# - `_` is the catch-all, like `else`.
# (Lecture 1 `house.py`)

# %%
def house(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            return "Gryffindor"
        case "Draco":
            return "Slytherin"
        case _:
            return "Who?"

house("Ron")          # -> 'Gryffindor'
house("Draco")        # -> 'Slytherin'
house("Neville")      # -> 'Who?'

# %% [markdown]
# ### `match` vs `elif` vs a dict
# - `match` handles **exact** matches only. For ranges (`score >= 90`), use `elif`.
# - When each option just maps to a value, a **dict** is often simplest (`nutrition.py`; see `GoTo Dict.py` §6).

# %%
calories = {"apple": 130, "banana": 110, "lime": 20}
fruit = "Banana".lower()
if fruit in calories:
    print(f"Calories: {calories[fruit]}")
# -> Calories: 110


# %% [markdown]
# # Part 2: Loops
#
# ## 7. `for` loops
# `for item in collection:` runs the block **once per item**. The loop variable (`item`) holds the current one.
# You can loop over strings, lists, dicts, `range()`, file lines, and more.

# %%
for letter in "cat":                         # string: each character
    print(letter)
# -> c
# -> a
# -> t

for name in ["Harry", "Ron"]:                # list: each item
    print("hello,", name)
# -> hello, Harry
# -> hello, Ron

prices = {"Taco": 3.00, "Bowl": 8.50}
for item, price in prices.items():           # dict: key and value (see GoTo Dict.py §4)
    print(f"{item}: ${price:.2f}")
# -> Taco: $3.00
# -> Bowl: $8.50

for _ in range(3):                           # _ means "I don't need the value"
    print("meow")
# -> meow
# -> meow
# -> meow

# %% [markdown]
# ### Getting the position too: `enumerate`
# `enumerate` gives `(position, item)` pairs. It's cleaner than `range(len(...))`.

# %%
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students, start=1):
    print(i, student)
# -> 1 Hermione
# -> 2 Harry
# -> 3 Ron

for i in range(len(students)):               # the Lecture 2 way, same result
    print(i + 1, students[i])
# -> 1 Hermione
# -> 2 Harry
# -> 3 Ron

# %% [markdown]
# ### Two lists side by side: `zip`

# %%
names = ["Hermione", "Draco"]
houses = ["Gryffindor", "Slytherin"]
for name, house in zip(names, houses):
    print(name, "->", house)
# -> Hermione -> Gryffindor
# -> Draco -> Slytherin


# %% [markdown]
# ## 8. `range()`
# Generates numbers for a loop. Like slicing, the **stop number is not included**.
#
# | Call | Numbers |
# |---|---|
# | `range(5)` | 0, 1, 2, 3, 4 |
# | `range(1, 6)` | 1, 2, 3, 4, 5 |
# | `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
# | `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

# %%
list(range(5))              # -> [0, 1, 2, 3, 4]
list(range(1, 6))           # -> [1, 2, 3, 4, 5]
list(range(0, 10, 2))       # -> [0, 2, 4, 6, 8]
list(range(5, 0, -1))       # -> [5, 4, 3, 2, 1]
len(range(10))              # -> 10  # range(n) always repeats n times

for i in range(3, 0, -1):
    print(i)
print("Liftoff!")
# -> 3
# -> 2
# -> 1
# -> Liftoff!


# %% [markdown]
# ## 9. `while` loops
# `while condition:` repeats **as long as** the condition is True. It checks before every pass.
# Something inside the loop **must** eventually make the condition False, or use `break`. Otherwise it runs forever.

# %%
i = 0
while i < 3:                # counting loop (Lecture 2 cat.py)
    print("meow")
    i += 1                  # same as i = i + 1
# -> meow
# -> meow
# -> meow

# %% [markdown]
# ### Loop until something happens (`coke.py`)
# `while` fits best when you **don't know in advance** how many passes you need.

# %%
simulate_input("25", "3", "10", "25")

paid = 0
cost = 50
while paid < cost:
    print(f"Amount Due: {cost - paid}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:              # ignore coins the machine doesn't accept
        paid += coin
print(f"Change Owed: {paid - cost}")
# -> Amount Due: 50
# -> Insert Coin: 25
# -> Amount Due: 25
# -> Insert Coin: 3
# -> Amount Due: 25
# -> Insert Coin: 10
# -> Amount Due: 15
# -> Insert Coin: 25
# -> Change Owed: 10

# %% [markdown]
# ### Walking a string by position (`camel.py`, solution 5)
# A `while` loop with an index does the same job as `for`. Usually `for` is simpler.

# %%
camel = "preferredFirstName"
snake = ""
position = 0
while position < len(camel):
    letter = camel[position]
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter
    position += 1
snake                        # -> 'preferred_first_name'

# %% [markdown]
# ### `while True` + `break`
# Loops forever **until** a `break` inside it runs. It's the basis of the re-prompt loop in §11.

# %%
n = 1
while True:
    n *= 2
    if n > 50:
        break
n                            # -> 64


# %% [markdown]
# ## 10. `break`, `continue`, `pass`
#
# | Keyword | What it does |
# |---|---|
# | `break` | leaves the loop **immediately** |
# | `continue` | skips the rest of this pass and **goes to the next one** |
# | `pass` | does nothing; a placeholder where Python needs a line |
# | `return` | (inside a function) leaves the loop **and** the function |
#
# `break` and `continue` affect only the **innermost** loop they're in.

# %%
for n in range(1, 8):
    if n % 2 == 0:
        continue             # skip even numbers
    if n > 5:
        break                # stop completely
    print(n)
# -> 1
# -> 3
# -> 5

text = "Twitter"
for letter in text:                      # twttr.py, revision 1
    if letter.lower() in "aeiou":
        continue                         # skip vowels
    print(letter, end="")
print()
# -> Twttr

def not_done_yet():
    pass                                 # placeholder so the function is valid

# %% [markdown]
# ### `return` inside a loop (`plates.py`)
# In a function, `return` stops the loop and hands back an answer right away. You don't need `break`.

# %%
def first_digit_position(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return i                     # found it: stop searching
    return None                          # loop finished without finding one

first_digit_position("CS50")             # -> 2
first_digit_position("HELLO")            # -> None


# %% [markdown]
# ## 11. The re-prompt loop (checking user input)
# This shape shows up in almost every CS50P problem set: **keep asking until the input is valid**.
#
# ```
# while True:
#     answer = input(...)
#     if answer is good:
#         break          # or return answer
#     (optional) print a hint
# ```

# %%
simulate_input("0", "-3", "5")

while True:
    n = int(input("Level: "))
    if n > 0:
        break                            # good input: leave the loop
    print("Must be positive")
print(f"You chose {n}")
# -> Level: 0
# -> Must be positive
# -> Level: -3
# -> Must be positive
# -> Level: 5
# -> You chose 5

# %% [markdown]
# ### Inside a function: `return` the good value (Lecture 2 `get_number`)
# To also handle non-numbers like "cat", add `try/except ValueError` (see `GoTo Exceptions.py` §6).

# %%
simulate_input("4", "2")

def get_level():
    while True:
        level = int(input("Level 1-3: "))
        if 1 <= level <= 3:
            return level                 # return ends the loop AND the function
        print("Please enter 1, 2, or 3")

level = get_level()
# -> Level 1-3: 4
# -> Please enter 1, 2, or 3
# -> Level 1-3: 2
level                                    # -> 2

# %% [markdown]
# ### A limited number of tries (`professor.py`)
# Count the attempts with a variable, and stop at the limit **or** when the answer is right.

# %%
simulate_input("5", "6", "9")

x, y = 3, 4
tries = 0
while tries < 3:
    answer = int(input(f"{x} + {y} = "))
    if answer == x + y:
        print("Correct!")
        break
    print("EEE")
    tries += 1
if tries == 3:
    print(f"{x} + {y} = {x + y}")        # out of tries: show the answer
# -> 3 + 4 = 5
# -> EEE
# -> 3 + 4 = 6
# -> EEE
# -> 3 + 4 = 9
# -> EEE
# -> 3 + 4 = 7

# %% [markdown]
# ### Reading until Ctrl-D (`grocery.py`, `taqueria.py`, `adieu.py`)
# When the user presses Ctrl-D, `input()` raises `EOFError`. Catch it to leave the loop.

# %%
simulate_input("apple", "banana", "apple")

items = []
while True:
    try:
        items.append(input("Item: "))
    except EOFError:
        print()                          # move to a fresh line after ^D
        break
print(items)
# -> Item: apple
# -> Item: banana
# -> Item: apple
# -> Item: ^D
# ->
# -> ['apple', 'banana', 'apple']


# %% [markdown]
# ## 12. Loop patterns you'll use again and again
#
# ### Build a new string (`camel.py`, `twttr.py`)
# Start empty, then add to it on each pass.

# %%
camel = "firstName"
snake = ""
for letter in camel:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter
snake                                    # -> 'first_name'

text = "Twitter"
no_vowels = ""
for letter in text:                      # twttr.py, revision 2
    if letter.lower() not in "aeiou":
        no_vowels += letter
no_vowels                                # -> 'Twttr'

# %% [markdown]
# ### Running total (`coke.py`, `taqueria.py`)
# Start at 0, then add on each pass.

# %%
menu = {"Taco": 3.00, "Burrito": 7.50, "Bowl": 8.50}
order = ["Taco", "Taco", "Bowl", "Pizza"]
total = 0
for food in order:
    if food in menu:                     # skip things not on the menu
        total += menu[food]
f"Total: ${total:.2f}"                   # -> 'Total: $14.50'

sum([3.00, 3.00, 8.50])                  # -> 14.5  # built-in shortcut when you just need the sum

# %% [markdown]
# ### Counting (`grocery.py`)
# To count **one** thing, use a number. To count **each different** thing, use a dict (see `GoTo Dict.py` §6).

# %%
words = ["apple", "banana", "apple"]
apples = 0
for word in words:
    if word == "apple":
        apples += 1
apples                                   # -> 2

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for word in sorted(counts):
    print(counts[word], word.upper())
# -> 2 APPLE
# -> 1 BANANA

# %% [markdown]
# ### Filter: keep only some items

# %%
nums = [4, -2, 7, 0, -5]
positives = []
for n in nums:
    if n > 0:
        positives.append(n)
positives                                # -> [4, 7]
[n for n in nums if n > 0]               # -> [4, 7]  # same thing as a list comprehension (see GoTo List.py §5)

# %% [markdown]
# ### Search: "is there one?" with a flag
# Start the flag at `False`, flip it to `True` when you find a match, and `break` if you don't need to keep looking.

# %%
plate = "AAA22A"
found_digit = False
for char in plate:
    if char.isdigit():
        found_digit = True
        break
found_digit                              # -> True

any(char.isdigit() for char in plate)    # -> True   # built-in shortcut
all(char.isalpha() for char in plate)    # -> False  # "every one?"

# %% [markdown]
# ### Find the biggest / smallest yourself

# %%
scores = [72, 95, 88]
best = scores[0]
for s in scores:
    if s > best:
        best = s
best                                     # -> 95
max(scores)                              # -> 95  # built-in shortcut


# %% [markdown]
# ## 13. Nested loops
# A loop inside a loop. The inner loop runs **completely** on every pass of the outer loop.
# (Lecture 2 `mario.py`)

# %%
for row in range(3):
    for col in range(4):
        print("#", end="")
    print()                              # end the row
# -> ####
# -> ####
# -> ####

for row in range(1, 4):                  # a staircase: the row number sets the width
    print("#" * row)
# -> #
# -> ##
# -> ###

grid = [[1, 2], [3, 4]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
# -> 1 2
# -> 3 4


# %% [markdown]
# ## 14. Pitfalls

# %% [markdown]
# ### `x == "a" or "b"` is always True
# Python reads it as `(x == "a") or ("b")`, and a non-empty string counts as True.
# Repeat the comparison on each side, or use `in`.

# %%
answer = "no"
bool(answer == "yes" or "y")                  # -> True   # WRONG: always True
answer == "yes" or answer == "y"              # -> False  # right
answer in ["yes", "y"]                        # -> False  # right, shorter

# %% [markdown]
# ### `=` vs `==`
# `=` stores a value. `==` asks "are these equal?". Writing `if x = 5:` is a `SyntaxError`.

# %% [markdown]
# ### `input()` always returns a string
# Convert it before comparing with numbers or doing math.

# %%
simulate_input("5")
age = input("Age: ")
# -> Age: 5
age == 5                                      # -> False  # "5" is not 5
int(age) == 5                                 # -> True

# %% [markdown]
# ### Capital letters matter
# Normalize the input with `.lower()` (and `.strip()` for spaces) before comparing, as in `bank.py`.

# %%
reply = "  HeLLo "
reply == "hello"                              # -> False
reply.strip().lower() == "hello"              # -> True

# %% [markdown]
# ### Infinite loops
# A `while` loop whose condition never becomes False runs forever. Stop it with **Ctrl-C**.
# Check that something in the loop changes the condition, or that a `break` can run.
#
# ```
# i = 0
# while i < 3:
#     print(i)        # forgot i += 1, so this never ends
# ```

# %% [markdown]
# ### Off by one
# `range(1, 10)` stops at **9**. Use `range(1, 11)` to include 10.
# `<` vs `<=` in a `while` condition changes the count by one too.

# %%
list(range(1, 10))[-1]                         # -> 9
list(range(1, 11))[-1]                         # -> 10

# %% [markdown]
# ### Changing a list while looping over it skips items
# Loop over a copy, or build a new list (see `GoTo List.py` §7).

# %%
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
nums                                           # -> [1, 2, 3]  # a 2 survived!
[n for n in [1, 2, 2, 3] if n != 2]            # -> [1, 3]

# %% [markdown]
# ### Comparing decimals with `==`
# Floats are stored approximately. Round first, or compare with a tolerance.

# %%
0.1 + 0.2 == 0.3                               # -> False
round(0.1 + 0.2, 2) == 0.3                     # -> True

# %% [markdown]
# ### Indentation decides what's inside the block
# Code indented under `if`, `for`, or `while` belongs to it. Un-indented code runs after it.

# %%
for n in range(3):
    print("inside", n)
print("after the loop")                        # runs once
# -> inside 0
# -> inside 1
# -> inside 2
# -> after the loop


# %% [markdown]
# ## 15. Which one do I use?
#
# **Loops**, in your own words from `camel.py`:
# *"FOR when we are doing something with each item. WHILE when we are waiting for something to change or happen."*
#
# | Situation | Use |
# |---|---|
# | Do something to **each** item in a string/list/dict | `for item in ...` |
# | Repeat a **known number** of times | `for _ in range(n)` |
# | Need the position too | `for i, item in enumerate(...)` |
# | Repeat **until** something happens (valid input, enough money, Ctrl-D) | `while` / `while True` + `break` |
# | Stop early once you've found the answer | `break` (or `return` in a function) |
# | Skip certain items but keep going | `continue` |
#
# **Decisions:**
#
# | Situation | Use |
# |---|---|
# | Yes/no | `if` / `else` |
# | Ranges or different kinds of tests | `if` / `elif` / `else` |
# | One value against exact options | `match` / `case` (or `in [...]`) |
# | Each option just maps to a value | a dict lookup |
# | Pick between two values in one line | `a if condition else b` |
