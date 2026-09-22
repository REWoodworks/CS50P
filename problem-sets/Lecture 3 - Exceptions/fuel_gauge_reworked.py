# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():
    print("Input your gas tank as a fraction X/Y")

    while True:
        try:
            x, y = (input("What is your fraction?")).split("/")
            x = int(x)
            y = int(y)
            fuel = x / y
        except (
            ValueError
        ):  # handles ALL non integer entries ie call words and malformed fraction entry
            print("Numbers must be integers.")
        except ZeroDivisionError:  # handles zero division
            print("Y must not be zero")
        else:
            if x >= 0 and y > 0 and not x > y:  # confirms all remaining conditions!!!
                break
            elif x < 0:
                print("x must be greater than or equal to zero")
            elif y <= 0:
                print("y must be greater than 0")
            elif x > y:
                print("x must not be greater than y")

    if fuel >= (99 / 100):
        print("F")

    elif (1 / 100) < fuel < (99 / 100):
        print(f"{fuel:.0%}")

    else:
        fuel <= (1 / 100)
        print("E")


main()
