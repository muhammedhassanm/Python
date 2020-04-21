# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:11:45 2020

@author: 100119
"""
import os
from psd_tools import PSDImage
from PIL import Image

IMG_DIR ='C:/Users/100119/Desktop/FIR_DATA_EXTRACTION_HDFC_ERGO/set2_30_5/5/5-3'

count =1
for psd_image in os.listdir(IMG_DIR):
    print(psd_image)
    psdimage_path = os.path.join(IMG_DIR,psd_image)
    basename = os.path.splitext(os.path.basename(psdimage_path))[0]
    psd = PSDImage.open(psdimage_path)
    psd.compose().save('C:/Users/100119/Desktop/FIR_DATA_EXTRACTION_HDFC_ERGO/set2_30_5/5/5-3_png/psd_set2_5_5-3_'+str(count)+'.png')
    count +=1

#for layer in psd:
#    print(layer)
#    image = layer.compose()