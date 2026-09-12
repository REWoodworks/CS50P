## building a calculator.

def main():

    answer = input("Expression:")

    first_number, operator, second_number = answer.split()

    first_number = float(first_number)
    second_number = float(second_number)

    if operator == "+":
        result = first_number + second_number
    elif operator == "/":
        result = first_number / second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    else:
        print ("invalid operator")
        return

    print(f"{result:.1f}")




main()

