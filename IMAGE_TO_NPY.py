# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:43:04 2020

@author: 100119
"""

import numpy as np
import pandas as pd
import cv2
import os
import tqdm
import glob
from scipy.io import loadmat
import matplotlib.pyplot as plt

image_path = 'Test/'
image_path_list = []

files = glob.glob ("Test/*.jpg")
for myFile in files:
    image = cv2.imread (myFile)
    image_path_list.append (image)
    

test = np.array(image_path_list,dtype='float32') #as mnist example

test = np.reshape(test,[test.shape[0],test.shape[1]*test.shape[2]*test.shape[3]])

# save numpy array as .npy formats
np.save('test',test) # saves test.npy