# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

list = {}

def main ():

    while True:
        try:
            new_add = input("Item to add to list:")
            #add to dict
        except NameError:
            #maybe
        except EOFError:
            break












main ()