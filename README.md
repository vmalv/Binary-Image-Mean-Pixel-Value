# Image Processing Script
Image Processing Script provided to reproduce the protocol described on the PLOS One article 'Relative assessment of cloth mask protection against ballistic droplets: a frugal approach' by V. Márquez-Alvarez, J. Amigó-Vega, A. Rivera, A. J. Batista-Leyva, and E. Altshuler.

TODO Add link to Arxiv

## Files and folders

Here you can find a description of each of the files and folders of the repository.
### Files

- main.py
Python script that contains an example of the extraction of the BBC and pnos parameters for different images.

- example.ipynb
Jupyter Notebook contains an example of the extraction of the BBC and pnos parameters for different images. Additionally, we have included some intermediate plots to help understand the image-preparation and parameter-extraction processes.
There are cases when the 'shift' parameter needs to be tuned because it could vary from one image to another. To select the proper one, we recommend using the notebook with the intermediate plots.

- libs/utils.py
Python file containing the utility functions used.

- requirements.txt
Contains the version information of the python libraries used.

### Folders

- data
We suggest placing in this directory the images that will be processed by the script.

- output
This directory contains the binarized images generated during the processing.

## Installation and first use

### Installing python
To install python for the first time, we suggest you use the following guide:
https://realpython.com/installing-python/

Although we used Python version 3.9.10, the code should run without problems with superior versions.

### Installing required packages

- With pip installed you can directly install the requirements file using the following line in the console:
    pip install -r requirements.txt

- If pip is not installed then you could manually download and install the python packages specified on the 'requirements.txt' file.
    In any case, we recommend installing the packages using pip. To install pip, the official documentation provides a step-by-step guide:
    https://pip.pypa.io/en/stable/installation/
    This guide provides some explanations that could help you with the manual installation process:
    https://www.geeksforgeeks.org/how-to-manually-install-python-packages/
