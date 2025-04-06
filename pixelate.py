# using the Pillow library
from PIL import Image
from outline import add_outline

# create a small image with pixels
def minimise(image: Image.Image, pixel_size) -> Image.Image:
    # resize and make the image smaller
    small: Image.Image = image.resize((image.width // pixel_size, image.height // pixel_size), 
                         resample = Image.Resampling.NEAREST)
    return small
    
# generate the new image path and type it's new name
def newPath(image_path: str):
    dot_index = image_path.index(".")
    new_path = image_path[:dot_index] + "_pixel.png"

    print("saved as:")
    print(new_path)

    return new_path

# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8):
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

    # Setup the new image path
    new_path = newPath(image_path)

    rescaled.save(new_path)