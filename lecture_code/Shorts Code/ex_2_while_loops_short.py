# CS50P Week 2 Short: While Loops
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# soil.py is a helper module that water0-2 import from; save it beside them to
# run them.


# -----------------------------------------------------------------------------
# Helper - soil.py
# Simulates a soil sensor. Each call to sample() lowers a global moisture value
# by a random 1-5 and returns it.

import random

moisture = random.randint(25, 40)


def sample():
    global moisture
    moisture = moisture - random.randint(1, 5)
    return moisture


# -----------------------------------------------------------------------------
# Version 0 - water0.py
# Takes one moisture reading.

from soil import sample


def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")


main()


# -----------------------------------------------------------------------------
# Version 1 - water1.py
# Keeps sampling while moisture > 20, then says it's time to water. The
# condition is checked before each pass.

from soil import sample


def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        print(f"Moisture is {moisture}%")

    print("Time to water!")


main()


# -----------------------------------------------------------------------------
# Version 2 - water2.py
# Adds a days counter, incremented with += 1 inside the loop, to show how many
# days passed.

from soil import sample


def main():
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisture is {moisture}%.")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}%.")

    print("Time to water!")


main()
