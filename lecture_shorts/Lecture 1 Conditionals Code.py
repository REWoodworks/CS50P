# Lecture 1 Conditionals Code
# All fenced examples are preserved in their original order, including sample output.
# Every line is commented out; intentional errors and intermediate examples are preserved.
#
# 01. An if statement prints a message only when x is less than y.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
#
#
# 02. Three independent if statements each test a comparison between x and y.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")
#
#
# 03. An if/elif chain stops checking later branches once a condition is true.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")
#
#
# 04. An else clause handles equality after the less-than and greater-than checks fail.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")
#
#
# 05. The or operator combines two comparisons to detect unequal values.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
#
#
# 06. The != operator directly tests whether two values are unequal.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
#
#
# 07. The == operator tests equality and else handles unequal values.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")
#
#
# 08. The and operator requires both bounds of each grade interval to be satisfied.
# score = int(input("Score: "))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >=80 and score < 90:
#     print("Grade: B")
# elif score >=70 and score < 80:
#     print("Grade: C")
# elif score >=60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
#
# 09. Chained comparisons express each grade interval without an explicit and operator.
# score = int(input("Score: "))
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
#
# 10. Checking grade thresholds in descending order removes redundant upper-bound comparisons.
# score = int(input("Score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
#
# 11. The modulo operator identifies even integers by checking for a remainder of zero.
# x = int(input("What's x? "))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
#
# 12. The is_even() function returns a Boolean for main() to use as a condition.
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# main()
#
#
# 13. A conditional expression selects the Boolean returned by is_even() on one line.
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# def is_even(n):
#     return True if n % 2 == 0 else False
# main()
#
#
# 14. Returning the comparison directly produces the Boolean result without extra branching.
# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# def is_even(n):
#     return n % 2 == 0
# main()
#
#
# 15. An if/elif chain selects a house based on the entered name.
# name = input("What's your name? ")
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron": 
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
#
#
# 16. The or operator groups names that share the same house.
# name = input("What's your name? ")
# if name == "Harry" or name == "Hermione" or name == "Ron": 
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
#
#
# 17. A match statement selects a matching name case and uses a wildcard for other names.
# name = input("What's your name? ")
# match name: 
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron": 
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
#
#
# 18. The vertical bar combines alternative name patterns within one case.
# name = input("What's your name? ")
# match name: 
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
#
#
