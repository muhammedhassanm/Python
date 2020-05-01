# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:29:11 2020

@author: Muhammed Hassan M
"""


import PIL
from PIL import Image

mywidth = 1000

img = Image.open('C:/Users/Muhammed Hassan M/Desktop/Well_Log_14.png')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('resized.jpg')
