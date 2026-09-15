# Lecture 2 Loops Code
# All fenced examples are preserved in their original order, including sample output.
# Every line is commented out; intentional errors and intermediate examples are preserved.
#
# 01. Three repeated print() calls demonstrate the repetition that a loop can replace.
# print("meow")
# print("meow")
# print("meow")
#
#
# 02. This while loop intentionally runs forever because i never changes.
# i = 3
# while i != 0:
#     print("meow")
#
#
# 03. Decreasing i after each iteration makes the loop stop after three prints.
# i = 3
# while i != 0:
#   print("meow")
#   i = i - 1
#
#
# 04. Increasing i from one repeats the loop while i is at most three.
# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1
#
#
# 05. Starting at zero and using += advances the counter through three iterations.
# i = 0
# while i < 3:
#     print("meow")
#     i += 1
#
#
# 06. A for loop repeats once for each item in a three-item list.
# for i in [0, 1, 2]:
#     print("meow")
#
#
# 07. Using range(3) supplies three successive integers for the loop.
# for i in range(3):
#     print("meow")
#
#
# 08. An underscore names a loop variable whose value is not needed in the body.
# for _ in range(3):
#     print("meow")
#
#
# 09. Multiplying a string repeats its contents without inserting separators.
# print("meow" * 3)
#
#
# 10. Newline characters separate repeated strings while end="" prevents an extra final newline.
# print("meow\n" * 3, end="")
#
#
# 11. The continue and break statements reject negative input and stop on nonnegative input.
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
#
#
# 12. A validation loop accepts a positive number before printing that many meows.
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")
#
#
# 13. Separate functions collect a positive number and use it to control repetition.
# def main():
#     meow(get_number())
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n
# def meow(n):
#     for _ in range(n):
#         print("meow")
# main()
#
#
# 14. Zero-based indexes access individual names in a list.
# students = ["Hermione", "Harry", "Ron"]
# print(students[0])
# print(students[1])
# print(students[2])
#
#
# 15. A for loop retrieves and prints each student directly from the list.
# students = ["Hermione", "Harry", "Ron"]
# for student in students:
#     print(student)
#
#
# 16. Combining range() and len() provides indexes for displaying numbered list entries.
# students = ["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i + 1, students[i])
#
#
# 17. Parallel lists associate students and houses by matching positions.
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
#
#
# 18. A dictionary maps student names to houses and supports lookup by key.
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
#
#
# 19. This sample terminal output shows the houses retrieved from the dictionary.
# $ python hogwarts.py
# Gryffindor
# Gryffindor
# Gryffindor
# Slytherin
#
#
# 20. Iterating directly over a dictionary yields its keys.
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student)
#
#
# 21. Using each dictionary key for lookup prints both the student and associated house.
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student, students[student])
#
#
# 22. The sep parameter places a comma and space between the printed student and house.
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student, students[student], sep=", ")
#
#
# 23. This sample terminal output shows the comma-separated student and house pairs.
# $ python hogwarts.py
# Hermione, Gryffindor
# Harry, Gryffindor
# Ron, Gryffindor
# Draco, Slytherin
#
#
# 24. A list of dictionaries stores multiple attributes per student and uses None for a missing patronus.
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]
#
#
# 25. Iterating over the student dictionaries prints selected attributes from each record.
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]
# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")
#
#
# 26. Three print() calls draw a vertical column of hash characters.
# print("#")
# print("#")
# print("#")
#
#
# 27. A for loop replaces repeated print() calls when drawing a column.
# for _ in range(3):
#     print("#")
#
#
# 28. The print_column() function uses a height parameter to control the number of rows.
# def main():
#     print_column(3)
# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()
#
#
# 29. String multiplication draws a horizontal row whose width comes from a parameter.
# def main():
#     print_row(4)
# def print_row(width):
#     print("?" * width)
# main()
#
#
# 30. Nested loops draw a square by printing individual bricks and ending each completed row.
# def main():
#     print_square(3)
# def print_square(size):
#     # For each row in square
#     for i in range(size):
#         # For each brick in row
#         for j in range(size):
#             #  Print brick
#             print("#", end="")
#         # Print blank line
#         print()
# main()
#
#
# 31. A helper function prints each row while an outer loop controls the square height.
# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#         print_row(size)
# def print_row(width):
#     print("#" * width)
# main()
#
#
