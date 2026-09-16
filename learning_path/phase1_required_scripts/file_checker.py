#The goal is to check a filename and report whether it ends in .csv.
#


def main():

    userfile= input("File name? ").lower()

    if userfile.endswith(".csv"):
        print ("Valid CSV Filename")
    else:
        print ("Not a CSV filename")


main()