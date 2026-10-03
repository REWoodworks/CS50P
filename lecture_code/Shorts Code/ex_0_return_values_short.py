# CS50P Week 0 Short: Return Values
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - area0.py
# area prints the result. Printing is a side effect: main sees the text appear
# but gets no value back.

def area(length, width):
    print(str(length * width) + " square feet")


def main():
    area(50, 20)


main()


# -----------------------------------------------------------------------------
# Version 1 - area1.py
# Calls area twice. Each call prints, but main still can't add the two areas
# together.

def area(length, width):
    print(str(length * width) + " square feet")


def main():
    area(50, 20)
    area(50, 50)


main()


# -----------------------------------------------------------------------------
# Version 2 - area2.py
# area now uses return, so main can store each result in a variable (house,
# yard).

def area(length, width):
    return length * width


def main():
    house = area(50, 20)
    yard = area(50, 50)


main()


# -----------------------------------------------------------------------------
# Version 3 - area3.py
# Adds house and yard into total and prints once. Returned values can be
# reused; printed ones cannot.

def area(length, width):
    return length * width


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")


main()
