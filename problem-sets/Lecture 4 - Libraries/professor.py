# In a file called professor.py, implement a program that:

# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    

    level = get_level()

    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

      
        i = 0
        while i < 3:
            #try should handle the only risk and let the if conditionals take care of the rest.  moving answer aq. into try and if out
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                i += 1    
                continue
            if answer != x + y:
                print("EEE")
                i += 1
            else:
                score = score + 1
                break
        # overcomplicated check loop....didn't think of simple ending. what happens after while loop, and while only completed at 3. Add the print on line below BUT IN A CONDITIONAL
        if i == 3:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score} / 10")


def get_level():

    while True:
        try:
            prompt = int(input("Level 1-3: "))
        except ValueError:
            print("Please enter a number 1-3")
            continue
            # had to add a continue to cycle the loop
        if not 1 <= prompt <= 3:
            print("Please enter a number 1-3")
        else:
            break
    return prompt
    # initially returned "get_level", should return "prompt"


def generate_integer(level):
    # completely restructured section due to requirements, wildly overthought the function.  main can take a random and assign to x, then to y. hence the direction, r"eturn a single"

    if level == 1:
        rando_int = random.randint(0, 9)
    elif level == 2:
        rando_int = random.randint(10, 99)
    elif level == 3:
        rando_int = random.randint(100, 999)
    else: 
        raise ValueError
         # raising an error, no idea why.  Its per spec

    return rando_int    


if __name__ == "__main__":
    main()