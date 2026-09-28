# CS50P Week 4 Short: API Calls
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.

# Version 0 - api0.py
# Establishes the basic API workflow: make a GET request, convert the JSON
# response into Python data, and print the complete result.

import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    print(content)


main()


# -----------------------------------------------------------------------------
# Version 1 - api1.py
# Instead of printing the entire response, this version loops through the
# response's "data" list and prints only each artwork title.

import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()


# -----------------------------------------------------------------------------
# Version 2 - api2.py
# Adds HTTP error handling: raise_for_status detects a failed request, and the
# program catches requests.HTTPError, prints a message, and exits with status 1.

import sys
import requests


def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()


# -----------------------------------------------------------------------------
# Version 3 - api3.py
# Prompts for an artist and sends that value as the API's "q" query parameter,
# turning the general request into a user-directed search.

import sys
import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()


# -----------------------------------------------------------------------------
# Version 4 - api4.py
# Adds a "limit" query parameter so the API returns no more than three results;
# the rest of the search and error-handling logic remains unchanged.

import sys
import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "limit": 3}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
