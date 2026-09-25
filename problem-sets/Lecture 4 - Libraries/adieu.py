# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

# references Pypi https://pypi.org/project/inflect/
# pip -m install inflect

import inflect

p = inflect.engine()
# names_list = [] # moving inside main to avoid stray global variable


def main():

    names_list = []

    while True:
        try:
            name = input("Name: ").strip().title()
            names_list.append(name)
            # continue    # unused, while loop will cycle without
        except EOFError:
            print()
            break

    print(f"Adieu, adieu, to {p.join(names_list)}")


main()
