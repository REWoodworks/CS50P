
def area(length, width):
    print(str(length * width) + " square feet")
    return length * width  

def main():
    room = area(10,12)
    kitchen = area(8,10)
    total = room + kitchen
    print("Total area = " + str(total) + " square feet")
    
main()