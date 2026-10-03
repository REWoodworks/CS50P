# in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

#  1)check arguments entered at CL
#     a) 1 argument only
#     b) is file there
#     b) ends in .py

# 1a) establish a var = 0
# 2) open File
# 3) assign lines to a var
# 3a) for line in lines....
# 3b) strip lines
# 3c) read lines
# 4) refuse to count anything with # or blank
# 5) count all else
# 6) print count var

import sys

def main():

    count = 0

    if len(sys.argv) == 2:
        file = sys.argv[1]
        
        if not file.endswith(".py"):
            sys.exit("not a python file")
        
    else:
         sys.exit("Enter one argument only")
        
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                 line = line.strip()
                 if not line.startswith("#") and line != "":
                      count += 1
    except FileNotFoundError:
            sys.exit("File does not exist")

    print(count)


if __name__ == "__main__":
    main()


