# #CREATING A COLUMN OF BRICKS
# print("#")
# print("#")
# print("#")

# #using a loop to create a column of bricks
# for _ in range(3):
#     print("#")

# #enclosing the loop in a function
# def main():
#     print_column(3)
# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()

# # NOW WE START TO CREATE ROWS
# def main():
#     print_row(4)
# def print_row(width):
#     print("?" * width)
# main()

# #creating both rows and columns with nested for loops
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

# #and finally we can create a square of bricks using the shortest code possible

# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#         print_row(size)
# def print_row(width):
#     print("#" * width)
# main()

