# CS50P Week 3 Short: Handling Exceptions
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - exceptions0.py
# The distances are strings, and two include " AU". main is a placeholder
# (...).

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main(): ...


def convert(au):
    return au * 149597870700


main()


# -----------------------------------------------------------------------------
# Version 1 - exceptions1.py
# Passes the string "163" to convert. Multiplying a string repeats it, so this
# tries to build a gigantic string and fails with a MemoryError.

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    m = convert(distances[spacecraft])
    print(f"{m} m")


def convert(au):
    return au * 149597870700


main()


# -----------------------------------------------------------------------------
# Version 2 - exceptions2.py
# Converts with float() first. "80 AU" now raises a ValueError, and an unknown
# name raises a KeyError.

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    au = float(distances[spacecraft])
    m = convert(au)
    print(f"{m} m")


def convert(au):
    return au * 149597870700


main()


# -----------------------------------------------------------------------------
# Version 3 - exceptions3.py
# Wraps only the risky line in try and catches ValueError with a clear message
# and return.

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return

    m = convert(au)
    print(f"{m} m")


def convert(au):
    return au * 149597870700


main()


# -----------------------------------------------------------------------------
# Version 4 - exceptions4.py
# Adds a second except for KeyError, so each kind of error gets its own
# message.

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return

    m = convert(au)
    print(f"{m} m")


def convert(au):
    return au * 149597870700


main()
