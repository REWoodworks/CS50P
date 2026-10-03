# CS50P Week 1 Short: Conditionals
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - recommendations0.py
# A recommend helper that prints a game suggestion. main is a placeholder
# (...).

def main(): ...


def recommend(game):
    print("You might like", game)


main()


# -----------------------------------------------------------------------------
# Version 1 - recommendations1.py
# Asks two questions and uses nested if/else to pick one of four games. Any
# answer other than "Difficult" falls into the else branch.

def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    else:
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")


def recommend(game):
    print("You might like", game)


main()


# -----------------------------------------------------------------------------
# Version 2 - recommendations2.py
# Uses elif to check each valid answer explicitly and adds else branches that
# report invalid input.

def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("You might like", game)


main()
