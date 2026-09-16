#take a small collection of data and print a readable summary.

#define main function
def main ():

    #establish expense list
    expenses = [12.50, 8.00, 19.25]

    #print opening lines
    print ("Expense Report")
    print ("--------------")

    # use LEN to get the count of items in a list and assign to count var
    count = len(expenses)
    # use f string to print text with count variable
    print (f"Number of expenses: {count}")

    #use SUM to sum the list and assign to total var
    total = sum(expenses)
    # use f string to print text with total variable
    print (f"Total: ${total:.2f}")

    # use MAX to find largest value and assign to largest var
    largest = max(expenses)
    #call printmax function with largest variable
    printmax (largest)

#define printmax function
def printmax(entry):
    # use f string to print text with entry variable
    print (f"Largest expense: ${entry:.2f}")

    ##this is an unneeded function, 
    ##.2f format specifier used to get cents


main()
