# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:27:39 2020

@author: Muhammed Hassan M
"""


from PIL import Image
import numpy as np

# name of your image file
filename = 'C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/TIF/25a5f5919a1fa404c303eb86ee6a16f15e9e979670153_228-001-000232-33-1.tif'

# open image using PIL
img = Image.open(filename)

# convert to numpy array
img = np.array(img)
img.shape
# find number of channels
if img.ndim == 2:
    channels = 1
    print("image has 1 channel")
else:
    channels = img.shape[-1]
    print("image has", channels, "channels")