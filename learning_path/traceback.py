# NEED CLARITY ON WHY THE LINE NUMBERS LISTED IN TRACEBACK ARE NONINTUITIVE
# useful to fail, then trace back through what happened
# failure cause by div by 0
# main 36 called 14 print selected to pass an argument (actual fail step)
# to 32 parameter which passed parameter
# to 27 / 28 parameters which returned an illegal div by zero
# failure div by zero
# zero happened in 13 when select_expenses (argument) was sent to 17 and returned empty
#   to 13 which was handed to 14 as an argument (see above for path from there) 
#
def main():
    expenses = [4.50, 8.00, 12.50, 19.25]
    selected = select_expenses(expenses)
    print_report(selected)


def select_expenses(expenses):
    selected = []

    for expense in expenses:
        if expense > 100:
            selected.append(expense)

    return selected


def average(expenses):
    return sum(expenses) / len(expenses)


def print_report(expenses):
    result = average(expenses)
    print(f"Average qualifying expense: ${result:.2f}")


main()