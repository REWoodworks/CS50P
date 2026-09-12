def main():

    answer = input ("File name: ").strip().lower()

    if answer.endswith (".gif"):
        print ("image/gif")
    elif answer.endswith (".jpg") or answer.endswith (".jpeg"):
        print ("image/jpg")
    elif answer.endswith (".png"):
        print ("image/png")
    elif answer.endswith (".pdf"):
        print ("image/pdf")
    elif answer.endswith (".txt"):
        print ("image/txt")
    elif answer.endswith ("zip"):
        print ("image/zip")
    else:
        print ("application/octet-stream")

main ()
