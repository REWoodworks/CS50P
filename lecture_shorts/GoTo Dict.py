# %% [markdown]
# # Dictionary (`dict`) Reference
#
# A dict maps **keys** to **values**. Look things up by name instead of by position.
# Companion file: `ref_list.py`.
#
# Every code cell runs on its own. `# -> result` shows what a line returns or prints.
#
# 1. Cheat sheet
# 2. Basics: create, access, add/change, remove, length, membership
# 3. Methods: every dict method, what it returns, whether it mutates
# 4. Looping
# 5. Comprehensions
# 6. Common patterns: counting, grouping, lookup tables, sorting, nesting
# 7. Pitfalls
# 8. Which one do I want? dict vs list vs tuple vs set
#
# Sources: CS50P Lectures 2 and 4, Python docs ("Mapping Types: dict", "Data Structures" tutorial),
# Think Python 3e Ch. 10 (Dictionaries) and Ch. 11 (Tuples).


# %% [markdown]
# ## 1. Cheat sheet

# %%
scores = {}                        # create an empty dict
scores = {"Alice": 95, "Bob": 87}  # create with entries

# scores["Alice"] = 95
#        key       value

scores["Carol"] = 78               # add a new entry
scores["Alice"] = 98               # change an existing entry

scores["Alice"]                    # -> 98
scores.get("Dave")                 # -> None
scores.get("Dave", 0)              # -> 0

"Bob" in scores                    # -> True
"Dave" not in scores               # -> True
len(scores)                        # -> 3

scores.keys()                      # -> dict_keys(['Alice', 'Bob', 'Carol'])
scores.values()                    # -> dict_values([98, 87, 78])
scores.items()                     # -> dict_items([('Alice', 98), ('Bob', 87), ('Carol', 78)])

del scores["Carol"]                # delete (KeyError if missing)
scores.pop("Bob")                  # -> 87
scores.pop("Zed", None)            # -> None  # safe delete: no KeyError
scores                             # -> {'Alice': 98}

for name, score in scores.items():
    print(name, score)
# -> Alice 98


# %% [markdown]
# ## 2. Basics
#
# ### Creating
# - Keys must be **hashable** (unchangeable): `str`, `int`, `float`, `bool`, `tuple`. Not `list` or `dict`.
# - Values can be anything, including lists and other dicts.
# - Dicts remember **insertion order**.
# - A key can only appear once. A repeated key keeps the last value.

# %%
empty = {}
also_empty = dict()

scores = {"Alice": 95, "Bob": 87}
from_pairs = dict([("a", 1), ("b", 2)])        # from a list of (key, value) tuples
from_keywords = dict(a=1, b=2)                 # keys become strings
from_zip = dict(zip(["a", "b"], [1, 2]))       # pair up two lists (see ref_list.py §4)
from_keys = dict.fromkeys(["a", "b"], 0)       # same starting value for every key

scores          # -> {'Alice': 95, 'Bob': 87}
from_pairs      # -> {'a': 1, 'b': 2}
from_keywords   # -> {'a': 1, 'b': 2}
from_zip        # -> {'a': 1, 'b': 2}
from_keys       # -> {'a': 0, 'b': 0}
{"a": 1, "a": 2}  # -> {'a': 2}

# %% [markdown]
# ### Accessing
# `d[key]` raises `KeyError` if the key is missing. `d.get(key, default)` never raises.

# %%
scores = {"Alice": 95, "Bob": 87}

scores["Alice"]           # -> 95
scores.get("Alice")       # -> 95
scores.get("Zed")         # -> None
scores.get("Zed", 0)      # -> 0

try:
    scores["Zed"]
except KeyError as e:
    print("KeyError", e)  # -> KeyError 'Zed'

# %% [markdown]
# ### Adding and changing
# Assigning to a key adds it if it's new and replaces the value if it exists.

# %%
scores = {"Alice": 95}

scores["Bob"] = 87                    # add
scores["Alice"] = 98                  # change
scores                                # -> {'Alice': 98, 'Bob': 87}

scores.update({"Carol": 78, "Bob": 90})   # add/change several at once
scores                                # -> {'Alice': 98, 'Bob': 90, 'Carol': 78}

scores["Alice"] += 1                  # update a value based on itself
scores["Alice"]                       # -> 99

# %% [markdown]
# ### Removing

# %%
scores = {"Alice": 95, "Bob": 87, "Carol": 78, "Dave": 60}

del scores["Alice"]          # remove (KeyError if missing)
scores.pop("Bob")            # -> 87
scores.pop("Zed", None)      # -> None  # returns default instead of KeyError
scores.popitem()             # -> ('Dave', 60)  # removes the LAST inserted pair
scores                       # -> {'Carol': 78}
scores.clear()               # remove everything
scores                       # -> {}

# %% [markdown]
# ### Length and membership
# `in` checks **keys**, not values. To search values, use `in d.values()`.

# %%
scores = {"Alice": 95, "Bob": 87}

len(scores)                # -> 2
"Alice" in scores          # -> True
95 in scores               # -> False
95 in scores.values()      # -> True
("Bob", 87) in scores.items()  # -> True


# %% [markdown]
# ## 3. Methods
#
# | Method | Returns | Mutates? |
# |---|---|---|
# | `d.get(k, default=None)` | value or default | no |
# | `d.keys()` / `d.values()` / `d.items()` | live view | no |
# | `d.update(other)` | `None` | **yes** |
# | `d.setdefault(k, default=None)` | value (inserts default if missing) | **yes** if missing |
# | `d.pop(k[, default])` | removed value | **yes** |
# | `d.popitem()` | last `(key, value)` pair | **yes** |
# | `d.clear()` | `None` | **yes** |
# | `d.copy()` | new shallow copy | no |
# | `dict.fromkeys(keys, value=None)` | new dict | no |
# | `d1 \| d2` | new merged dict | no |
# | `d1 \|= d2` | (same as update) | **yes** |

# %% [markdown]
# ### `d.get(key, default=None)`
# Returns the value, or `default` if the key is missing. Never raises `KeyError`.

# %%
stock = {"apples": 3}
stock.get("apples")        # -> 3
stock.get("pears")         # -> None
stock.get("pears", 0)      # -> 0
stock                      # -> {'apples': 3}

# %% [markdown]
# ### `d.keys()`, `d.values()`, `d.items()`
# Return **views**: live windows onto the dict that update when the dict changes.
# Wrap them in `list()` if you need to index them or keep a snapshot.

# %%
stock = {"apples": 3, "pears": 5}
keys = stock.keys()
keys                       # -> dict_keys(['apples', 'pears'])
stock["plums"] = 2
keys                       # -> dict_keys(['apples', 'pears', 'plums'])  # view updated itself
list(stock.values())       # -> [3, 5, 2]
list(stock.items())        # -> [('apples', 3), ('pears', 5), ('plums', 2)]
list(stock)[0]             # -> 'apples'  # first key

# %% [markdown]
# ### `d.update(other)`
# Adds or overwrites entries from another dict (or from keyword arguments). Returns `None`.

# %%
stock = {"apples": 3, "pears": 5}
stock.update({"pears": 10, "plums": 2})
stock                      # -> {'apples': 3, 'pears': 10, 'plums': 2}
stock.update(kiwis=4)
stock                      # -> {'apples': 3, 'pears': 10, 'plums': 2, 'kiwis': 4}
print(stock.update({}))    # -> None

# %% [markdown]
# ### `d.setdefault(key, default=None)`
# If the key exists, returns its value. If not, **inserts** `key: default` and returns `default`.
# Useful for building dicts of lists (see §6 Grouping).

# %%
stock = {"apples": 3}
stock.setdefault("apples", 0)   # -> 3
stock.setdefault("pears", 0)    # -> 0
stock                           # -> {'apples': 3, 'pears': 0}

# %% [markdown]
# ### `d.pop(key[, default])`
# Removes the key and returns its value. Raises `KeyError` if missing unless you give a default.

# %%
stock = {"apples": 3, "pears": 5}
stock.pop("apples")          # -> 3
stock.pop("kiwis", 0)        # -> 0
stock                        # -> {'pears': 5}

# %% [markdown]
# ### `d.popitem()`
# Removes and returns the **last inserted** `(key, value)` pair. `KeyError` if the dict is empty.

# %%
stock = {"apples": 3, "pears": 5}
stock.popitem()              # -> ('pears', 5)
stock                        # -> {'apples': 3}

# %% [markdown]
# ### `d.clear()`
# Empties the dict in place. Every variable pointing at it sees the empty dict.

# %%
stock = {"apples": 3}
alias = stock
stock.clear()
alias                        # -> {}

# %% [markdown]
# ### `d.copy()`
# A **shallow** copy: a new dict, but nested lists/dicts inside are still shared. See §7.

# %%
stock = {"apples": 3}
backup = stock.copy()
stock["apples"] = 0
backup                       # -> {'apples': 3}

# %% [markdown]
# ### `dict.fromkeys(keys, value=None)`
# Builds a new dict with every key set to the same value.
# Use it only with immutable values like `0`, `None` or `""`. See §7 for the list trap.

# %%
dict.fromkeys(["a", "b", "c"])       # -> {'a': None, 'b': None, 'c': None}
dict.fromkeys(["a", "b", "c"], 0)    # -> {'a': 0, 'b': 0, 'c': 0}
dict.fromkeys("hello", 0)            # -> {'h': 0, 'e': 0, 'l': 0, 'o': 0}

# %% [markdown]
# ### Merge operators `|` and `|=`
# `d1 | d2` returns a **new** dict. On clashes, the right side wins. `d1 |= d2` updates `d1` in place.

# %%
defaults = {"color": "red", "size": "M"}
choice = {"size": "L"}
defaults | choice            # -> {'color': 'red', 'size': 'L'}
{**defaults, **choice}       # -> {'color': 'red', 'size': 'L'}  # older way, same result
defaults                     # -> {'color': 'red', 'size': 'M'}  # unchanged
defaults |= choice
defaults                     # -> {'color': 'red', 'size': 'L'}

# %% [markdown]
# ### Built-in functions that work on dicts
# These act on the **keys** unless you pass `.values()` or `.items()`.

# %%
scores = {"Bob": 87, "Alice": 95, "Carol": 78}
len(scores)                          # -> 3
sorted(scores)                       # -> ['Alice', 'Bob', 'Carol']
list(reversed(scores))               # -> ['Carol', 'Alice', 'Bob']
max(scores)                          # -> 'Carol'  # alphabetically last key
max(scores.values())                 # -> 95
max(scores, key=scores.get)          # -> 'Alice'  # key with the highest value
sum(scores.values())                 # -> 260
sum(scores.values()) / len(scores)   # -> 86.66666666666667
any(v < 80 for v in scores.values()) # -> True
all(v > 70 for v in scores.values()) # -> True


# %% [markdown]
# ## 4. Looping
# Looping over a dict gives you its **keys**. Use `.items()` to get key and value together.

# %%
scores = {"Alice": 95, "Bob": 87}

for name in scores:                     # keys
    print(name)
# -> Alice
# -> Bob

for name, score in scores.items():      # key and value (most common)
    print(f"{name}: {score}")
# -> Alice: 95
# -> Bob: 87

for score in scores.values():           # values only
    print(score)
# -> 95
# -> 87

# %% [markdown]
# ### Sorted order, numbering, and pairing lists

# %%
scores = {"Bob": 87, "Alice": 95, "Carol": 78}

for name in sorted(scores):                            # by key
    print(name, scores[name])
# -> Alice 95
# -> Bob 87
# -> Carol 78

for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):   # by value, high to low
    print(name, score)
# -> Alice 95
# -> Bob 87
# -> Carol 78

for rank, (name, score) in enumerate(scores.items(), start=1):   # numbered
    print(rank, name, score)
# -> 1 Bob 87
# -> 2 Alice 95
# -> 3 Carol 78

names = ["Hermione", "Harry"]
houses = ["Gryffindor", "Gryffindor"]
for name, house in zip(names, houses):                 # walk two lists together
    print(name, house)
# -> Hermione Gryffindor
# -> Harry Gryffindor

# %% [markdown]
# ### Looping over a list of dicts (CS50P Lecture 2)

# %%
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student in students:
    print(student["name"], student["house"], sep=", ")
# -> Hermione, Gryffindor
# -> Harry, Gryffindor
# -> Draco, Slytherin


# %% [markdown]
# ## 5. Comprehensions
# `{key_expr: value_expr for item in iterable if condition}` builds a new dict in one line.

# %%
names = ["Alice", "Bob", "Carol"]
{name: len(name) for name in names}                # -> {'Alice': 5, 'Bob': 3, 'Carol': 5}
{n: n ** 2 for n in range(1, 5)}                   # -> {1: 1, 2: 4, 3: 9, 4: 16}

scores = {"Alice": 95, "Bob": 87, "Carol": 78}
{k: v for k, v in scores.items() if v >= 80}       # -> {'Alice': 95, 'Bob': 87}  # filter
{k: v + 5 for k, v in scores.items()}              # -> {'Alice': 100, 'Bob': 92, 'Carol': 83}  # transform values
{k.upper(): v for k, v in scores.items()}          # -> {'ALICE': 95, 'BOB': 87, 'CAROL': 78}  # transform keys
{v: k for k, v in scores.items()}                  # -> {95: 'Alice', 87: 'Bob', 78: 'Carol'}  # swap (values must be unique)


# %% [markdown]
# ## 6. Common patterns
#
# ### Counting (Think Python `value_counts`)
# Three ways to count: an explicit `if`, `.get(key, 0) + 1`, or `collections.Counter`.

# %%
word = "brontosaurus"

counts = {}
for letter in word:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1
counts        # -> {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1    # same result, one line
counts        # -> {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

from collections import Counter
Counter(word).most_common(2)                      # -> [('r', 2), ('o', 2)]

# %% [markdown]
# ### Grouping: a dict of lists
# Collect items under a shared key.

# %%
students = [("Hermione", "Gryffindor"), ("Draco", "Slytherin"), ("Harry", "Gryffindor")]

by_house = {}
for name, house in students:
    by_house.setdefault(house, []).append(name)   # create the list the first time
by_house      # -> {'Gryffindor': ['Hermione', 'Harry'], 'Slytherin': ['Draco']}

from collections import defaultdict
by_house = defaultdict(list)                      # missing keys start as []
for name, house in students:
    by_house[house].append(name)
dict(by_house)  # -> {'Gryffindor': ['Hermione', 'Harry'], 'Slytherin': ['Draco']}

# %% [markdown]
# ### Lookup table
# Replace a long `if/elif` chain with a dict (compare CS50P Lecture 1 `match`).

# %%
houses = {"Harry": "Gryffindor", "Hermione": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}
houses.get("Draco", "Who?")   # -> 'Slytherin'
houses.get("Neville", "Who?") # -> 'Who?'

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

operations = {"+": add, "-": sub}     # values can be functions
operations["+"](3, 4)                 # -> 7

# %% [markdown]
# ### Reverse lookup and inverting (Think Python)
# Dicts look up **key → value** quickly. Going **value → key** means a loop.

# %%
scores = {"Alice": 95, "Bob": 87, "Carol": 95}

def reverse_lookup(d, value):
    for key in d:
        if d[key] == value:
            return key
    return None

reverse_lookup(scores, 87)     # -> 'Bob'

def invert_dict(d):             # values become keys, each mapping to a list of original keys
    inverse = {}
    for key, value in d.items():
        inverse.setdefault(value, []).append(key)
    return inverse

invert_dict(scores)            # -> {95: ['Alice', 'Carol'], 87: ['Bob']}

# %% [markdown]
# ### Sorting (see also ref_list.py §6)
# A dict has no `.sort()`. Use `sorted()`, which returns a **list**. Wrap it in `dict()` to get a dict back.

# %%
scores = {"Bob": 87, "Alice": 95, "Carol": 78}
sorted(scores)                                              # -> ['Alice', 'Bob', 'Carol']
sorted(scores.items(), key=lambda item: item[1])            # -> [('Carol', 78), ('Bob', 87), ('Alice', 95)]
dict(sorted(scores.items()))                                # -> {'Alice': 95, 'Bob': 87, 'Carol': 78}
dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))   # -> {'Alice': 95, 'Bob': 87, 'Carol': 78}
sorted(scores, key=scores.get, reverse=True)[:2]            # -> ['Alice', 'Bob']  # top 2 keys

# %% [markdown]
# ### List of dicts: records (CS50P Lecture 2)
# Each dict is one record. Sort, filter, or pull out one field.

# %%
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Harry", "house": "Gryffindor"},
]
[s["name"] for s in students]                                   # -> ['Hermione', 'Draco', 'Harry']
[s["name"] for s in students if s["house"] == "Gryffindor"]     # -> ['Hermione', 'Harry']
[s["name"] for s in sorted(students, key=lambda s: s["name"])]  # -> ['Draco', 'Harry', 'Hermione']
students.append({"name": "Ron", "house": "Gryffindor"})
len(students)                                                   # -> 4

# %% [markdown]
# ### Dict of lists / nested dicts
# Chain the lookups: `d[outer][inner]`. Use `.get(..., {})` to walk safely through missing keys.

# %%
grades = {"Alice": [90, 85], "Bob": [70]}
grades["Alice"].append(100)
grades["Alice"]                         # -> [90, 85, 100]
sum(grades["Alice"]) / len(grades["Alice"])   # -> 91.66666666666667

people = {
    "Harry": {"house": "Gryffindor", "pets": ["Hedwig"]},
    "Draco": {"house": "Slytherin", "pets": []},
}
people["Harry"]["house"]                # -> 'Gryffindor'
people["Harry"]["pets"][0]              # -> 'Hedwig'
people.get("Ron", {}).get("house")      # -> None  # safe: no KeyError at either level

# %% [markdown]
# ### JSON from an API (CS50P Lecture 4 `itunes2.py`)
# `response.json()` returns nested dicts and lists. Use the same indexing and loops as above.

# %%
data = {"resultCount": 2, "results": [{"trackName": "Song A"}, {"trackName": "Song B"}]}
for result in data["results"]:
    print(result["trackName"])
# -> Song A
# -> Song B

# %% [markdown]
# ### Tuples as keys (Think Python Ch. 11)
# Use a tuple when the key has more than one part. A list won't work as a key.

# %%
phone = {("Doe", "John"): "555-1234", ("Doe", "Jane"): "555-9876"}
phone[("Doe", "Jane")]                  # -> '555-9876'
for (last, first), number in phone.items():
    print(first, last, number)
# -> John Doe 555-1234
# -> Jane Doe 555-9876

# %% [markdown]
# ### Memoization (Think Python)
# Store results you've already computed so you don't redo the work.

# %%
known = {0: 0, 1: 1}

def fibonacci(n):
    if n in known:
        return known[n]
    known[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return known[n]

fibonacci(50)          # -> 12586269025


# %% [markdown]
# ## 7. Pitfalls

# %% [markdown]
# ### `KeyError` vs `.get()`
# Use `d[key]` when the key *must* exist, so a bug fails loudly.
# Use `.get()` when a missing key is normal.
# Watch out: `if d.get(k):` is also False when the value is `0` or `""`. Use `if k in d:` to test for the key.

# %%
stock = {"apples": 0}
if stock.get("apples"):
    print("found by get")
if "apples" in stock:
    print("found by in")
# -> found by in

# %% [markdown]
# ### Aliasing vs copying (see also ref_list.py §7)
# `b = a` makes a second **name** for the same dict, not a copy.
# `.copy()` copies only the top level. Nested lists are still shared.
# `copy.deepcopy()` copies everything.

# %%
import copy

a = {"name": "Harry", "pets": ["Hedwig"]}
b = a                          # alias: same object
b["name"] = "Ron"
a["name"]                      # -> 'Ron'
a is b                         # -> True

a = {"name": "Harry", "pets": ["Hedwig"]}
shallow = a.copy()
shallow["name"] = "Ron"        # top level: independent
shallow["pets"].append("Owl")  # nested list: SHARED
a                              # -> {'name': 'Harry', 'pets': ['Hedwig', 'Owl']}

a = {"name": "Harry", "pets": ["Hedwig"]}
deep = copy.deepcopy(a)
deep["pets"].append("Owl")
a                              # -> {'name': 'Harry', 'pets': ['Hedwig']}

# %% [markdown]
# ### Changing size while looping
# Adding or removing keys while looping raises `RuntimeError`. Loop over a copy of the keys, or build a new dict.

# %%
scores = {"Alice": 95, "Bob": 60, "Carol": 55}
try:
    for name in scores:
        if scores[name] < 70:
            del scores[name]
except RuntimeError as e:
    print("RuntimeError:", e)  # -> RuntimeError: dictionary changed size during iteration

scores = {"Alice": 95, "Bob": 60, "Carol": 55}
for name in list(scores):      # loop over a snapshot of the keys
    if scores[name] < 70:
        del scores[name]
scores                         # -> {'Alice': 95}

scores = {"Alice": 95, "Bob": 60, "Carol": 55}
{k: v for k, v in scores.items() if v >= 70}   # -> {'Alice': 95}  # or build a new one

# %% [markdown]
# ### `fromkeys` with a mutable value
# Every key shares the **same** list object.

# %%
bad = dict.fromkeys(["a", "b"], [])
bad["a"].append(1)
bad                            # -> {'a': [1], 'b': [1]}

good = {k: [] for k in ["a", "b"]}   # a fresh list per key
good["a"].append(1)
good                           # -> {'a': [1], 'b': []}

# %% [markdown]
# ### Mutable default arguments
# A default `{}` or `[]` is created **once**, when the function is defined, and shared by every call.

# %%
def add_score_bad(name, score, book={}):
    book[name] = score
    return book

add_score_bad("Alice", 95)     # -> {'Alice': 95}
add_score_bad("Bob", 87)       # -> {'Alice': 95, 'Bob': 87}  # Alice leaked in from the last call

def add_score(name, score, book=None):
    if book is None:
        book = {}
    book[name] = score
    return book

add_score("Alice", 95)         # -> {'Alice': 95}
add_score("Bob", 87)           # -> {'Bob': 87}

# %% [markdown]
# ### Other gotchas
# - Views aren't lists, so `d.keys()[0]` fails. Use `list(d)[0]`.
# - Lists can't be keys. Use a tuple.
# - `in` checks keys, not values (see §2).

# %%
d = {"a": 1}
try:
    d.keys()[0]
except TypeError:
    print("TypeError: views can't be indexed")   # -> TypeError: views can't be indexed
list(d)[0]                                       # -> 'a'

try:
    {["x", "y"]: 1}
except TypeError:
    print("TypeError: list can't be a key")      # -> TypeError: list can't be a key
{("x", "y"): 1}                                  # -> {('x', 'y'): 1}


# %% [markdown]
# ## 8. Which one do I want?
#
# | Need | Use | Example |
# |---|---|---|
# | Look up a value by **name/label** | `dict` | `ages["Alice"]` |
# | An **ordered** sequence you add to, sort, or index by position | `list` | `names[0]`, `names.append(x)` |
# | A **fixed** group of values that won't change, or a dict key | `tuple` | `point = (3, 4)` |
# | **Unique** items / fast "have I seen this?" / no duplicates | `set` | `seen.add(x)`, `x in seen` |
# | Many records with named fields | list of dicts | `students[0]["name"]` |
# | Many items grouped under a label | dict of lists | `by_house["Gryffindor"]` |
#
# Rule of thumb: ask **"How will I find things?"** By position → list. By name → dict.
# Both `in` checks work, but `x in dict` / `x in set` stays fast as the data grows, while `x in list` checks every item.

# %%
ages = {"Alice": 30, "Bob": 25}      # by name
names = ["Alice", "Bob", "Alice"]    # by position; duplicates allowed
point = (3, 4)                       # fixed pair
unique = set(names)                  # duplicates removed

ages["Bob"]              # -> 25
names[2]                 # -> 'Alice'
point[0]                 # -> 3
len(unique)              # -> 2
