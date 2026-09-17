menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

def main ():

    cost = 0
        
    while True:
        #food = input("Item:").title() - could not place here because ^D would cause EOFError
        try:
            food = input("Item:").title()
            purchase = (menu[food])
            cost = cost + float(purchase)
            #print (f"Total: ${cost:.02f}")   
            continue
        except KeyError:
            pass
        except EOFError:
            print(f"\nTotal: ${cost:.02f}")
            break #could not use return here because it left the entire main function?!

    print("Thank you come again!")

main()

print("Main doesn't set the sun")
