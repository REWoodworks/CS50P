# In a file called scourgify.py, implement a program that:
# Expects the user to provide two command-line arguments:
# 1) the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and 
# 2) the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. 
# Assume that each student will have both a first name and last name.
# 
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

def main():

    if len(sys.argv) != 3:
        sys.exit("Please provide filenames")

    before_csv = []
    
    try:
        with open(sys.argv[1], mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                before_csv.append(row)
    except FileNotFoundError:
        sys.exit("File cannot be read.")

   
    after_csv = []

    for row in before_csv:
        last, first = row["name"].split(", ") 
        house = row["house"]
        newrow = {"first": first, "last": last, "house": house}
        after_csv.append(newrow)
   
    with open(sys.argv[2], mode="w") as file:
        data = after_csv
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in after_csv:
            writer.writerow(line)



    #use open/with and dictwrite to write the new csv file
    
    
    




if __name__ == "__main__":
    main()