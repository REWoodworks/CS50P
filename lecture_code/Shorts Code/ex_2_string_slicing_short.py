# CS50P Week 2 Short: String Slicing
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.


# -----------------------------------------------------------------------------
# Version 0 - phone0.py
# phone[0:3] takes indexes 0, 1 and 2 (the area code). The stop index is
# excluded.

def main():
    phone = "6174951000"
    print(phone[0:3])


main()


# -----------------------------------------------------------------------------
# Version 1 - phone1.py
# Leaving out the start, phone[:3], means start at the beginning.

def main():
    phone = "6174951000"
    print(phone[:3])


main()


# -----------------------------------------------------------------------------
# Version 2 - phone2.py
# phone[6:10] takes the last four digits.

def main():
    phone = "6174951000"
    print(phone[6:10])


main()


# -----------------------------------------------------------------------------
# Version 3 - phone3.py
# Leaving out the stop, phone[6:], means go to the end.

def main():
    phone = "6174951000"
    print(phone[6:])


main()


# -----------------------------------------------------------------------------
# Version 4 - phone4.py
# Negative indexes count from the end: phone[-4:] is the last four characters.

def main():
    phone = "6174951000"
    print(phone[-4:])


main()


# -----------------------------------------------------------------------------
# Version 5 - phone5.py
# A third number is the step: phone[0:10:1] moves one character at a time.

def main():
    phone = "6174951000"
    print(phone[0:10:1])


main()


# -----------------------------------------------------------------------------
# Version 6 - phone6.py
# A step of -1 walks backward, so phone[::-1] reverses the string.

def main():
    phone = "6174951000"
    print(phone[::-1])


main()
