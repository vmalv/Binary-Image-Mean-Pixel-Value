from typing import Type
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


def bbc(binaryimage: Image, meanpno: float) -> None:
    """Extracts the BBC metric introduced in the paper.

    It takes as arguments a binary image and the mean_pno value. 
    Two local variables are defined: "po" , the pixel mean value of an image corresponding to a CONFX (X=1,2,3,4)
    experiment (analog to "pno" defined above); and "bbc" which follows the definition of BBC in the paper.

    Arguments:
        binaryimage -- Binarized image.
        meanpno -- Pixel mean value. 
    """

    po = np.mean(np.array(binaryimage).flatten())
    bbc = (1 - po/meanpno)*100
    
    # TODO formatear bonito estos prints
    print('po: {}'.format(po))           # TODO ver cómo formatear el p_o y barrita encima
    print('<meanpno>: {}'.format(meanpno)) # TODO ver cómo formatear el p_no y barrita encima y entre <> (revisar la imagen guardada)
    print('BBC: {} %'.format(bbc))


def cloth_used(image: Image, pnos: list) -> None:
    """Extract the BBC value of an image captured using a cloth.

    Calculates the meanpno of the Extract the BBC value of an image captured using a cloth. 

    Arguments:
        image -- Image to extract the BBC from.
        pnos -- A list containing the pixel mean values of all CONFFREE experiments previously made.
    """    

    # Find the mean of pnos
    meanpno = np.mean(pnos)
    # Get the BBC value
    bbc(image, meanpno)


def no_cloth_used(image: Image) -> np.array:
    """Extract the pno parameter of an image captured not using a cloth.

    Extract pixel values matrix from the image by flattening the image to a single list and finding its mean.

    Arguments:
        image -- Image to extract the pno from.

    Returns:
        Pixel values matrix.
    """
     
    pno = np.mean(np.array(image).flatten())
    return pno


def get_results(cloth: bool, img: Image, pnos: list = []) -> None:
    """Extract the parameters required for the particular case.

    The parameter 'cloth' defines if for the image inputted a cloth was used. In this case a call to the
    function cloth_used() is raised to obtain the BBC. Otherwise no_cloth_used() is called to obtain the pno. 

    Arguments:
        cloth -- Defines if a cloth material was used for this experiment.
        img -- Image to extract the parameters from.

    Keyword Arguments:
        pnos -- Pixel mean values of all CONFFREE experiments previously made (default: {[]}).

    Raises:
        Exception: Error with input parameter.
    """

    # For CLOTH experiments
    if(cloth):
        if pnos:
            cloth_used(img, pnos)
        else:
            raise Exception('Error with input parameter. The parameter pnos is empty.')      
    # For NON-CLOTH experiments 
    else:
        pno = no_cloth_used(img)
        print('pno: ',pno) # TODO ver cómo formatear el p_no (sub) para que tenga una barrita encima


def get_p(binaryimage: Image) -> None:
    """Extracts the mean pixel value (p) of a binary image.
    
    Extracts pixel values matrix from a binary image, flattens the matrix to a single list and finds its mean.
    
    The parameter p corresponds to both the parameters <\overline{p_{o}}> (Latex formatting) and <\overline{p_{no}}>, since both are calculated the same way. Please refer to the article to know their difference and usage.

    Argument:
        binaryimage -- Binarized image. 
    """

    p = np.mean(np.array(binaryimage).flatten())
    
    print('p: {}'.format(p))