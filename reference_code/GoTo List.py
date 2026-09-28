# %% [markdown]
# # List (`list`) Reference
#
# A list is an **ordered**, **changeable** sequence. You find items by **position** (index), starting at 0.
# Companion file: `ref_dict.py`.
#
# Every code cell runs on its own. `# -> result` shows what a line returns or prints.
#
# 1. Cheat sheet
# 2. Basics: create, index, slice, change, add, remove, length, membership
# 3. Methods: every list method, what it returns, whether it mutates
# 4. Looping
# 5. Comprehensions
# 6. Common patterns: totals, map/filter, sorting, min/max, unique, grids, stacks, split/join, unpacking
# 7. Pitfalls
# 8. Which one do I want? list vs dict vs tuple vs set
#
# Sources: CS50P Lectures 2 and 4, Python docs ("Sequence Types: list", "Data Structures" tutorial),
# Think Python 3e Ch. 9 (Lists) and Ch. 11 (Tuples).


# %% [markdown]
# ## 1. Cheat sheet

# %%
nums = []                   # create an empty list
nums = [3, 1, 2]            # create with items

# nums[0]    nums[1]    nums[2]
#   3          1          2        <- index 0 is the first item
# nums[-3]   nums[-2]   nums[-1]   <- negative indexes count from the end

nums[0]                     # -> 3
nums[-1]                    # -> 2
nums[1:]                    # -> [1, 2]

nums.append(4)              # add one item to the end
nums.insert(0, 9)           # add at a position
nums.extend([5, 6])         # add several items to the end
nums                        # -> [9, 3, 1, 2, 4, 5, 6]

nums[0] = 8                 # change an item
nums.remove(8)              # delete by value (first match)
nums.pop()                  # -> 6
nums.pop(0)                 # -> 3
del nums[0]                 # delete by index
nums                        # -> [2, 4, 5]

4 in nums                   # -> True
len(nums)                   # -> 3
nums.index(5)               # -> 2
nums.count(2)               # -> 1
sorted(nums, reverse=True)  # -> [5, 4, 2]

for i, n in enumerate(nums):
    print(i, n)
# -> 0 2
# -> 1 4
# -> 2 5


# %% [markdown]
# ## 2. Basics
#
# ### Creating
# Lists can hold any types, even mixed, and can contain other lists.

# %%
empty = []
also_empty = list()

nums = [1, 2, 3]
mixed = ["spam", 2.0, 5, [10, 20]]     # anything goes, including a nested list
list("abc")                  # -> ['a', 'b', 'c']
list(range(5))               # -> [0, 1, 2, 3, 4]
list(range(2, 10, 3))        # -> [2, 5, 8]
[0] * 3                      # -> [0, 0, 0]
"a b c".split()              # -> ['a', 'b', 'c']
"a,b,c".split(",")           # -> ['a', 'b', 'c']
len(mixed)                   # -> 4  # the nested list counts as one item

# %% [markdown]
# ### Indexing
# `lst[i]` gets one item. Negative indexes count from the end.
# An index past the end raises `IndexError`.

# %%
cheeses = ["Cheddar", "Edam", "Gouda"]
cheeses[0]                   # -> 'Cheddar'
cheeses[-1]                  # -> 'Gouda'
cheeses[len(cheeses) - 1]    # -> 'Gouda'  # same thing, the long way

try:
    cheeses[3]
except IndexError as e:
    print("IndexError:", e)  # -> IndexError: list index out of range

grid = [[1, 2], [3, 4]]
grid[1][0]                   # -> 3  # row 1, column 0

# %% [markdown]
# ### Slicing: `lst[start:stop:step]`
# `stop` is **not included**. Leave out a part for "from the beginning" or "to the end".
# A slice always returns a **new list**, and a slice past the end doesn't raise.

# %%
letters = ["a", "b", "c", "d", "e", "f"]
letters[1:3]                 # -> ['b', 'c']
letters[:3]                  # -> ['a', 'b', 'c']  # first 3
letters[3:]                  # -> ['d', 'e', 'f']  # from index 3 on
letters[-2:]                 # -> ['e', 'f']  # last 2
letters[::2]                 # -> ['a', 'c', 'e']  # every 2nd
letters[::-1]                # -> ['f', 'e', 'd', 'c', 'b', 'a']  # reversed copy
letters[:]                   # -> ['a', 'b', 'c', 'd', 'e', 'f']  # full copy
letters[4:100]               # -> ['e', 'f']

# %% [markdown]
# ### Changing items
# Lists are **mutable**: you can change them in place. Strings aren't.

# %%
nums = [10, 20, 30, 40]
nums[0] = 11
nums                         # -> [11, 20, 30, 40]
nums[1:3] = [21, 31]         # replace a slice
nums                         # -> [11, 21, 31, 40]
nums[-1] += 1
nums                         # -> [11, 21, 31, 41]

# %% [markdown]
# ### Adding items

# %%
nums = [1, 2]
nums.append(3)               # one item at the end
nums                         # -> [1, 2, 3]
nums.extend([4, 5])          # each item from another list
nums                         # -> [1, 2, 3, 4, 5]
nums.insert(0, 0)            # at index 0; later items shift right
nums                         # -> [0, 1, 2, 3, 4, 5]
nums += [6]                  # same as extend
nums                         # -> [0, 1, 2, 3, 4, 5, 6]

[1, 2] + [3, 4]              # -> [1, 2, 3, 4]  # + makes a NEW list
[1, 2] * 2                   # -> [1, 2, 1, 2]

# %% [markdown]
# ### Removing items
# - Know the **value**? Use `remove`.
# - Know the **index** and want the item back? Use `pop`.
# - Know the index or slice and don't need it back? Use `del`.

# %%
nums = [10, 20, 30, 20, 40, 50]
nums.remove(20)              # first 20 only
nums                         # -> [10, 30, 20, 40, 50]
nums.pop()                   # -> 50  # last item
nums.pop(1)                  # -> 30
del nums[0]
nums                         # -> [20, 40]
del nums[:]                  # delete a slice (here, everything)
nums                         # -> []

nums = [1, 2]
try:
    nums.remove(99)
except ValueError:
    print("ValueError: 99 not in list")   # -> ValueError: 99 not in list

# %% [markdown]
# ### Length, membership, comparing

# %%
nums = [3, 1, 2]
len(nums)                    # -> 3
2 in nums                    # -> True
9 not in nums                # -> True
[1, 2] == [1, 2]             # -> True  # same items, same order
[1, 2] == [2, 1]             # -> False
[1, 2] < [1, 3]              # -> True  # compared item by item


# %% [markdown]
# ## 3. Methods
# **Almost every list method mutates the list and returns `None`.** Only `pop`, `index`, `count`, and `copy` return something useful.
#
# | Method | Returns | Mutates? |
# |---|---|---|
# | `lst.append(x)` | `None` | **yes** |
# | `lst.extend(iterable)` | `None` | **yes** |
# | `lst.insert(i, x)` | `None` | **yes** |
# | `lst.remove(x)` | `None` (ValueError if missing) | **yes** |
# | `lst.pop(i=-1)` | removed item (IndexError if empty) | **yes** |
# | `lst.clear()` | `None` | **yes** |
# | `lst.sort(key=None, reverse=False)` | `None` | **yes** |
# | `lst.reverse()` | `None` | **yes** |
# | `lst.index(x[, start[, stop]])` | index of first match (ValueError if missing) | no |
# | `lst.count(x)` | number of matches | no |
# | `lst.copy()` | new shallow copy | no |

# %% [markdown]
# ### `lst.append(x)`
# Adds **one** item to the end. If `x` is a list, it's added as a single nested item.

# %%
nums = [1, 2]
nums.append(3)
nums                         # -> [1, 2, 3]
nums.append([4, 5])
nums                         # -> [1, 2, 3, [4, 5]]

# %% [markdown]
# ### `lst.extend(iterable)`
# Adds **each** item from the iterable to the end.

# %%
nums = [1, 2]
nums.extend([3, 4])
nums                         # -> [1, 2, 3, 4]
letters = ["a"]
letters.extend("bc")         # a string is iterable
letters                      # -> ['a', 'b', 'c']

# %% [markdown]
# ### `lst.insert(i, x)`
# Inserts `x` **before** index `i`.

# %%
nums = [1, 2, 3]
nums.insert(1, 99)
nums                         # -> [1, 99, 2, 3]
nums.insert(len(nums), 100)  # same as append
nums                         # -> [1, 99, 2, 3, 100]

# %% [markdown]
# ### `lst.remove(x)`
# Removes the **first** item equal to `x`. Raises `ValueError` if there's none.

# %%
pets = ["cat", "dog", "cat"]
pets.remove("cat")
pets                         # -> ['dog', 'cat']
if "fish" in pets:           # check first to avoid ValueError
    pets.remove("fish")
pets                         # -> ['dog', 'cat']

# %% [markdown]
# ### `lst.pop(i=-1)`
# Removes and **returns** the item at `i` (the last item by default).

# %%
stack = ["a", "b", "c"]
stack.pop()                  # -> 'c'
stack.pop(0)                 # -> 'a'
stack                        # -> ['b']

# %% [markdown]
# ### `lst.clear()`
# Empties the list in place. Every variable pointing at it sees the empty list.

# %%
nums = [1, 2, 3]
alias = nums
nums.clear()
alias                        # -> []

# %% [markdown]
# ### `lst.sort(key=None, reverse=False)`
# Sorts **in place** and returns `None`. Use `sorted(lst)` when you want a new list and to keep the original.

# %%
nums = [3, 1, 2]
nums.sort()
nums                         # -> [1, 2, 3]
nums.sort(reverse=True)
nums                         # -> [3, 2, 1]

words = ["banana", "kiwi", "apple"]
words.sort(key=len)          # sort by length
words                        # -> ['kiwi', 'apple', 'banana']

# %% [markdown]
# ### `lst.reverse()`
# Reverses **in place** and returns `None`. Use `lst[::-1]` or `reversed(lst)` to leave the original alone.

# %%
nums = [1, 2, 3]
nums.reverse()
nums                         # -> [3, 2, 1]

# %% [markdown]
# ### `lst.index(x[, start[, stop]])`
# Position of the **first** match. Raises `ValueError` if it's not found.

# %%
letters = ["a", "b", "c", "b"]
letters.index("b")           # -> 1
letters.index("b", 2)        # -> 3  # search from index 2 on
"z" in letters and letters.index("z")   # -> False  # check first if it might be missing

# %% [markdown]
# ### `lst.count(x)`
# How many items equal `x`.

# %%
votes = ["yes", "no", "yes", "yes"]
votes.count("yes")           # -> 3
votes.count("maybe")         # -> 0

# %% [markdown]
# ### `lst.copy()`
# A **shallow** copy, the same as `lst[:]` or `list(lst)`. Nested lists are still shared. See §7.

# %%
nums = [1, 2, 3]
backup = nums.copy()
nums.append(4)
backup                       # -> [1, 2, 3]

# %% [markdown]
# ### Built-in functions that work on lists
# None of these change the list.

# %%
nums = [4, 1, 3, 2]
len(nums)                    # -> 4
sum(nums)                    # -> 10
min(nums)                    # -> 1
max(nums)                    # -> 4
sum(nums) / len(nums)        # -> 2.5  # average
sorted(nums)                 # -> [1, 2, 3, 4]
list(reversed(nums))         # -> [2, 3, 1, 4]
any(n > 3 for n in nums)     # -> True
all(n > 0 for n in nums)     # -> True
list(enumerate(["a", "b"]))  # -> [(0, 'a'), (1, 'b')]
list(zip([1, 2], ["a", "b"]))   # -> [(1, 'a'), (2, 'b')]
", ".join(["a", "b", "c"])   # -> 'a, b, c'  # list of strings -> one string
nums                         # -> [4, 1, 3, 2]  # unchanged


# %% [markdown]
# ## 4. Looping

# %%
students = ["Hermione", "Harry", "Ron"]

for student in students:                          # each item (most common)
    print(student)
# -> Hermione
# -> Harry
# -> Ron

for i, student in enumerate(students, start=1):   # item with a number
    print(i, student)
# -> 1 Hermione
# -> 2 Harry
# -> 3 Ron

for i in range(len(students)):                    # by index (CS50P Lecture 2); enumerate is usually cleaner
    print(i + 1, students[i])
# -> 1 Hermione
# -> 2 Harry
# -> 3 Ron

# %% [markdown]
# ### Pairing, reversing, sorting, and changing items while looping

# %%
names = ["Hermione", "Draco"]
houses = ["Gryffindor", "Slytherin"]
for name, house in zip(names, houses):     # two lists side by side; stops at the shorter
    print(name, house)
# -> Hermione Gryffindor
# -> Draco Slytherin

for name in reversed(names):
    print(name)
# -> Draco
# -> Hermione

for name in sorted(names):
    print(name)
# -> Draco
# -> Hermione

nums = [1, 2, 3]
for i in range(len(nums)):                 # need the index to CHANGE items in place
    nums[i] = nums[i] * 2
nums                                       # -> [2, 4, 6]

# %% [markdown]
# ### Nested lists (a grid)

# %%
grid = [[1, 2, 3], [4, 5, 6]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
# -> 1 2 3
# -> 4 5 6


# %% [markdown]
# ## 5. Comprehensions
# `[expr for item in iterable if condition]` builds a new list in one line.
# Put `if` **after** the loop to filter. Put `x if cond else y` **before** `for` to choose a value for each item.

# %%
nums = [1, 2, 3, 4, 5]
[n * 2 for n in nums]                        # -> [2, 4, 6, 8, 10]  # transform
[n for n in nums if n % 2 == 0]              # -> [2, 4]  # filter
["even" if n % 2 == 0 else "odd" for n in nums]   # -> ['odd', 'even', 'odd', 'even', 'odd']  # choose

words = ["  Hi ", "there  "]
[w.strip().upper() for w in words]           # -> ['HI', 'THERE']

grid = [[1, 2], [3, 4]]
[x for row in grid for x in row]             # -> [1, 2, 3, 4]  # flatten (loops read left to right)
[[0] * 3 for _ in range(2)]                  # -> [[0, 0, 0], [0, 0, 0]]  # safe way to build a grid

[len(w) for w in "the quick brown fox".split()]   # -> [3, 5, 5, 3]


# %% [markdown]
# ## 6. Common patterns
#
# ### Reduce, map, filter (Think Python)
# - **Reduce**: combine a list into one value.
# - **Map**: do the same thing to each item.
# - **Filter**: keep some items.

# %%
nums = [1, 2, 3, 4]

total = 0                                    # reduce
for n in nums:
    total += n
total                                        # -> 10
sum(nums)                                    # -> 10  # built-in version

words = ["spam", "eggs"]
result = []                                  # map
for w in words:
    result.append(w.capitalize())
result                                       # -> ['Spam', 'Eggs']
[w.capitalize() for w in words]              # -> ['Spam', 'Eggs']  # comprehension version

evens = []                                   # filter
for n in nums:
    if n % 2 == 0:
        evens.append(n)
evens                                        # -> [2, 4]
[n for n in nums if n % 2 == 0]              # -> [2, 4]

# %% [markdown]
# ### Sorting with `key=` (see also ref_dict.py §6)
# `key` is a function applied to each item, and the list is sorted by those results.
# `lambda item: ...` is a one-line throwaway function.

# %%
words = ["banana", "apple", "Cherry"]
sorted(words)                                # -> ['Cherry', 'apple', 'banana']  # uppercase sorts first
sorted(words, key=str.lower)                 # -> ['apple', 'banana', 'Cherry']  # ignore case
sorted(words, key=len)                       # -> ['apple', 'banana', 'Cherry']
sorted(words, key=len, reverse=True)         # -> ['banana', 'Cherry', 'apple']

pairs = [("Bob", 87), ("Alice", 95), ("Carol", 78)]
sorted(pairs)                                # -> [('Alice', 95), ('Bob', 87), ('Carol', 78)]  # by first item
sorted(pairs, key=lambda p: p[1])            # -> [('Carol', 78), ('Bob', 87), ('Alice', 95)]  # by second item

students = [{"name": "Harry", "year": 2}, {"name": "Draco", "year": 1}]
[s["name"] for s in sorted(students, key=lambda s: s["year"])]   # -> ['Draco', 'Harry']

# %% [markdown]
# ### Min / max / top N

# %%
pairs = [("Bob", 87), ("Alice", 95), ("Carol", 78)]
max(pairs, key=lambda p: p[1])               # -> ('Alice', 95)
min(pairs, key=lambda p: p[1])               # -> ('Carol', 78)
sorted(pairs, key=lambda p: p[1], reverse=True)[:2]   # -> [('Alice', 95), ('Bob', 87)]  # top 2

words = ["kiwi", "banana", "fig"]
max(words, key=len)                          # -> 'banana'
max([], default=None)                        # -> None  # avoids ValueError on an empty list

# %% [markdown]
# ### Remove duplicates
# `set()` loses the order. `dict.fromkeys()` keeps it.

# %%
names = ["Ron", "Harry", "Ron", "Hermione", "Harry"]
list(dict.fromkeys(names))                   # -> ['Ron', 'Harry', 'Hermione']  # keeps first-seen order
sorted(set(names))                           # -> ['Harry', 'Hermione', 'Ron']
len(set(names))                              # -> 3  # how many unique

# %% [markdown]
# ### Counting items
# Use `.count(x)` for one value. To count every value, use a dict (see ref_dict.py §6).

# %%
from collections import Counter
votes = ["yes", "no", "yes"]
votes.count("yes")                           # -> 2
Counter(votes)                               # -> Counter({'yes': 2, 'no': 1})

# %% [markdown]
# ### Grids: a list of lists (CS50P Lecture 2 Mario)

# %%
size = 3
grid = [["#"] * size for _ in range(size)]
grid[1][1] = "."
for row in grid:
    print("".join(row))
# -> ###
# -> #.#
# -> ###

# %% [markdown]
# ### Stack and queue
# A stack is last in, first out: `append` + `pop()`.
# A queue is first in, first out: `append` + `pop(0)`, or `collections.deque` for big queues.

# %%
stack = []
stack.append("a")
stack.append("b")
stack.pop()                                  # -> 'b'

queue = ["a", "b"]
queue.append("c")
queue.pop(0)                                 # -> 'a'

from collections import deque
q = deque(["a", "b"])
q.append("c")
q.popleft()                                  # -> 'a'

# %% [markdown]
# ### Strings ↔ lists (Think Python)
# `str.split()` breaks a string into a list. `sep.join(list)` glues a list of strings back together.
# `list(s)` gives the characters.

# %%
line = "pining for the fjords"
words = line.split()
words                                        # -> ['pining', 'for', 'the', 'fjords']
" ".join(words)                              # -> 'pining for the fjords'
"-".join(words)                              # -> 'pining-for-the-fjords'
"2024-01-15".split("-")                      # -> ['2024', '01', '15']
list("spam")                                 # -> ['s', 'p', 'a', 'm']
", ".join(str(n) for n in [1, 2, 3])         # -> '1, 2, 3'  # join needs strings

# %% [markdown]
# ### Unpacking (Think Python Ch. 11)
# Assign list or tuple items to separate names in one step. `*` collects the rest.

# %%
point = [3, 4]
x, y = point
x                                            # -> 3
first, *rest = [1, 2, 3, 4]
rest                                         # -> [2, 3, 4]
*init, last = [1, 2, 3, 4]
last                                         # -> 4
a, b = 1, 2
a, b = b, a                                  # swap
[a, b]                                       # -> [2, 1]
print(*["a", "b", "c"])                      # -> a b c  # * spreads a list into arguments

# %% [markdown]
# ### Command-line arguments are a list (CS50P Lecture 4)
# `sys.argv` is a list of strings. `sys.argv[1:]` slices off the script name.

# %%
argv = ["name.py", "David", "Carter"]        # what sys.argv looks like for: python name.py David Carter
for arg in argv[1:]:
    print("hello, my name is", arg)
# -> hello, my name is David
# -> hello, my name is Carter


# %% [markdown]
# ## 7. Pitfalls

# %% [markdown]
# ### `.sort()` returns `None`
# In-place methods return `None`, so don't assign their result.

# %%
nums = [3, 1, 2]
result = nums.sort()
print(result)                                # -> None
nums                                         # -> [1, 2, 3]  # the list itself was sorted

nums = [3, 1, 2]
result = sorted(nums)                        # use sorted() for a new list
result                                       # -> [1, 2, 3]

# %% [markdown]
# ### Aliasing (Think Python) (see also ref_dict.py §7)
# `b = a` doesn't copy. Both names point to the **same** list.
# `is` checks whether two names are the same object. `==` checks whether the contents are equal.

# %%
a = [1, 2, 3]
b = a
b[0] = 99
a                                            # -> [99, 2, 3]
a is b                                       # -> True

c = a.copy()                                 # or a[:] or list(a)
c[0] = 1
a                                            # -> [99, 2, 3]
a == [99, 2, 3]                              # -> True
a is c                                       # -> False

# %% [markdown]
# ### Functions can change a list you pass in (Think Python)
# The parameter is an alias for the caller's list. Mutating it changes the original. Reassigning it doesn't.

# %%
def delete_head(t):
    del t[0]                                 # mutates the caller's list

letters = ["a", "b", "c"]
delete_head(letters)
letters                                      # -> ['b', 'c']

def bad_delete_head(t):
    t = t[1:]                                # makes a NEW list; caller's list is untouched

letters = ["a", "b", "c"]
bad_delete_head(letters)
letters                                      # -> ['a', 'b', 'c']

def tail(t):
    return t[1:]                             # better: return a new list

tail(["a", "b", "c"])                        # -> ['b', 'c']

# %% [markdown]
# ### `append` vs `+` vs `extend`
# - `t.append(x)` and `t += [x]` change `t` in place.
# - `t = t + [x]` builds a new list, so other names still see the old one.

# %%
t = [1, 2]
alias = t
t = t + [3]                                  # new list
alias                                        # -> [1, 2]

t = [1, 2]
alias = t
t += [3]                                     # in place
alias                                        # -> [1, 2, 3]

t = [1]
t.append([2, 3])                             # adds ONE item, a list
t                                            # -> [1, [2, 3]]

# %% [markdown]
# ### Shallow vs deep copy, and the grid trap
# `[[0] * 3] * 3` repeats the **same** inner list 3 times. Build grids with a comprehension instead.

# %%
import copy

bad = [[0] * 3] * 3
bad[0][0] = 1
bad                                          # -> [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

good = [[0] * 3 for _ in range(3)]
good[0][0] = 1
good                                         # -> [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

grid = [[1, 2], [3, 4]]
shallow = grid.copy()
shallow[0].append(99)                        # inner lists are shared
grid                                         # -> [[1, 2, 99], [3, 4]]

grid = [[1, 2], [3, 4]]
deep = copy.deepcopy(grid)
deep[0].append(99)
grid                                         # -> [[1, 2], [3, 4]]

# %% [markdown]
# ### Removing while looping skips items
# Removing an item shifts the rest left, so the loop steps over the next one.
# Build a new list, or loop over a copy.

# %%
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
nums                                         # -> [1, 2, 3]  # one 2 was skipped!

nums = [1, 2, 2, 3]
nums = [n for n in nums if n != 2]           # build a new list
nums                                         # -> [1, 3]

nums = [1, 2, 2, 3]
for n in nums[:]:                            # or loop over a copy
    if n == 2:
        nums.remove(n)
nums                                         # -> [1, 3]

# %% [markdown]
# ### Mutable default arguments
# A default `[]` is created **once** and shared by every call. Use `None` instead.

# %%
def add_item_bad(item, items=[]):
    items.append(item)
    return items

add_item_bad("a")                            # -> ['a']
add_item_bad("b")                            # -> ['a', 'b']  # 'a' leaked in from the last call

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

add_item("a")                                # -> ['a']
add_item("b")                                # -> ['b']

# %% [markdown]
# ### Off-by-one and empty lists
# The last index is `len(lst) - 1`. `range(len(lst))` already stops there.
# `min`, `max`, and `pop` fail on an empty list, and `sum` returns 0.

# %%
nums = [10, 20, 30]
nums[len(nums) - 1]                          # -> 30
list(range(len(nums)))                       # -> [0, 1, 2]

empty = []
sum(empty)                                   # -> 0
if empty:                                    # an empty list is falsy
    print("has items")
else:
    print("empty")                           # -> empty

# %% [markdown]
# ### String methods return new strings, list methods mutate (Think Python)

# %%
word = "spam"
word.upper()                                 # -> 'SPAM'
word                                         # -> 'spam'  # unchanged; you must assign: word = word.upper()

letters = ["b", "a"]
letters.sort()
letters                                      # -> ['a', 'b']  # changed in place


# %% [markdown]
# ## 8. Which one do I want?
#
# | Need | Use | Example |
# |---|---|---|
# | An **ordered** sequence you add to, sort, or index by position | `list` | `names[0]`, `names.append(x)` |
# | Look up a value by **name/label** | `dict` | `ages["Alice"]` (see ref_dict.py) |
# | A **fixed** group of values that won't change, or a dict key | `tuple` | `point = (3, 4)` |
# | **Unique** items / fast "have I seen this?" / no duplicates | `set` | `seen.add(x)`, `x in seen` |
# | Many records with named fields | list of dicts | `students[0]["name"]` |
# | A 2-D grid | list of lists | `grid[row][col]` |
#
# Rule of thumb: ask **"How will I find things?"** By position → list. By name → dict.
# If you keep writing `for item in lst: if item["name"] == x:`, you probably want a dict keyed by name.
# Tuples work like read-only lists: indexing, slicing, `in`, `len`, `count`, and `index` all work, but nothing that changes them.

# %%
point = (3, 4)
point[0]                                     # -> 3
try:
    point[0] = 5
except TypeError:
    print("TypeError: tuples can't be changed")   # -> TypeError: tuples can't be changed

seen = set()
for n in [1, 2, 1, 3]:
    if n in seen:
        print("duplicate:", n)
    seen.add(n)
# -> duplicate: 1

list((1, 2))                                 # -> [1, 2]  # convert tuple -> list
tuple([1, 2])                                # -> (1, 2)  # list -> tuple
