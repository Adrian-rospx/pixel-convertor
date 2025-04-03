# using the Pillow library
from PIL import Image

# define a pixelate function to setup functionality
def pixelate(image_path: str, pixel_size = 8):
    # initialising the image
    img = Image.open(image_path, 'r')

    # resize and make the image smaller
    smaller: Image.Image = img.resize((img.width // pixel_size, img.height // pixel_size), 
                         resample = Image.Resampling.NEAREST)
    
    # rescale back to original size
    rescaled: Image.Image = smaller.resize(img.size, resample = Image.Resampling.NEAREST)

    # show the result:
    rescaled.show()

    # add a suffix to the pixelated image
    dot_index = image_path.index(".")
    newpath = image_path[:dot_index] + "_pixel.png"
    print("saved as:")
    print(newpath)

    rescaled.save(newpath)