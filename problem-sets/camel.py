# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

### The first 4 solutions involve a FOR loop while the fifth uses a WHILE lloop.  The FOR loop appears to be a better choice here because we are doing something with each letter as opposed to waiting for something to change or happen.  
### The WHILE loop is more appropriate when we are waiting for something to change or happen, such as a user inputting a specific value or a variable reaching a certain value.

### FIRST SOLUTION, prints each letter as it is passed through the loop, but does not store the final result in a variable to print at the end.
# def main():
#     camel_case = input("What is the variable name in camelCase?")
#
#     for letter in camel_case:
#         if letter.islower():
#             print (letter, end="")
#         elif letter.isupper():
#             letter = ("_" + letter.lower())
#             print (letter, end="")
#     print()
#
#
#main()

#### SECOND SOLUTION, stores each loop pass into a variable a variable and prints it at the end.
# def main():
#     camel_case = input("What is the variable name in camelCase?")
#
#     snake_case = ("")
#
#     for letter in camel_case:
#
#         if letter.islower():
#             snake_case = snake_case + letter
#         elif letter.isupper():
#             letter = ("_" + letter.lower())
#             snake_case = snake_case + letter
#
#     print(snake_case)
#
# main ()
    

### THIRD SOLUTION using f strings and making the assignment/creation of letter in the elif section unneded
# def main():
#     camel_case = input("What is the variable name in camelCase?")
#
#     snake_case = ("")
#
#     for letter in camel_case:
#
#         if letter.islower():
#             snake_case = f"{snake_case}{letter}"
#         elif letter.isupper():
#             snake_case = f"{snake_case}_{letter.lower()}"
#
#     print(snake_case)
#
# main ()


### FOURTH SOLUTION using cacatination of the variable assignment, making the assignment/creation of "letter" in the elif section unneded
# def main():
#     camel_case = input("What is the variable name in camelCase?")
#
#     snake_case = ("")
#
#     for letter in camel_case:
#
#         if letter.islower():
#             snake_case = snake_case + letter
#         elif letter.isupper():
#             snake_case = snake_case + "_" + letter.lower()
#         
#     print(snake_case)
#
# main ()


### FIFTH SOLUTION using WHILE loop instead of FOR loop, and using the index to access each letter in the string
def main():
    camel_case = input("What is the variable name in camelCase?")

    position = 0
    snake_case = ""

    while (position) < len(camel_case):

        letter = camel_case[position]

        if letter.islower():
            snake_case = f"{snake_case}{letter}"
        elif letter.isupper():
            snake_case = f"{snake_case}_{letter.lower()}"

        position = position + 1

    print (snake_case)

main()
