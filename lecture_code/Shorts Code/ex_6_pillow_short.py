# CS50P Week 6 Short: Pillow (Images)
# Review compilation: each complete lecture version is preserved in sequence.
# Running this combined file would run every version, so it is intended for review.
# Needs an in.jpeg image and Pillow (pip install pillow) to run.


# -----------------------------------------------------------------------------
# Version 0 - image0.py
# Opens an image with Pillow's Image.open and closes it again by hand.

from PIL import Image


def main():
    img = Image.open("in.jpeg")
    img.close()


main()


# -----------------------------------------------------------------------------
# Version 1 - image1.py
# Prints the image's size (width, height) and format before closing it.

from PIL import Image


def main():
    img = Image.open("in.jpeg")
    print(img.size)
    print(img.format)
    img.close()


main()


# -----------------------------------------------------------------------------
# Version 2 - image2.py
# Uses a with statement (context manager) so the image closes automatically,
# replacing the manual img.close().

from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)


main()


# -----------------------------------------------------------------------------
# Version 3 - image3.py
# Rotates the image 180 degrees and saves it as out.jpeg. rotate returns a new
# image, so the result is assigned back to img.

from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img.save("out.jpeg")


main()


# -----------------------------------------------------------------------------
# Version 4 - image4.py
# Imports ImageFilter and applies a blur after rotating.

from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("out.jpeg")


main()


# -----------------------------------------------------------------------------
# Version 5 - image5.py
# Swaps the blur for ImageFilter.FIND_EDGES, which highlights outlines.

from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


main()
