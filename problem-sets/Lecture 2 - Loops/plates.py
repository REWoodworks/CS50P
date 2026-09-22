# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
#
# 1) “All vanity plates must start with at least two letters.”
# -2) “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# 3) “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# -4) “No periods, spaces, or punctuation marks are allowed.”
#
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


# we define what we want to keep, use not to find anything else, then return false to say invalid
# we want to be able to return falses to keep from further nesting
# simply tracing code progress and noting triggers as well as comprehending syntax is tough


def main():
    plate = input("Plate: ")
    # we will set up a string of true/false.  Any return of FALSE from is_valid pushed the code to ELSE, "Invalid"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # 1st conditional check; must contain 2-6 chars
    if not 2 <= len(plate) <=6:     
        return False
    
    # 2nd condition, 1st 2 positions must be letters 
    # we use a SLICE with an .isalpha confirmation, again returning false
    if not plate[:2].isalpha():
        return False

    # 3rd condition, nothing but numbers and letters are allowed
    # next we use .ISALNUM() to see if there is anything other than alphanumebrics
    if not plate.isalnum():
        return False

    # Finally, find the first digit and rule out letters after that 
    for position in range(len(plate)):
        character = plate[position]

        if character.isdigit():
            # The first digit cannot be zero.
            if int(character) == 0:
                return False

            # From the first digit onward, everything must be digits.
            return plate[position:].isdigit()
            # if plate[position:].isdigit():
            #    return True
            # else:
            #    return False

    # No digits were found, and all earlier checks passed.
    return True

    



main()
