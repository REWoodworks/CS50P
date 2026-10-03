# CS50P Week 1 Short: Boolean Expressions
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - recommendations0.py
# Starting point: the nested if/elif/else from the Conditionals short, with
# validation buried in the branches.

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


# -----------------------------------------------------------------------------
# Version 1 - recommendations1.py
# Validates each answer right after input, using not (... or ...), and leaves
# main early with return.

def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
       print("Enter a valid number of players")
       return

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")


def recommend(game):
    print("You might like", game)


main()


# -----------------------------------------------------------------------------
# Version 2 - recommendations2.py
# Because input is already validated, the inner elif checks become plain else.

def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
       print("Enter a valid number of players")
       return

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
# Version 3 - recommendations3.py
# Flattens the nesting by combining conditions with and, so there is one
# if/elif chain.

def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
       print("Enter a valid number of players")
       return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game):
    print("You might like", game)


main()
