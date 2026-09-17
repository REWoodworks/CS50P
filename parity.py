### Introducing %, the modulo operator, which gives the remainder of a division. For example, 5 % 2 is 1 because 5 divided by 2 is 2 with a remainder of 1. We can use this to determine if a number is even or odd. If a number is divisible by 2 (i.e., the remainder is 0), it is even; otherwise, it is odd.
###
#x = int(input("What's x? "))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


### Def a function to determine if a number is even or odd. 
### This is a more efficient way to determine if a number is even or odd because it uses the modulo operator to check if the number is divisible by 2. If the number is divisible by 2, it is even; otherwise, it is odd.

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
#
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# main()


### we can colapse the if else statement in the is_even function to a single line using a ternary operator. 
### This is a more efficient way to determine if a number is even or odd because it uses the modulo operator to check if the number is divisible by 2. 
### If the number is divisible by 2, it is even; otherwise, it is odd.

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
# def is_even(n):
#     return True if n % 2 == 0 else False
# main()


## further refinement of the is_even function to a single line using the modulo operator.
## the program will evaluate what is happening within the n % 2 == 0 as either True or False and simply return that to the main function.
## Just RETURN the value of your own BOOL expression

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()
