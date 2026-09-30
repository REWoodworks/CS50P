


def main():
    plate = input("Plate: ")
    # we will set up a string of true/false.  Any return of FALSE from is_valid pushed the code to ELSE, "Invalid"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # must contain 2-6 chars
    if not 2 <= len(plate) <=6:     
        return False
    
    # 1st 2 positions must be letters 
    if not plate[:2].isalpha():
        return False

    # nothing but numbers and letters are allowed
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

    


if __name__ == "__main__":
    main()
