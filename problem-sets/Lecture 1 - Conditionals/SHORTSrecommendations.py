# This is a SHORTS program from Lecture1 that demonstrates methosds of using boolean logic to make recommendations based on user input. 
# IF, AND, ELIF, ELSE.
# Note the use of NOT as a way to convert booleans to their opposites. 
# Note the use of RETURN to end the program if the user input is invalid.  This is a good way to avoid nested IF statements.

def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
       print("Enter a valid number of players")
       return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game):
    print("You might like", game)


main()