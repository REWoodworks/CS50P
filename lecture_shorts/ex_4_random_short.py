# CS50P Week 4 Short: random
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - cards0.py
# Creates the shared card list and a placeholder main function. The ellipsis
# marks code that has not yet been implemented.

cards = ["jack", "queen", "king"]


def main(): ...


main()


# -----------------------------------------------------------------------------
# Version 1 - cards1.py
# Imports random and uses random.choice to select and print one card.

import random

cards = ["jack", "queen", "king"]


def main():
    print(random.choice(cards))


main()


# -----------------------------------------------------------------------------
# Version 2 - cards2.py
# Replaces choice with choices and requests two results. Because choices samples
# with replacement, the same card may be selected more than once.

import random

cards = ["jack", "queen", "king"]


def main():
    print(random.choices(cards, k=2))


main()


# -----------------------------------------------------------------------------
# Version 3 - cards3.py
# Adds weights to control relative selection probabilities. These weights force
# both selections to be "jack" because the other cards have zero weight.

import random

cards = ["jack", "queen", "king"]


def main():
    print(random.choices(cards, weights=[100, 0, 0], k=2))


main()


# -----------------------------------------------------------------------------
# Version 4 - cards4.py
# Replaces choices with sample, selecting two distinct cards without replacement.

import random

cards = ["jack", "queen", "king"]


def main():
    print(random.sample(cards, k=2))


main()


# -----------------------------------------------------------------------------
# Version 5 - cards5.py
# Seeds the pseudorandom generator before sampling, making the result repeatable
# each time the program starts with the same seed.

import random

cards = ["jack", "queen", "king"]


def main():
    random.seed(0)
    print(random.sample(cards, k=2))


main()
