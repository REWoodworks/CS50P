# CS50P Week 0 Short: Functions
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - hello0.py
# Two print calls at the top level of the file. Python runs them from top to
# bottom.

print("Hello, world!")
print("This is CS50P.")


# -----------------------------------------------------------------------------
# Version 1 - hello1.py
# Wraps the prints in a function named main. Running this prints nothing,
# because defining a function does not call it.

def main():
    print("Hello, world!")
    print("This is CS50P.")


# -----------------------------------------------------------------------------
# Version 2 - hello2.py
# Adds main() at the bottom. Calling the function is what makes its body run.

def main():
    print("Hello, world!")
    print("This is CS50P.")


main()
