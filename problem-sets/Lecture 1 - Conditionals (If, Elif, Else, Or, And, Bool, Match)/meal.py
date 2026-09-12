# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
# lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you 
# had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether 
# it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, 
# don’t output anything at all. Assume that the user’s input will be formatted in 24-hour 
# time as #:## or ##:##. And assume that each meal’s time range is inclusive. 
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, 
# it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) 
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance,
#  given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("Its breakfast time!")

    elif 12 <= converted_time <= 13:
        print("Its lunch time!")

    elif 18 <= converted_time <= 19:
        print("Its dinner time!")

    else:
        print("Its not time to eat.")


def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) / 60
    time=float(hour) +minutes
    return time

# -initial errors surrounded the splitting of the time string.  I splt on spaces, which is called normally and needed to add a : into the ()
#   so that .split splits around :'s.  
# -error also made at handling of minutes.  float(minutes/60) took minutes as text from the above split.  float(minutes) / 60 solved the problem.
# finally, time was cahnged to float the hour such that everything in the variable "time" was a float and could be returned to "converted_time" 
#   as a flaot....which could be if argued.



if __name__ == "__main__":
    main()

