# CS50P Week 4 Short: Creating Modules and Packages
# This Short uses several companion files rather than progressive versions of
# one program. They are collected below in package order for review.
# This combined review file is not intended to run as one standalone program.


# -----------------------------------------------------------------------------
# File: museum/__init__.py
# This file is intentionally empty. Its presence identifies museum as a package.


# -----------------------------------------------------------------------------
# File: museum/artists.py
# Adds get_artists, which calls the museum's agent-search endpoint and returns a
# list of artist names. A failed HTTP request produces an empty list.

import requests


def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artists["title"] for artists in content["data"]]


# -----------------------------------------------------------------------------
# File: museum/artwork.py
# Adds the parallel get_artwork function. It searches the artworks endpoint and
# returns artwork titles while using the same error-handling pattern.

import requests


def get_artwork(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]


# -----------------------------------------------------------------------------
# File: search.py
# Imports functions from the museum package, prompts for an artist, and prints
# three returned results. The original source imports get_artwork but does not use it.

from museum.artwork import get_artwork
from museum.artists import get_artists


def main():
    artist = input("Artist: ")
    artworks = get_artists(query=artist, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")


main()
