# cowsay.cow('Hello World')
# print(cowsay.get_output_string('cow', 'Hello World'))
# cowsay.char_names
# ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
# 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
# 'turkey', 'turtle', 'tux']
# len(cowsay.chars)
# 19

# add path for random
# add conditional to take an arg 



import sys
import random
import cowsay

cow_dict = cowsay.char_names
random_cow = random.choice(cow_dict)

def main():
    
    if len(sys.argv) == 2:
        cowsay.cow("Hi, " + sys.argv[1])
    elif len(sys.argv) == 1:
        name = input ("What is your name?").upper()
        name = f"HI {name}"
        print(cowsay.get_output_string(random_cow, name))
    else:
        sys.exit

main ()

    