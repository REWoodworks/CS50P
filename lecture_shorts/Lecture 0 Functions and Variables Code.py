# Lecture 0 Functions and Variables Code
# All fenced examples are preserved in their original order, including sample output.
# Every line is commented out; intentional errors and intermediate examples are preserved.
#
# 01. Calling input() asks for a name, but this version still prints a fixed greeting.
input("What's your name? ")
print("hello, world")
#
#
# 02. Assigning input() to name saves the response for later use.
name = input("What's your name? ")
print("hello, world")
#
#
# 03. Placing name inside quotation marks prints the literal word instead of the variable value.
name = input("What's your name? ")
print("hello, name")
#
#
# 04. Separate print() calls display the greeting and stored name on separate lines.
# name = input("What's your name? ")
print("hello,")
print(name)
#
#
# 05. This sample terminal output shows the greeting and name appearing on separate lines.
# What's your name? David
# hello,
# David
#
#
# 06. Comments explain the purpose of the input and greeting code.
# # Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
#
#
# 07. Pseudocode comments outline the steps the program performs.
# # Ask the user for their name
name = input("What's your name? ")
# # Print hello
print("hello,")
# # Print the name inputted
print(name)
#
#
# 08. The + operator concatenates the greeting and name into one string.
# # Ask the user for their name
name = input("What's your name? ")
# # Print hello and the inputted name
print("hello, " + name)
#
#
# 09. Passing two arguments to print() displays them with its default space separator.
# # Ask the user for their name
# name = input("What's your name? ")
# # Print hello and the inputted name
# print("hello,", name)
#
#
# 10. Two print() calls demonstrate the default newline after each call.
# # Ask the user for their name
# name = input("What's your name? ")
# print("hello,")
# print(name)
#
#
# 11. Setting end="" prevents the first print() call from adding a newline.
# # Ask the user for their name
# name = input("What's your name? ")
# print("hello,", end="")
# print(name)
#
#
# 12. An f-string inserts the stored name into the greeting.
# # Ask the user for their name
# name = input("What's your name? ")
# print(f"hello, {name}")
#
#
# 13. The strip() method removes whitespace from the beginning and end of the name.
# # Ask the user for their name
# name = input("What's your name? ")
# # Remove whitespace from the str
name = name.strip()
# # Print the output
print(f"hello, {name}")
#
#
# 14. The title() method applies title casing after surrounding whitespace is removed.
# # Ask the user for their name
name = input("What's your name? ")
# # Remove whitespace from the str
name = name.strip()
# Capitalize the first letter of each word
name = name.title()
# Print the output
print(f"hello, {name}")


15. Chaining strip() and title() performs both transformations in one assignment.
# Ask the user for their name
name = input("What's your name? ")
# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()
# Print the output
print(f"hello, {name}")


16. Applying string methods directly to the input result combines input and cleanup.
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()
# Print the output
print(f"hello, {name}")


17. The + operator adds two integers and stores their sum.
x = 1
y = 2
z = x + y
print(z)
#
#
# 18. Adding two input strings concatenates their text instead of performing numeric addition.
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)
#
#
# 19. Converting both input strings with int() enables integer addition.
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)
#
#
# 20. Nesting input() inside int() converts each response before assigning it.
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)
#
#
# 21. Converting input with float() allows addition of numbers containing decimal points.
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)
#
#
# 22. Calling round() without a digit count rounds the sum to an integer.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Create a rounded result
z = round(x + y)
# Print the result
print(z)
#
#
# 23. The comma format specifier displays the rounded number with thousands separators.
# # Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Create a rounded result
z = round(x + y)
# Print the formatted result
print(f"{z:,}")
#
#
# 24. Dividing two floats produces a quotient that print() displays.
# # Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the result
z = x / y
# Print the result
print(z)
#
#
# 25. Passing 2 to round() rounds the quotient to two decimal places.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the result and round
z = round(x / y, 2)
# Print the result
print(z)
#
#
# 26. The .2f format specifier displays the quotient with exactly two decimal places.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the result
z = x / y
# Print the result
print(f"{z:.2f}")
#
#
# 27. This greeting example provides the starting point for introducing custom functions.
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()
# Print the output
print(f"hello, {name}")
#
#
# 28. Calling hello() before defining it intentionally demonstrates an undefined function error.
name = input("What's your name? ")
hello()
print(name)
#
#
# 29. Defining hello() creates a reusable function that prints a greeting.
def hello():
    print("hello")
name = input("What's your name? ")
hello()
print(name)
#
#
# 30. The to parameter lets hello() greet the name supplied by its caller.
# Create our own function
def hello(to):
    print("hello,", to)
# Output using our own function
name = input("What's your name? ")
hello(name)
#
#
# 31. A default parameter lets hello() greet world when no argument is supplied.
# Create our own function
def hello(to="world"):
    print("hello,", to)
# Output using our own function
name = input("What's your name? ")
hello(name)
# Output without passing the expected arguments
hello()
#
#
# 32. Defining main() organizes the program but does not execute its body without a call.
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)
#
#
# 33. Calling main() starts the program after the functions have been defined.
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)
main()
#
#
# 34. The square() function returns a calculated value for main() to display.
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()
#
#
