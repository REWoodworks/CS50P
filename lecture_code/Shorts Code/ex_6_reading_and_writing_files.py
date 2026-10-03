def main():
    with open("alice.txt", "r") as f:   
        contents = f.readlines()    #returns a LIST of lines in file


    chapter1 = contents[52:272] # uses a slice ro take a 
    
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)


main()