from PIL import Image

def is_transparent_px(pixel: tuple) -> bool:
    if pixel[3] == 0:
        return True
    else:
        return False

def create_outline(src_img: Image.Image) -> Image:
    # use the alpha channel of the image
    src_img.convert("RGBA")
    width, height = src_img.size
    # pixel access object:
    pixels = src_img.load()

    # store the outline of the image
    outline_img = Image.new("RGBA", (width, height), (0,0,0,0))
    outline_pixels = outline_img.load()

    # iterate through all pixels
    for x in range(width):
        for y in range(height):
            # skip non-transparent pixels
            if not is_transparent_px(pixels[x,y]):
                continue
            
            # verify for non transparent edges
            is_edge = False
            for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # Skip the pixel itself
                        if dx == 0 and dy == 0:
                            continue
                        # Skip image boundries
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= width or ny >= height:
                            continue
                        # If a neighbor is not transparent, 
                        # mark this as an edge pixel
                        if not is_transparent_px(pixels[nx, ny]):
                            is_edge = True
            # If an edge is detected, set the outline pixel to black
            if is_edge:
                outline_pixels[x, y] = (0, 0, 0, 255)

    return outline_img
    
# add an outline over the transparent image
def add_outline(src_img: Image.Image) -> Image:
    outline = create_outline(src_img)
    # composite the outline onto the original image
    combined = Image.alpha_composite(src_img, outline)

    return combined
