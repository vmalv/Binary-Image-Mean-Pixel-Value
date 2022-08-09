import numpy as np


def crop_raw(image, length, v_shift, h_shift, dpi):
    width, height = image.size   # Get dimensions of original image

    new_width = dpi/2.54 * length   # Get the desired width
    new_height = dpi/2.54 * length  # Get the desired height

    left = (width - new_width)/2 + h_shift       # Get the left pixel coordinate 
    top = (height - new_height)/2 + v_shift      # Get the top pixel coordinate
    right = (width + new_width)/2 + h_shift      # Get the right pixel coordinate
    bottom = (height + new_height)/2 + v_shift   # Get the bottom pixel coordinate

    # Validate the new pixel coordinates.
    if left<0 or right>width or top<0 or bottom>height:
        print(' width: {}\n height: {}'.format(width, height))
        print(' new_left: {}\n new_top: {}\n new_right: {}\n new_bottom: {}'.format(left, top, right, bottom))
        raise Exception('ERROR cropping the image. Check the shift values printed above, the image borders are exceeded.') 

    # Crop the image to the desired dimensions
    image_cut = image.crop((left, top, right, bottom))   # Crop the center of the image

    return image_cut


def bbc(binaryimage, meanpno):
    # Extract the BBC metric introduced in the paper. It takes as arguments a binary image and the mean_pno value. 
    # Two local variables are defined: "po" , the pixel mean value of an image corresponding to a CONFX (X=1,2,3,4)
    # experiment (analog to "pno" defined above); and "bbc" which follows the definition of BBC in the paper. 
    po = np.mean(np.array(binaryimage).flatten())
    bbc = (1 - po/meanpno)*100
    
    # TODO formatear bonito estos prints
    print('po: {}'.format(po))           # TODO ver cómo formatear el p_o y barrita encima
    print('<meanpno>: {}'.format(meanpno)) # TODO ver cómo formatear el p_no y barrita encima y entre <> (revisar la imagen guardada)
    print('BBC: {} %'.format(bbc))


def cloth_used(image, pnos):
    # Find the mean of pnos
    meanpno = np.mean(pnos)
    # Get the BBC value
    bbc(image, meanpno)


def no_cloth_used(image):
    # Extract pixel values matrix from the image, flatten the matrix to a single list and find its mean.
    pno = np.mean(np.array(image).flatten())
    return pno


def get_results(cloth, img, pnos=[]):
    # For CLOTH experiments
    if(cloth):
        if pnos:
            cloth_used(img, pnos)
        else:
            raise Exception('ERROR with input parameter. The parameter pnos is empty.')      
    # For NON-CLOTH experiments 
    else:
        pno = no_cloth_used(img)
        print('pno: ',pno) # TODO ver cómo formatear el p_no (sub) para que tenga una barrita encima
