# CS50P Week 2 Short: Dictionary Methods
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Versions 0-2 loop until every word is guessed.


# -----------------------------------------------------------------------------
# Version 0 - bee0.py
# Spelling Bee: WORDS maps each answer to its points. The loop runs while the
# dict still has entries (len(WORDS) > 0).

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary

    print("That's the game!")


main()


# -----------------------------------------------------------------------------
# Version 1 - bee1.py
# A correct guess is removed with .pop(guess), which also returns its points.

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")


main()


# -----------------------------------------------------------------------------
# Version 2 - bee2.py
# Guessing the bonus word "GRAPHIC" empties the whole dict with .clear(), which
# ends the loop.

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")


main()


# -----------------------------------------------------------------------------
# Version 3 - bee3.py
# Shows yesterday's answers by looping over .items(), which gives each key and
# value together.

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Here are yesterday's answers:")

    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


main()
