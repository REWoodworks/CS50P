# CS50P Week 2 Short: Dictionaries
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - distances0.py
# A dict maps spacecraft names (keys) to distances (values). Loops over .keys()
# and looks up each value with distances[name].

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")


main()


# -----------------------------------------------------------------------------
# Version 1 - distances1.py
# Loops over .values() and converts each distance from AU to meters.

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()


# -----------------------------------------------------------------------------
# Version 2 - report0.py
# create_report builds a multi-line f-string from a spacecraft dict. main is a
# placeholder (...).

def main(): ...


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 3 - report1.py
# Passes a dict with both name and distance, so the report fills in.

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 4 - report2.py
# The dict has no "distance" key, so spacecraft["distance"] raises a KeyError.

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 5 - report3.py
# Uses .get(), which returns None instead of crashing when a key is missing.

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name")}
    Distance: {spacecraft.get("distance")} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 6 - report4.py
# Gives .get() a default ("Unknown") to show when a key is missing.

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 7 - report5.py
# Adds a key after creation with spacecraft["distance"] = 0.01.

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU

    ==========================
    """


main()


# -----------------------------------------------------------------------------
# Version 8 - report6.py
# Adds several keys at once with .update({...}) and adds an Orbit line to the
# report.

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()
