# in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.


import sys

def main():

    count = 0

    if len(sys.argv) != 2:
        sys.exit("Enter one argument only")
    if not sys.argv[1].endswith(".py"):
        sys.exit("not a python file")
        
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


