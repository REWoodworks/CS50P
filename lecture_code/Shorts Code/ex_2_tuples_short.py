# CS50P Week 2 Short: Tuples
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Version 3 raises a TypeError on purpose.


# -----------------------------------------------------------------------------
# Version 0 - location0.py
# A tuple uses parentheses to group values that belong together, here a
# latitude and longitude.

def main():
    coordinates = (42.376, -71.115)


main()


# -----------------------------------------------------------------------------
# Version 1 - location1.py
# Reads tuple items by index, like a list.

def main():
    coordinates = (42.376, -71.115)
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")


main()


# -----------------------------------------------------------------------------
# Version 2 - location2.py
# Unpacks the tuple into two variables in one line: lat, long = coordinates.

def main():
    coordinates = (42.376, -71.115)
    lat, long = coordinates
    print(f"Latitude: {lat}")
    print(f"Longitude: {long}")


main()


# -----------------------------------------------------------------------------
# Version 3 - location3.py
# Trying to change an item raises a TypeError, because tuples are immutable
# (can't be changed).

def main():
    coordinates = (42.376, -71.115)
    coordinates[0] = -42.376


main()


# -----------------------------------------------------------------------------
# Version 4 - location4.py
# sys.getsizeof shows the tuple uses less memory than an equivalent list.

import sys


def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")


main()
