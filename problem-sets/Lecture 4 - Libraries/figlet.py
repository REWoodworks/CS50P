# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

import sys
from pyfiglet import Figlet
import random

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit()

figlet = Figlet()
figlist = figlet.getFonts()


def main():

    if len(sys.argv) == 3:
        arg = sys.argv[1]
        ufont = sys.argv[2]

        if arg not in ("-f", "--font"):
            sys.exit("Invalid argument")

        if ufont not in figlist:
            sys.exit("Font not found")

        figlet.setFont(font=ufont)

    else:
        random_font = random.choice(figlist)
        figlet.setFont(font=random_font)

    user_input = input("Input: ")

    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()
