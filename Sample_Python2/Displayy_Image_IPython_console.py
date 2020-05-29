# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:20:35 2020

@author: 100119
"""
from IPython.display import Image, display

display(Image(filename='C:/Users/100119/Desktop/OIL_&_GAS/CONTOURS_DETECTED_IMAGES/TIF_15/TIF_15_Table_7.jpg'))



import glob

import matplotlib.pyplot as plt

import matplotlib.image as mpimg



def display_photo(path):

    print("File: {}".format(path))

    img = mpimg.imread(path)

    imgplot = plt.imshow(img)

    plt.show()

display_photo('C:/Users/100119/Desktop/OIL_&_GAS/CONTOURS_DETECTED_IMAGES/TIF_15/TIF_15_Table_7.jpg')