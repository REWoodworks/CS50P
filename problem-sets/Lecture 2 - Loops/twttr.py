#When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


# def main():

#     twitter_prompt = input("Give me your string: ")

#     for letter in twitter_prompt:
#         if letter.lower() in ["a","e","i","o","u"]:
#             letter = ("")
#             print(letter, end="")
#         elif letter:
#             print(letter, end="")


# main()

## REVISION ONE...addressing the vowel branching printing an empty string
#     twitter_prompt = input("Give me your string: ")

#     for letter in twitter_prompt:
#         if letter.lower() in ["a","e","i","o","u"]:
#             continue
#         elif letter:
#             print(letter, end="")

# main()

## REVISION TWO....printing only non vowels

def main():

    twitter_prompt = input("Give me your string: ")

    for letter in twitter_prompt:
        if letter.lower() not in ["a","e","i","o","u"]:
            print(letter, end="")

main()