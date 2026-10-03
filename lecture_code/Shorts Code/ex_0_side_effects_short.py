# CS50P Week 0 Short: Side Effects
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - machine0.py
# A global variable, emoticon, defined outside every function. main is a
# placeholder (...).

emoticon = "v.v"


def main():
    ...


main()


# -----------------------------------------------------------------------------
# Version 1 - machine1.py
# say prints the phrase plus the global emoticon. Printing is the function's
# side effect.

emoticon = "v.v"


def main():
    say("Is anyone there?")


def say(phrase):
    print(phrase + " " + emoticon)


main()


# -----------------------------------------------------------------------------
# Version 2 - machine2.py
# Calls say twice with different phrases.

emoticon = "v.v"


def main():
    say("Is anyone there?")
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()


# -----------------------------------------------------------------------------
# Version 3 - machine3.py
# Sets emoticon = ":D" inside main. This makes a new local variable in main, so
# say still prints the global "v.v".

emoticon = "v.v"


def main():
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()


# -----------------------------------------------------------------------------
# Version 4 - machine4.py
# Adds `global emoticon` in main, so the assignment changes the global and the
# second say prints ":D". Changing global state is a side effect too.

emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
