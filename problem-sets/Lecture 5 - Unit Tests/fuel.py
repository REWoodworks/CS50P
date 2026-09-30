#In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

# convert expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a positive integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int.



def main():
    
    print("Input your gas tank as a fraction X/Y")
    

    while True:
        fraction = input("what is your fraction?")
        
        try:
            percentage = convert(fraction)
            break
        except(ValueError, ZeroDivisionError):
            print("Invalid fraction")


    display = gauge(percentage)
    print(f"{display}")



def convert(fraction):

    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError ("Y must not be zero")
    if x < 0 or x > y:
        raise ValueError ("X must be between 0 and y")
    fuel = (x / y) * 100
    percentage = round(fuel)
    return percentage                                 

    # Original effort code take from rework of ch 2
    # while True:
    #     try:
    #         x, y = (fraction).split("/")
    #         x = int(x)
    #         y = int(y)
    #         fuel = (x / y) * 100
    #     except ValueError:
    #         sys.exit("Numbers must be integers.")
    #     except ZeroDivisionError: 
    #         sys.exit("Y must not be zero")
    #     else:
    #         if x >= 0 and y > 0 and not x > y:
    #             break
    #         elif x < 0:
    #             sys.exit("x must be greater than or equal to zero")
    #         elif y <= 0:
    #             sys.exit("y must be greater than 0")
    #         elif x > y:
    #             sys.exit("x must not be greater than y")

    # percentage = round(fuel)
    # return percentage

def gauge(percentage):

    if percentage >= (99):
        percentage = "F"
        return percentage

    elif (1) < percentage < (99):
        percentage = (f"{percentage}%")
        return percentage

    else:
        # percentage <= (1) (marker held for self)
        percentage = "E"
        return percentage    
    
    
    
    
    

if __name__ == "__main__":
    main()
