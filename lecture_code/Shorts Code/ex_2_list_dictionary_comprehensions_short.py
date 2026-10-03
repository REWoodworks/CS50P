# CS50P Week 2 Short: List and Dictionary Comprehensions
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Needs address.txt (JFK's inaugural address) beside it; writes counts.csv.


# -----------------------------------------------------------------------------
# Helper - helpers.py
# Provided by the short. get_words reads a file and returns a list of words;
# save_counts writes a dict of counts to counts.csv, most frequent first. It
# uses re (regular expressions) and csv, which come later in the course.

import csv
import re


def get_words(filename):
    with open(filename, "r") as f:
        contents = f.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


# -----------------------------------------------------------------------------
# Version 0 - comprehensions0.py
# Counts words with a for loop and an if/else on a dict.

from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()


# -----------------------------------------------------------------------------
# Version 1 - comprehensions1.py
# A list comprehension, [word.lower() for word in words], builds a new
# lowercased list in one line.

from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    words = [word.lower() for word in words]

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()


# -----------------------------------------------------------------------------
# Version 2 - comprehensions2.py
# Adds a filter, if len(word) > 4, to keep only longer words.

from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    words = [word.lower() for word in words if len(word) > 4]

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()


# -----------------------------------------------------------------------------
# Version 3 - comprehensions3.py
# A dict comprehension, {word: words.count(word) for word in words}, replaces
# the whole counting loop.

from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    words = [word.lower() for word in words if len(word) > 4]
    
    counts = {word: words.count(word) for word in words}

    save_counts(counts)


main()
