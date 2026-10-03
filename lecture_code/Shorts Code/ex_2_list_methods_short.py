# CS50P Week 2 Short: List Methods
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Each version loops forever (while True). Press Ctrl-C to stop it.


# -----------------------------------------------------------------------------
# Version 0 - sokoban0.py
# Records every action in a history list with append.

def main():
    history = []

    while True:
        action = input("Action: ")
        history.append(action)
        print(history)


main()


# -----------------------------------------------------------------------------
# Version 1 - sokoban1.py
# "Undo" calls pop(), which removes and returns the last item, like taking the
# top plate off a stack.

def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: '{undone}'")
        else:
            history.append(action)

        print(history)


main()


# -----------------------------------------------------------------------------
# Version 2 - sokoban2.py
# "Restart" calls clear() to empty the list.

def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: '{undone}'")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)

        print(history)


main()
