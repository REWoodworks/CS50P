# %% [markdown]
# <!-- names0.py -->
#
# Stores a single name in a variable and greets it. This is the starting point: the name is lost as soon as the program ends.

# %%
# Stores a name in a variable

name = input("What's your name? ")
print(f"hello, {name}")


# %% [markdown]
# <!-- names1.py -->
#
# Collects three names into a list and greets them in sorted order. Compared with the previous block, it handles many names, but they still vanish when the program exits.

# %%
# Stores names in a list

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


# %% [markdown]
# <!-- names.txt -->
#
# A plain-text data file with one name per line. The following programs write to and read from this file.
#
# ```
# Hermione
# Harry
# Ron
# Draco
# ```

# %% [markdown]
# <!-- names2.py -->
#
# Opens `names.txt` in write mode (`"w"`), writes the name, and closes the file. Compared with the previous blocks, the data now persists after the program ends, but `"w"` overwrites the file on every run.

# %%
# Writes to a file

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()


# %% [markdown]
# <!-- names3.py -->
#
# Switches to append mode (`"a"`) and adds a `\n` after each name. Compared with the previous block, names accumulate on separate lines instead of replacing each other.

# %%
# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# %% [markdown]
# <!-- names4.py -->
#
# Uses `with open(...) as file:`, a context manager that closes the file automatically. Compared with the previous block, there is no `file.close()` to forget.

# %%
# Adds context manager

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# %% [markdown]
# <!-- names5.py -->
#
# Reads every line into a list with `readlines()`, then greets each name, using `rstrip()` to remove the trailing newline. This is the first block that reads from the file instead of writing to it.

# %%
# Reads from a file

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())


# %% [markdown]
# <!-- names6.py -->
#
# Loops over the file object directly, one line at a time. Compared with the previous block, it skips the intermediate `lines` list.

# %%
# Reads from a file, one line at a time

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())


# %% [markdown]
# <!-- names7.py -->
#
# Reads the names into a list first, then greets them in sorted order. Compared with the previous block, it can sort because it collects everything before printing.

# %%
# Appends names to a list for sorting

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# %% [markdown]
# <!-- students0.csv -->
#
# A CSV (comma-separated values) file: each line holds a name and a house, separated by a comma.
#
# ```
# Hermione,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin
# ```

# %% [markdown]
# <!-- students0.py -->
#
# Splits each line on `","` into a list and prints `row[0]` and `row[1]`. This is the first block that works with more than one value per line.

# %%
# Reads a CSV file

with open("students0.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# %% [markdown]
# <!-- students1.py -->
#
# Unpacks the split result straight into `name, house`. Compared with the previous block, the names make the code easier to read than `row[0]` and `row[1]`.

# %%
# Unpacks a list

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# %% [markdown]
# <!-- students2.py -->
#
# Builds a list of the finished sentences and prints them sorted. Compared with the previous block, the output is sorted, but only by the whole sentence, so it can't sort by house.

# %%
# Sorts a list of strings

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# %% [markdown]
# <!-- students3.py -->
#
# Stores each student as a `dict` with `"name"` and `"house"` keys, starting from an empty dict and filling it in. Compared with the previous block, the data keeps its structure instead of being flattened into a string.

# %%
# Reads a CSV file into a list of dict objects, creating empty dict first

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# %% [markdown]
# <!-- students4.py -->
#
# Builds each dict in one step with `{"name": name, "house": house}`. Compared with the previous block, two assignment lines collapse into one.

# %%
# Reads a CSV file into a list of dict objects, creating dict first

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# %% [markdown]
# <!-- students5.py -->
#
# Appends the dict directly without the temporary `student` variable. Compared with the previous block, it is one line shorter and does the same thing.

# %%
# Reads a CSV file into a list of dict objects

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in students:
    print(f"{student['name']} is in {student['house']}")


# %% [markdown]
# <!-- students6.py -->
#
# Passes a function, `get_name`, as the `key=` argument to `sorted`, which tells it what to sort dicts by. Compared with the previous block, it can now sort a list of dicts by name.

# %%
# Sorts a list of dictionaries using a function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


# %% [markdown]
# <!-- students7.py -->
#
# Replaces `get_name` with a `lambda`, an anonymous one-line function written in place. Compared with the previous block, the sort works the same without a separately named function.

# %%
# Sorts a list of dictionaries using a lambda function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


# %% [markdown]
# <!-- students1.csv -->
#
# A new CSV whose first value contains a comma, so it is wrapped in quotes. A plain `split(",")` would break this line into three pieces.
#
# ```
# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor
# ```

# %% [markdown]
# <!-- students8.py -->
#
# Uses the `csv` library's `csv.reader`, which understands quoted fields. Compared with the previous block, it handles commas inside values correctly. It reads `students1.csv` and uses a `"home"` key instead of `"house"`.

# %%
# Reads a CSV file using csv.reader

import csv

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# %% [markdown]
# <!-- students2.csv -->
#
# The same data with a header row (`name,home`) that names each column.
#
# ```
# name,home
# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor
# ```

# %% [markdown]
# <!-- students9.py -->
#
# Uses `csv.DictReader`, which reads the header row and gives back each row as a dict keyed by column name. Compared with the previous block, it uses `row["name"]` instead of `row[0]`, so it keeps working if the columns are reordered.

# %%
# Reads a CSV file using csv.DictReader

import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# %% [markdown]
# <!-- students10.py -->
#
# Writes a new row to `students2.csv` with `csv.writer`, passing a list of values. This switches from reading CSV files to writing them; the library adds quotes when a value contains a comma.

# %%
# Writes a CSV file using csv.writer

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# %% [markdown]
# <!-- students11.py -->
#
# Uses `csv.DictWriter` with `fieldnames`, passing a dict instead of a list. Compared with the previous block, values are matched to columns by name rather than by position.

# %%
# Writes a CSV file using csv.DictWriter

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


# %% [markdown]
# <!-- costumes.py -->
#
# Opens image files named on the command line with the third-party `PIL` (Pillow) library and saves them as an animated GIF. This moves from text files to binary files. Run it as `python costumes.py costume1.gif costume2.gif`.

# %%
# Opens and saves binary files

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
