#### A Series of refinements to the code that compares two numbers and prints out whether they are equal or not.
#### Uses if, elif, else, or, and != operators to demonstrate different ways to compare two numbers and print out the result.

### this causes the computer to ask all three questions no matter what the answer is to the first question
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")


### creates mutual exclusivity between the three conditions. If one condition is true, the others will not be checked. This is more efficient and avoids unnecessary comparisons.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")

### we dont need to check if x == y because if the first two conditions are false, it must be true that x == y. This is more efficient and avoids unnecessary comparisons.
### else will catch all other cases that are not covered by the previous conditions. In this case, it will catch the case where x == y.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

### or operator can be used to combine multiple conditions into a single condition.  If either of 1st conditions are true, then x is not equal to y.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

### != operator can be used to check if two values are not equal. This is more efficient and avoids unnecessary comparisons.
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

### also stated as
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x == y:
#     print("x is equal to y")
# else:
#     print("x is equal to y")

