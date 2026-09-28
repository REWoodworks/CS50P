# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():

    twitter_prompt = input("Give me your string: ")
    word = shorten(twitter_prompt)

    print(word)

    #for _ in len(word):
    #    print


def shorten(word):

    letter = []

    for alpha in word:
        if alpha.lower() not in ["a","e","i","o","u"]:
            letter.append(alpha)
    
    return "".join(letter)


if __name__ == "__main__":
    main()