# CS50P Week 2 Short: String Methods
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - shows0.py
# .capitalize() uppercases only the first character and lowercases the rest.

SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    for show in SHOWS:
        print(show.capitalize())


main()


# -----------------------------------------------------------------------------
# Version 1 - shows1.py
# .title() uppercases the first letter of every word.

SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    for show in SHOWS:
        print(show.title())


main()


# -----------------------------------------------------------------------------
# Version 2 - shows2.py
# .strip() removes leading and trailing whitespace (see "the Proud family ").

SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    for show in SHOWS:
        print(show.strip())


main()


# -----------------------------------------------------------------------------
# Version 3 - shows3.py
# Chains methods: .strip().title() runs left to right, each on the previous
# result.

SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    for show in SHOWS:
        print(show.strip().title())


main()


# -----------------------------------------------------------------------------
# Version 4 - shows4.py
# Collects the cleaned titles in a list, then joins them into one string with
# ', '.join(...).

SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print(', '.join(cleaned_shows))


main()
