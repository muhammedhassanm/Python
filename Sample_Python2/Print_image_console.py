# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:14:53 2020

@author: Muhammed Hassan M
"""


# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:20:35 2020

@author: 100119
"""
from IPython.display import Image, display

display(Image(filename='C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/TIF_29/TIF_29_Table_6.jpg'))



import glob

import matplotlib.pyplot as plt

import matplotlib.image as mpimg



def display_photo(path):

    print("File: {}".format(path))

    img = mpimg.imread(path)

    imgplot = plt.imshow(img)

    plt.show()

display_photo('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/TIF_29/TIF_29_Table_6.jpg')