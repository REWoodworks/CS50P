#Totaler: Add a list of numbers and print the total—for example, expenses of 12.50, 8, and 19.25 should produce 39.75
# write a script that adds those three expenses and prints the answer.

def main():

    addend1 = float(input("Item 1: "))
    addend2 = float(input("Item 2: "))
    addend3 = float(input("Item 3: "))

    total = addend1 + addend2 + addend3

    print (f"{addend1} + {addend2} + {addend3} = {total}")
    print (addend1+addend2+addend3)

main()