# In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print




def main():

    greeting = value(input ("Greeting: ").strip().lower())

    print(f"${greeting}")


def value(greeting):

    if greeting == ("hello"):
        pay = 0
        greeting = int(pay)
        return greeting
    elif greeting.startswith("h"):
        pay = 20
        greeting = int(pay)
        return greeting
    else:
        pay = 100
        greeting = int(pay)
        return (greeting) 
        


if __name__ == "__main__":
    main ()
