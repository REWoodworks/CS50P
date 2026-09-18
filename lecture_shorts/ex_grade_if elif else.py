## using AND with if, elif, else, and and operators to demonstrate different ways to compare two numbers and print out the result.
## note the use of ELSE to end the pattern

score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# removes the AND operator and uses chained comparisons to demonstrate different ways to compare two numbers and print out the result.
# tightens the code and makes it more readable. Chained comparisons are a more efficient way to compare two numbers and print out the result.

score = int(input("Score: "))
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# removes AND and chained comparisons and uses only the >= operator to demonstrate different ways to compare two numbers and print out the result.
# final reduction, most elegant according to professor. This is the most efficient way to compare two numbers and print out the result.

score = int(input("Score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")