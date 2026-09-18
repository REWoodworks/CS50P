# Lecture 3 Exceptions Code
# Code examples from Lecture 3 - Exceptions.md, in their original order.
# All examples are commented out; intentional errors are preserved.
#
# 01. A missing closing quotation mark intentionally demonstrates a SyntaxError.
print("hello, world)
#
#
# 02. Converting user input with int() can raise ValueError when the input does not represent an integer.
x = int(input("What's x? "))
print(f"x is {x}")
#
#
# 03. A try/except statement catches ValueError and displays an explanation instead of stopping with an unhandled exception.
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
#
#
# 04. Printing x outside the try/except can cause NameError if conversion failed before x was assigned.
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
print(f"x is {x}")
#
#
# 05. The else clause prints x only when the try block completes without an exception.
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
#
#
# 06. A while loop repeatedly requests input until successful conversion allows break to end the loop.
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
#
#
# 07. The get_int() function repeats the input request until valid and returns the integer after leaving its loop.
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
main()
#
#
# 08. Returning x from the else clause exits the function and its loop as soon as valid input is received.
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x
main()
#
#
# 09. Returning the conversion result directly removes the need for an intermediate variable.
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
main()
#
#
# 10. The pass statement handles ValueError without displaying an error message, allowing the loop to ask again.
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass
main()
#
#
# 11. A prompt parameter makes get_int() reusable with different input questions.
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
#
#
