# using the Pillow library
from PIL import Image

from outline import add_outline

# create a small image with pixels
def minimise(image: Image.Image, pixel_size) -> Image.Image:
    # resize and make the image smaller
    small: Image.Image = image.resize((image.width // pixel_size, image.height // pixel_size), 
                         resample = Image.Resampling.NEAREST)
    return small
    
# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8) -> Image.Image:
    # initialising the image
    img = Image.open(image_path, 'r')

    # make the image smaller
    small = minimise(img, pixel_size)
    # show small image outline
    small: Image.Image = add_outline(small)
    small.show()

    # rescale back to original size
    rescaled: Image.Image = small.resize(img.size, resample = Image.Resampling.NEAREST)

    # show the result:
    rescaled.show()
    # return the rescaled image
    return rescaled