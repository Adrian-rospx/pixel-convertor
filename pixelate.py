# using the Pillow library
from PIL import Image

# create a small image with pixels
def minimise(image: Image.Image, pixel_size) -> Image.Image:
    # resize and make the image smaller
    small: Image.Image = image.resize((image.width // pixel_size, image.height // pixel_size), 
                         resample = Image.Resampling.NEAREST)
    return small
    

# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8):
    # initialising the image
    img = Image.open(image_path, 'r')

    # make the image smaller
    small = minimise(image_path, pixel_size)

    # rescale back to original size
    rescaled: Image.Image = small.resize(img.size, resample = Image.Resampling.NEAREST)

    # show the result:
    rescaled.show()

    # add a suffix to the pixelated image
    dot_index = image_path.index(".")
    newpath = image_path[:dot_index] + "_pixel.png"
    print("saved as:")
    print(newpath)

    rescaled.save(newpath)