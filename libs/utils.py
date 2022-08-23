import numpy as np
from PIL import Image


def crop_raw(image: Image, length: float, v_shift: int, h_shift: int, dpi: int) -> Image:
    """Crops the original raw image.

    Crops and shifts the original raw image removing the borders.

    Arguments:
        image -- PIL.Image object containing the raw image.
        length -- Desired width and height of final image in centimeters (side length of scanned squared area in the experiments)
        v_shift -- The number of pixels to shift the image on the vertical axis (downward direction)
        h_shift -- The number of pixels to shift the image on the horizontal axis (right direction)
        dpi -- Dots per inch (DPI) of raw image (resolution used to scan the droplet patterns)

    Raises:
        Exception: Error cropping the image.

    Returns:
        Cropped image with the desired dimensions.
    """

    width, height = image.size   # Get dimensions of original image

    new_width = dpi/2.54 * length   # Set the desired width
    new_height = dpi/2.54 * length  # Set the desired height

    left = (width - new_width)/2 + h_shift       # Set the left pixel coordinate 
    top = (height - new_height)/2 + v_shift      # Set the top pixel coordinate
    right = (width + new_width)/2 + h_shift      # Set the right pixel coordinate
    bottom = (height + new_height)/2 + v_shift   # Set the bottom pixel coordinate

    # Validate the new pixel coordinates.
    if left<0 or right>width or top<0 or bottom>height:
        print(' width: {}\n height: {}'.format(width, height))
        print(' new_left: {}\n new_top: {}\n new_right: {}\n new_bottom: {}'.format(left, top, right, bottom))
        raise Exception('Error cropping the image. Check the shift values printed above. The image borders are exceeded.') 

    # Crop the image to the desired dimensions
    image_cut = image.crop((left, top, right, bottom))   # Crop the center of the image

    return image_cut


def get_p(binaryimage: Image) -> None:
    """Extracts the mean pixel value (p) of a binary image.
    
    Extracts pixel values matrix from a binary image, flattens the matrix to a single list and finds its mean.
    
    The parameter p corresponds to both the parameters <\overline{p_{o}}> (Latex formatting) and <\overline{p_{no}}>, since both are calculated the same way. Please refer to the article to know their difference and usage.

    Argument:
        binaryimage -- Binarized image. 
    """

    p = np.mean(np.array(binaryimage).flatten())
    
    print('p: {}'.format(p))