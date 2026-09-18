### Prompts a user for their name and gives their Harry Potter house based on their name.
## Starting off using if, elif, and else statements to check the name and print out the house.

name = input("What's your name? ")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

## Using the or operator to check if the name is one of the three Gryffindor students. 
## This is a more efficient way to check if the name is one of the three Gryffindor students because it uses the or operator to check if the name is equal to any of the three names. 
## If the name is equal to any of the three names, it will print "Gryffindor"; otherwise, it will print "Who?".

name = input("What's your name? ")
if name == "Harry" or name == "Hermione" or name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Match, so cool. 
# note use of _ in final case to catch all other names.

name = input("What's your name? ")
match name: 
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

## Further refinment 
## Note the match statement can use the | operator to check for multiple cases in a single line.

name = input("What's your name? ")
match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")