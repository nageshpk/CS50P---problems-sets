import sys
from PIL import Image, ImageOps


def main():
    call_overlay_images()


def call_overlay_images():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[2].split(".")[1] not in ['png', 'jpg']:
        sys.exit("Invalid output")
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and Output have different extensions")
    else:
        try:
            overlay_images()
        except FileNotFoundError:
            sys.exit(f"Input does not exist")


def overlay_images():
    shirt = Image.open("shirt.png").convert("RGBA")
    before = Image.open(sys.argv[1])
    before = ImageOps.fit(before, size=shirt.size)
    before.paste(shirt, shirt)
    before.save(sys.argv[2])


main()