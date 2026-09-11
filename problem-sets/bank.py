def main():

    answer = input ("Greeting: ").strip().lower()

    if answer == ("hello"):
        print ("$0")
    elif answer.startswith("h"):
        print ("$20")
    else:
        print ("$100")

main ()
