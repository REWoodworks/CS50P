# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below: (list formed in code) Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



def main():

    while True:
        user_date = input("Input the Date: ")
        try:
            month, day, year = user_date.split(sep="/")
            month = int(month)
            day = int(day)
            year = int(year)
            checked_date = new_date(month, day, year)
            if checked_date:    # == True:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        except ValueError:
            try:
                month, day, year = user_date.split(sep=" ")
                month = months.index(month) + 1
                # month = int(month) + 1 while using periods above
                day = int(day.replace(",", ""))
                # day = int(day) while using periods above
                year = int(year)
                checked_date = new_date(month, day, year)
                if checked_date:    # == True:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
            except ValueError:
                print("Input date Ex. '9/8/1936' or 'September 8, 1936'") 
                continue  
        #else:
        #    break

def new_date(month, day, year):
    if not 0 < month <= 12 or not 0 < day <= 31:
        print ("Please enter date with a month range 1-12 and day 1-31")
        return False
    else:
        return True            
    # print(f"{year}-{month:02}-{day:02}")






main()