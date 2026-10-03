# CS50P Week 6 Short: CSV
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Needs views.csv, the matching <id>.jpeg images, numpy, and Pillow to run.


# -----------------------------------------------------------------------------
# Version 0 - views0.py
# Defines calculate_brightness, which converts an image to grayscale ("L"),
# averages its pixels with numpy, and scales the result to 0-1. main is still a
# placeholder.

import numpy as np
from PIL import Image


def main(): ...


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


# -----------------------------------------------------------------------------
# Version 1 - views1.py
# Opens views.csv with csv.DictReader and prints each row as a dict keyed by
# the header names.

import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


# -----------------------------------------------------------------------------
# Version 2 - views2.py
# Uses each row's id to build an image filename and prints that image's
# brightness, rounded to two places.

import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness, 2))


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


# -----------------------------------------------------------------------------
# Version 3 - views3.py
# Opens views.csv for reading and analysis.csv for writing in one with
# statement. Sets up a csv.DictWriter whose columns are the original headers
# plus "brightness", and writes the header row. Rows are still only printed.

import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness, 2))


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


# -----------------------------------------------------------------------------
# Version 4 - views4.py
# Writes each row to analysis.csv by building a new dict that lists every
# column by name, including the rounded brightness.

import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()


# -----------------------------------------------------------------------------
# Version 5 - views5.py
# Adds the "brightness" key to the existing row dict and writes that row
# directly, so the columns no longer have to be typed out by hand.

import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
