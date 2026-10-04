# In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

# ORIGINALLY iterated over a list of dicts built by DictReader.  Tabulate was able to handle the iteration itself so was able to move it inside a print command.!!  The issue is TRY now covers more than just the risky call, which is the rule of thumb.

import sys
import csv
from tabulate import tabulate


def main():
    
    if len(sys.argv) != 2:
        sys.exit("One argument please")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv menu")

    # menu = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))    
            # for row in reader:
            #     menu.append(row)
        
    except FileNotFoundError:
        sys.exit("File not found")

    # print(tabulate(reader = csv.DictReader(file), headers="keys", 
    # tablefmt="grid"))

if __name__=="__main__":
    main()
