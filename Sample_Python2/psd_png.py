# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:21:59 2020

@author: Muhammed Hassan M
"""

import os
from psd_tools import PSDImage
from PIL import Image

IMG_DIR =r'C:/Users/Muhammed Hassan M/Desktop/sheikh/psd/1.psd'

count =1
for psd_image in os.listdir(IMG_DIR):
    print(psd_image)
    psdimage_path = os.path.join(IMG_DIR,psd_image)
    basename = os.path.splitext(os.path.basename(psdimage_path))[0]
    psd = PSDImage.open(psdimage_path)
    psd.compose().save('C:/Users/100119/Desktop/'+str(count)+'.png')
    count +=1

#for layer in psd:
#    print(layer)
#    image = layer.compose()