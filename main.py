# Python image to pixel art converter
from pixelate import pixelate

# usage:
def main():
    path = input("Enter the name of the file you want to pixelate: ")
    path = "Images/"+ path

    pixel_size = int(input("Enter the pixel size you want: "))

    pixelate(path, pixel_size)

if __name__ == "__main__":
    main()

