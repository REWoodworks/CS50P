def main():
    dollars = dollars_to_float(input("How much was the meal? $##.##  "))

    # tip_dollars = dollars_to_float(dollars)
    # failed 1st effort.  didn't realize that the initial lines called the function directly

    percent = percent_to_float(input("What percentage would you like to tip? ##%  "))

    # tip_percent = percent_to_float(percent)
    # failed effort, thought percent to float was a variable being defined.
    #   it was in fact a function being called

    tip =dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.removeprefix("$"))

    return d
    

def percent_to_float(p):
    p = float(p.removesuffix("%"))
    p = p/100
        
    return p


main()