import numpy as np
from PIL.Image import Image


def crop_raw(
    image: Image,
    length: float,
    v_shift: int,
    h_shift: int,
    dpi: int,
) -> Image:
    """
    Crops the original raw image.

    Crops and shifts the original raw image removing the borders.

    Parameters
    ----------
    image : Image
        PIL.Image object containing the raw image.
    length : float
        Desired width and height of final image in centimeters (side
        length of scanned squared area in the experiments).
    v_shift : int
        The number of pixels to shift the image on the vertical
        axis (downward direction).
    h_shift : int
        The number of pixels to shift the image on the horizontal
        axis (right direction).
    dpi : int
        Dots per inch (DPI) of raw image (resolution used to scan
        the droplet patterns).

    Raises
    ------
    Exception
        If the image cannot be cropped to the desired dimensions.

    Returns
    -------
    Image
        Cropped image with the desired dimensions.
    """

    # Get dimensions of original image
    width, height = image.size

    # Set desired dimensions of cropped image
    new_width = dpi / 2.54 * length
    new_height = dpi / 2.54 * length

    # Set boundaries pixel coordinates
    left = int((width - new_width) / 2 + h_shift)
    top = int((height - new_height) / 2 + v_shift)
    right = int((width + new_width) / 2 + h_shift)
    bottom = int((height + new_height) / 2 + v_shift)

    # Validate the new pixel coordinates.
    if left < 0 or right > width or top < 0 or bottom > height:
        print(f" width: {width}", f"height: {height}", sep="\n")
        print(
            f" new_left: {left}",
            f" new_top: {top}",
            f" new_right: {right}",
            f" new_bottom: {bottom}",
            sep="\n",
        )
        raise Exception(
            "Error cropping the image. Check the shift values printed above. "
            "The image borders are exceeded."
        )

    # Returns the image cropped to the desired dimensions
    return image.crop((left, top, right, bottom))


def get_p(binaryimage: Image) -> None:
    """
    Extracts the mean pixel value (p) of a binary image.

    Extracts pixel values matrix from a binary image, flattens the matrix to a
    single list and finds its mean.

    The parameter p corresponds to both the parameters <\\overline{p_{o}}>
    (Latex formatting) and <\\overline{p_{no}}>, since both are calculated the
    same way. Please refer to the article to know their difference and usage.

    Parameters
    ----------
    binaryimage : Image
        Binarized image.
    """

    p = np.mean(np.array(binaryimage).flatten())
    print(f"p: {p}")
