#replaces user answer with emokis (smiley and frowny faces)

def main ():
    
    answer = input(":( or :)? ")

    converted_answer = convert(answer)

    print (converted_answer)




def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

  

main()

   


