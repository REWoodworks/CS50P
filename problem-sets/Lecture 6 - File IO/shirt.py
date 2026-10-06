"""In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

X if the user does not specify exactly two command-line arguments,
X if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
X if the input’s name does not have the same extension as the output’s name, or
X if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!"""

import os
import sys
from PIL import Image
from PIL import ImageOps

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")

    _, before_ext = os.path.splitext(sys.argv[1])
    _, after_ext = os.path.splitext(sys.argv[2])

    if before_ext.casefold() != after_ext.casefold():
        sys.exit("Before and after formats must be same")

    if before_ext.casefold() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Please use supported filetype .jpg, .jpeg, .png")

    with Image.open("shirt.png") as shirt:
        shirt_size = shirt.size

        try:
            with Image.open(sys.argv[1]) as img:
                img_resized = ImageOps.fit(img, shirt_size)   
        except FileNotFoundError:
            sys.exit("Input file not found")

        img_resized.paste(shirt, mask=shirt)
        output = sys.argv[2]
        img_resized.save(output)


if __name__ == "__main__":
    main()