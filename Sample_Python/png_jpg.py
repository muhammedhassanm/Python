# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:27:17 2020

@author: 100119
"""
import os
from PIL import Image
IMG_DIR ='C:/Users/100119/Desktop/FIR_DATA_EXTRACTION_HDFC_ERGO/set2_30_5/5/5-3_png/'
count = 1
for image in os.listdir(IMG_DIR):

    image_path = os.path.join(IMG_DIR,image)
    basename = os.path.splitext(os.path.basename(image_path))[0]
    im = Image.open(image_path)
    rgb_im = im.convert('RGB')
    rgb_im.save('C:/Users/100119/Desktop/FIR_DATA_EXTRACTION_HDFC_ERGO/set2_30_5/5/5-3_jpg/'+basename+'.jpg')
    count+=1