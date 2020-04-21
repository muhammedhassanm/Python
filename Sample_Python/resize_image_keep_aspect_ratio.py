# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:51:08 2020

@author: 100119
"""

import PIL
from PIL import Image

mywidth = 600

img = Image.open('E:/TEXT_DETECTION/TEXT_DETECT_IMAGE/test_images/MedicalExpenses(2days).jpeg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('resized.jpg')
