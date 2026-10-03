# CS50P Week 3 Short: Raising Exceptions
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Versions 1-3 raise on purpose (minutes=0).


# -----------------------------------------------------------------------------
# Version 0 - pace0.py
# get_pace divides minutes by miles. It uses keyword arguments (miles=...,
# minutes=...) so the call is clear.

def main():
   pace = get_pace(miles=26.2, minutes=180)
   print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    return minutes / miles


main()


# -----------------------------------------------------------------------------
# Version 1 - pace1.py
# With minutes=0 the result is nonsense, so get_pace raises a plain Exception()
# to stop.

def main():
   pace = get_pace(miles=26.2, minutes=0)
   print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise Exception()
    return minutes / miles


main()


# -----------------------------------------------------------------------------
# Version 2 - pace2.py
# Raises the more specific ValueError, which tells the caller the value was the
# problem.

def main():
   pace = get_pace(miles=26.2, minutes=0)
   print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError()
    return minutes / miles


main()


# -----------------------------------------------------------------------------
# Version 3 - pace3.py
# Adds a message to ValueError(...) so the traceback explains what went wrong.

def main():
   pace = get_pace(miles=26.2, minutes=0)
   print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0")
    return minutes / miles


main()
