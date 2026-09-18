# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

grocery_list = {}

def main ():

    while True:
        try:
            new_add = input("Item to add to list:").lower()
            #tabling if/else dict search/addition
            current = grocery_list.get (new_add, 0)
            grocery_list[new_add] = current + 1
        except EOFError:
            print ()
            break

    sorted_list = dict(sorted(grocery_list.items()))

    for food, count in sorted_list.items():
        print ((count), food.upper())
        


main ()