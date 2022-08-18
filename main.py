from PIL import Image
import PIL.ImageOps
import os

from libs import utils

## Parameters

# raw image filename and extension
file = "TelaAzul_Conf1_Exp1_3200dpi"
ext = ".bmp"

# Dots per inch (DPI) used to scan the droplet patterns
dpi = 3200

# Length and width of scanned squared area in centimeters
length = 5.0

# Binary threshold used to binarize the images. 0.3 gives the most accurate results with our materials, 
# but any other value can be used. 
binary_threshold = 0.3

# Sometimes when the image is cropped, the borders used as reference, are not completely removed. 
# These two parameters allow us to adjust such shifts. They are the number of pixels to shift the image on 
# the vertical and horizontal axis.
v_shift = 0
h_shift = 0

# Defines if a CLOTH was used for this experiment
cloth = True

# The parameter 'pnos' should contain the pixel mean values of all CONFFREE experiments previously made
pnos = [0.309129, 0.291286, 0.270232, 0.269421]

# Load raw image
raw = Image.open(os.path.join(os.path.dirname(__file__),'data', file+ext))

# Crop "raw" image to ensure it is 5x5 cm^2 (1 inch = 2.54 cm). Be sure no reference marks printed on the
# paper remain included inside the cropped image. Note that after cropping we keep the center of the 
# original image, i.e. borders are removed until specified dimensions are satisfied
rawcut = utils.crop_raw(raw, length, v_shift, h_shift, dpi)

# Negate "rawcut" image and take its first (red) component in RGB
# color space. As our stains are blue and background is white, this
# component gives the best contrast between stains and background. In
# case of using another color for stains and/or background, select the
# component that maximizes the contrast between them.
rawneg = PIL.ImageOps.invert(rawcut)
rawnegred, _, _ = rawneg.split()

# Binarize the image using the parameter binary_threshold. All values below or equal are converted to 1 and above to 0.
# With the point() function we are able to map each pixel through a function. 
# In our case we use it for the binarization of the image.  
binary = rawnegred.point(lambda p: 1 if p >= (binary_threshold*255) else 0)

# The values of the binarized image are converted to the 0-255 scale for being saved on a file.
output = binary.point(lambda p: p*255)
output.save(os.path.join(os.path.dirname(__file__),'output', 'Binary_' + file + ext))
print('Binarized image generated under the name: {}'.format('Binary_' + file + ext))

# calculate the output parameters for this experiment and print them
utils.get_results(cloth, binary, pnos)
