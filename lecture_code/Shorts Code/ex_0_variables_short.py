# CS50P Week 0 Short: Variables
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - clock0.py
# Creates two variables, alarm and timezone. Assignment (=) gives a value a
# name.

def main():
    alarm = "7:00 AM"
    timezone = "US/Eastern"


main()


# -----------------------------------------------------------------------------
# Version 1 - clock1.py
# Joins the variables into one string with + and prints it.

def main():
    alarm = "7:00 AM"
    timezone = "US/Eastern"

    print(alarm + " in " + timezone)


main()


# -----------------------------------------------------------------------------
# Version 2 - clock2.py
# Reassigns both variables. The name stays the same; the value it points to
# changes.

def main():
    alarm = "7:00 AM"
    timezone = "US/Eastern"

    alarm = "4:45 PM"
    timezone = "Asia/Kathmandu"

    print(alarm + " in " + timezone)


main()


# -----------------------------------------------------------------------------
# Version 3 - clock3.py
# Stores alarm as an int (seconds since 1970). str() is needed before joining
# it with text.

def main():
    alarm = 1741604400
    timezone = "US/Eastern"

    print(str(alarm) + " in " + timezone)


main()


# -----------------------------------------------------------------------------
# Version 4 - clock4.py
# Snoozes five minutes with alarm = alarm + 300. The right side is computed
# first, then stored back.

def main():
    alarm = 1741604400
    timezone = "US/Eastern"

    alarm = alarm + 300

    print(str(alarm) + " in " + timezone)


main()


# -----------------------------------------------------------------------------
# Version 5 - clock5.py
# Same update written with the shorthand +=.

def main():
    alarm = 1741604400
    timezone = "US/Eastern"

    alarm += 300

    print(str(alarm) + " in " + timezone)


main()
