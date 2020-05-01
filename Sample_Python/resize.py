# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:57:35 2020

@author: 100119
"""

import glob
import cv2
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import os
count = 1
for image in glob.glob('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/RESIZED_PNG/*.png'):
     print(image)
     base_name = os.path.splitext(os.path.basename(image))[0]
     print(base_name)
     image=cv2.imread(image)
#     print(image.shape)
     image = cv2.resize(image,(600,1024),fx=2.5,fy=2.5)
     # image = cv2.resize(image,None,fxo=2.5, fy=2.5, interpolation=cv2.INTER_AREA)
     # plt.imshow(image)
     # plt.show()
     #Save Each Transformation
     cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/RESIZED_1_PNG/'+base_name+'_' +  str(count)+ '.png',image)
#     os.rename(image,'D:/DOC_EXTRACT/train/doc_res_' +str(count)+ '.jpg')
     count=count+1