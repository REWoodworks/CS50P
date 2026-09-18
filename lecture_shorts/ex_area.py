#def area(length, width):
#    print(str(length * width) + " square feet")

#print here is a side effect of the area function, doesnt return the area as a value

#def main():
#    area(50, 20)
#    area(50, 50)

#main()

def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print("Total area: " + str(total) + " square feet")



def area(length, width):
    print(str(length * width) + " square feet")
    # we must use str here to convert the numeric value to a string for printing otherwise fails
    # str will converty L*W to a string to use with square feet for use by the print function   
    return length * width
    print(str(length * width) + " square feet")
    #return ends the function immediately, so any code after it will not be executed (line 17 will not work, hence the underlined print 



main()