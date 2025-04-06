# using the Pillow library
from PIL import Image

from outline import add_outline
from imgPath import suffix, new_image_path

# create a small image with pixels
def minimise(image: Image.Image, pixel_size: int) -> Image.Image:
    # resize and make the image smaller
    small: Image.Image = image.resize((image.width // pixel_size, image.height // pixel_size), 
                         resample = Image.Resampling.NEAREST)
    return small

# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8) -> Image.Image:
    # initialising the image
    img = Image.open(image_path, 'r')

    # make the image smaller
    small: Image.Image = minimise(img, pixel_size)
    # add outline to PNGs
    if suffix(image_path) == ".png":
        small = add_outline(small)

    # rescale back to original size
    rescaled: Image.Image = small.resize(img.size, resample = Image.Resampling.NEAREST)

    # show the result:
    rescaled.show()
    # return the rescaled image
    return rescaled

# save the image with a new suffix
def save_img(image: Image.Image, original_path: str):
    # obtain the new filename and path
    path = new_image_path(original_path)

    image.save(path)