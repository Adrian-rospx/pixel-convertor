# Python image to pixel art converter
# using the Pillow library
from PIL import Image

# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8):
    # initialising the image
    img = Image.open(image_path, 'r')

    # resize and make the image smaller
    smaller: Image.Image = img.resize(img.width // pixel_size, img.height // pixel_size, 
                         resample = Image.Resampling.NEAREST)
    
    # rescale back to original size
    rescaled: Image.Image = smaller.resize(img.size, resample = Image.Resampling.NEAREST)

    # show the result:
    rescaled.show()
    rescaled.save("images/pixelated.png")

