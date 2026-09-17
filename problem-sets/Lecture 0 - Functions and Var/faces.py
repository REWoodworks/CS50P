#replaces user answer with emokis (smiley and frowny faces)

def main ():
    
    answer = input("Happy or Sad?")

    converted_answer = convert(answer)

    print (converted_answer)


def convert(text):
    text = text.replace(":)", "🙂").replace("=)", "🙂")
    text = text.replace(":(", "🙁").replace("=(", "🙁")
    return text

  

main()

   


