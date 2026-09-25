# Guessing Game

# I’m thinking of a number between 1 and 100…

# What is it?
# In a file called game.py, implement a program that:

# Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.


import random

def main():

    while True:
        try:
            n = int(input("Level: "))
            if n <1:
                continue
            else:
                break
        except ValueError:
            print("Input should be integer.")

    k = random.randint(1,n)

    while True:
        guess = int(input("Guess: "))

        if guess <= 0:
            print ("Guess again with positive integer.")
        elif guess < k:
            print("Too small!")
        elif guess > k:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()