# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main ():
    print("\nWelcome to the Coke-O-Matic!")
    print("Cokes cost $0.50")
    print("This machine accepts the following coins: 25, 10, and 5\n")

    payment_made = 0
    cost = 50

    while payment_made < cost:
        print(f"\nAmount due: {cost - payment_made} cents")
        coin_spent = int(input("\nPlease insert coin:"))

        if coin_spent not in [25, 10, 5]:
            print("\nPayment must be in the form of 25, 10, or 5c coins")
            continue

        payment_made = payment_made + coin_spent


    change_owed = payment_made - cost
    print ("\nHere is your coke!")
    print (f"Your change due is {change_owed} cents\n")


main()

## Corrections involved removing an if conditional at the end, removing a zero assigned variable from the main body that was unneeded, and also the addition of an if conditional for coins spent if they ARE NOT 25,10,5...remembering to add continue.  I'll need to get some clarity on that conditional and the use of continue later on.