# Binary Image Mean Pixel Value

[![Python](https://img.shields.io/badge/-Python-blue?logo=Python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?logo=opensourceinitiative&logoColor=white)](/LICENSE)
![GitHub repo size](https://img.shields.io/github/repo-size/vmalv/Binary-Image-Mean-Pixel-Value?color=chocolate&label=Repo%20size&logo=GitHub)
[![Zenodo](https://img.shields.io/badge/Raw%20images%20repo-10.5281%2Fzenodo.6941696-blue?logo=Zenodo&logoColor=white&logoWidth=15)](https://doi.org/10.5281/zenodo.6941696)


Python script to binarize an RGB image and find its mean pixel value.

This script was built for the image processing of the data reported on "Márquez-Alvarez V, Amigó-Vera J, Rivera A, Batista-Leyva AJ, Altshuler E. Relative assessment of cloth mask protection against ballistic droplets: a frugal approach. PLOS One; 2022."

Please refer to the article to understand the context, main use case and definition of parameters used in the script.

Sample raw images that can be used to test the script can be found at "Márquez-Alvarez V, Altshuler E. Raw images corresponding to article 'Relative assessment of cloth mask protection against ballistic droplets: a frugal approach.' Zenodo; 2022. doi: [10.5281/zenodo.6941696](https://doi.org/10.5281/zenodo.6941696)".

### Intended usage

This script is publicly hosted in this repository to allow the reproduction of the results reported on the article. 

Nevertheless, further applications are encouraged. 


## Files and folders

Here you can find a description of each file and folder in the repository. It takes an image and some parameters as arguments

### Files

- **[main.py](/main.py)**
Python script that contains the minimum coding required to fulfill the script goal.

- **[example.ipynb](/example.ipynb)**
Jupyter Notebook that contains an example using the script. Intermediate plots are included to help understanding each step in the image-preparation and parameter-extraction processes.

- **[libs/utils.py](/libs/utils.py)**
Python file containing the utility functions used.

- **[requirements.txt](/requirements.txt)**
Text file containing the version information of the Python libraries used.

### Folders

- **[input](/input)**
Suggested directory to place the image(s) that will be processed by the script.

- **[output](/output)**
Directory that contains the binarized image(s) exported by the script.


## Requirements

To use the script you must download the repository files, have Python>=3.9.10 installed as well as the packages included in the 'requirements.txt' file.

### Downloading repository files

If you have [Git](https://git-scm.com/ "Git official website") installed, you can open the terminal, go to the path where you want to download the repository and simply run

    git clone https://github.com/vmalv/Binary-Image-Mean-Pixel-Value.git

If you need help installing Git see this [link](https://github.com/git-guides/install-git "https://github.com/git-guides/install-git").

If you do not want to install Git, or simply don't want to open a local Git repo, download the repository files using this link 

> <https://github.com/vmalv/Binary-Image-Mean-Pixel-Value/archive/refs/heads/main.zip>

and extract the ZIP file in the directory of your preference.

### Installing Python

To install Python for the first time, this [guide](https://realpython.com/installing-python/ "https://realpython.com/installing-python/") could be useful.

Although we used Python version 3.9.10, the code should run without problems with superior versions.

### Installing required packages

We recommend using [pip](https://pip.pypa.io/ "pip official website") to install the required packages --contained in 'requirements.txt'. If you need help installing pip, the official documentation provides a step-by-step [guide](https://pip.pypa.io/en/stable/installation/ "https://pip.pypa.io/en/stable/installation/").

With pip installed, open a terminal in the repository directory and run the following code:

    pip install -r requirements.txt


## Script workflow

In general terms, the script workflow is as follows:

1. Load libraries and image parameters.
2. Load raw image.
3. Crop raw image.
4. Select the RGB component with best stains-background contrast.
5. Binarize the RGB component and export it.
6. Get the binary image mean pixel value.

It is strongly recommended to see [example.ipynb](/example.ipynb) and [libs/utils.py](/libs/utils.py) for a detailed explanation of each line of the code.

## Further steps to calculate BBC

The script itself can be used for any application where it is suited. However, if you are looking to reproduce our results, or make a new research based on ours, further steps are necessary to calculate the BBC parameter for a given blocking material and configuration.

1. Run the script for all the raw scanned images corresponding to CONFFREE experiments (experiments made with no cloth at any position). For each one of these experiments you will get a mean pixel value (p). The mean of all p values in CONFFREE corresponds to the parameter <\overline{p_{no}}> (Latex formatting) introduced in the article. 
2. Suppose you make a set of experiments with a given blocking material in CONF1 (if the experiments were made in CONF2, CONF3 or CONF4 the steps would be identical). Run the script for the set of raw scanned images obtained. You will get the corresponding set of p values. The mean of these p values corresponds to the parameter <\overline{p_{o}}> presented in the article.
3. Calculate BBC using the formula (1) from the article.
4. For BBC uncertainty, refer to S1 Supporting Information Section C.

In this example you obtain the BBC value of the given blocking material in CONF1. For the rest of configurations and materials, repeat steps from 2 to 4.

## License

Copyright (c) 2022 vmalv, jamigov

This repository and its entire content is available under the MIT license. See the [LICENSE](/LICENSE) file for more info.
