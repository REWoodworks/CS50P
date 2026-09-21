<!-- generate0.py -->

Introduces Python's `random` module and uses `random.choice` to select either `"heads"` or `"tails"`. This is the first example, so there is no earlier block to compare it with.


# Demonstrates import and random.choice

import random

coin = random.choice(["heads", "tails"])
print(coin)


<!-- generate1.py -->

Imports only the `choice` function from `random`, allowing it to be called without the `random.` prefix. The result is the same as the previous block, but the import and function call are more specific.


# Demonstrates from

from random import choice

coin = choice(["heads", "tails"])
print(coin)


<!-- generate2.py -->

Returns a random integer from 1 through 10 with `random.randint`. Compared with the previous block, it returns a number from a range instead of choosing an item from a list.


# Demonstrates randint

import random

number = random.randint(1, 10)
print(number)


<!-- generate3.py -->

Uses `random.shuffle` to rearrange a list in place, then prints each card in its new order. Unlike the previous block, this changes an existing list instead of producing one random value.


# Demonstrates shuffle

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


<!-- average.py -->

Introduces the `statistics` module and calculates the arithmetic mean of two numbers. This starts a new standard-library example and replaces randomization with a deterministic calculation.


# Demonstrates statistics

import statistics

print(statistics.mean([100, 90]))


<!-- name0.py -->

Introduces `sys.argv` and reads the first command-line argument supplied after the script name. This begins a new topic: accepting input when the program is launched rather than working with values written directly in the code.


# Demonstrates sys.argv

import sys

print("hello, my name is", sys.argv[1])


<!-- name1.py -->

Wraps the command-line argument access in `try`/`except` so the program can handle a missing argument. The previous block crashes with an `IndexError`; this version catches that error and prints a helpful message.


# Demonstrates IndexError

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


<!-- name2.py -->

Checks the length of `sys.argv` before accessing an argument and reports whether there are too few or too many. Instead of reacting to an `IndexError` after it happens, this version validates the input explicitly in advance.


# Adds error checking

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


<!-- name3.py -->

Uses `sys.exit` to stop the program immediately when the argument count is invalid. This removes the final `else` from the previous block because valid execution can continue only after both error checks have been passed.


# Demonstrates sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


<!-- name4.py -->

Uses the slice `sys.argv[1:]` to loop over every supplied name while excluding the script name at index 0. Compared with the previous block, it allows multiple arguments instead of rejecting them.


# Demonstrates list slice

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


<!-- say0.py -->

Introduces the third-party `cowsay` package and displays a greeting spoken by an ASCII cow. This starts a package-installation example while retaining the earlier idea of reading one command-line argument.


# Demonstrates pip-installed package

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])


<!-- say1.py -->

Calls `cowsay.trex` to display the same greeting with a T. rex character. The only behavioral change from the previous block is the specific function selected from the `cowsay` package.


# Demonstrates a t-rex

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])


<!-- itunes0.py -->

Uses the third-party `requests` package to call the iTunes Search API and prints the parsed JSON response. This moves from a display-oriented package to retrieving live data over HTTP, while still using a command-line search term.


# Demonstrates requests

import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())


<!-- itunes1.py -->

Formats the API response with `json.dumps(..., indent=2)` so its nested structure is easier to inspect. The request is unchanged from the previous block; only the presentation of the response becomes human-readable.


# Demonstrates json

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))


<!-- itunes2.py -->

Stores the parsed JSON object, loops through its `"results"` list, and prints each result's `"trackName"`. Compared with the previous block, it removes the one-result limit and extracts useful fields instead of printing the entire JSON structure.


# Demonstrates iterating over JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])


<!-- sayings0.py -->

Defines reusable `hello` and `goodbye` functions that each accept a name. This starts the custom-module section, replacing API response processing with code intended to be imported elsewhere.


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


<!-- say2.py -->

Imports only `hello` from the new `sayings0` module and calls it with a command-line argument. The functions from the previous block are now being reused by a separate program.


# Demonstrates own module

import sys

from sayings0 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


<!-- sayings1.py -->

Adds a `main` function that calls both greeting functions, then calls `main()` at the bottom of the module. Unlike the earlier `sayings0` module, this file executes code immediately whenever it is run or imported.


# Doesn't check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


main()


<!-- say3.py -->

Imports `hello` from `sayings1` and calls it with a command-line argument. Compared with `say2.py`, the import now also triggers `sayings1.py`'s unguarded `main()` call, illustrating an unwanted import side effect.


# Demonstrates own module

import sys

from sayings1 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


<!-- sayings2.py -->

Guards the call to `main()` with `if __name__ == "__main__"`, so it runs only when this file is launched directly. This fixes the previous module's import side effect while keeping its functions available to other files.


# Check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()


<!-- say4.py -->

Imports and calls `hello` from the guarded `sayings2` module. Compared with `say3.py`, importing the module no longer runs the module's own `main()` function first.


# Demonstrates own module

import sys

from sayings2 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


<!-- say5.py -->

Imports `goodbye` instead of `hello` from the same guarded module and calls it with the command-line argument. The structure is otherwise unchanged from the previous block, demonstrating that either reusable function can be imported independently.


# Demonstrates own module

import sys

from sayings2 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

