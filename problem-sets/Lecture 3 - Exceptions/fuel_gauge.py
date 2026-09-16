# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    print("Input your gas tank as a fraction X/Y")
    user_fraction = (input("What is your fraction?"))

    get_xy(user_fraction)

def get_xy(xyinput):

    x, y = xyinput.split("/")
    while True:

        #if x or y arent integers, prompt again
        while True:
            try:
                x = int(x)
            except ValueError:
                print (".X should be an integer")
                x = input("Please enter X: ")
            else:
                break

        while True:
            try:
                y = int(y)
            except ValueError:
                print (".Y should be an integer")
                y = input("Please enter Y: ")
            else:
                break

        #if x>y, nonsense and prompt again
        while True:
            if int(x) > int(y):
                print ("Please enter a value where x < y")
                # removing to clear duplication and overwrite
                # x, y = (input("Please enter X/Y ").split("/"))
                while True:
                    try:
                        print ("X and Y must both be integers")
                        x, y = (input("Please enter X/Y ").split("/"))
                        x = int(x)
                        y = int(y)
                    except ValueError:
                        print("X and Y must both be integers")
                        # x = int(x) removed, exception should restate then restart loop
                        # y = int(y) this setup would cause a re-try of the error causing function
                    else:
                        break
            else:
                break

                    
        #if x is less than zero, prompt again
        while True:
            if int(x) < 0:
                while True:
                    try:
                        x = int(input(".Please enter an X value greater than 0: "))
                    except ValueError:
                        print (".X should be an integer greater than 0: ")
                        x = (input(".Please enter X: "))
                    else:
                        break    
            else:
                break
        
        #if y is 0, prompt again (also less than)
        while not int(y) > 0:
            try:
                y = int(input("Y must be greater than 0:"))
            except ValueError:
                y = int(input("Y must be an integer greater than 0"))    
            if y > 0:
                break


        if x >= 0 and y > 0 and x <= y:
            convert(x, y)
            break
    
def convert(x, y):

    #fuel = x/y

    if int(x) / int (y) >= (99/100):
        output = x/y
        print ("F")
    elif (1/100) < (x/y) < (99/100):
        output = x/y
        print (f"{output:.0%}")
    else:
        #x/y <= (1/100)
        output = x/y
        print ("E")

#def guage_out():
   # ...

main()
