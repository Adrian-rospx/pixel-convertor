# Python image to pixel art converter
from pixelate import pixelate
from imgPath import get_image_path

# usage:
def main():
    # get image file path
    file = input("Enter the name of the file you want to pixelate: ")
    path = get_image_path(file)

    pixel_size = int(input("Enter the pixel size you want: "))

    img = pixelate(path, pixel_size)

if __name__ == "__main__":
    main()

