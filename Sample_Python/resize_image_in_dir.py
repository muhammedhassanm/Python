# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:57:52 2020

@author: Muhammed Hassan M
"""

import glob
import cv2
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import os

ROOT_DIR = 'C:/Users/Muhammed Hassan M/Desktop/dir'

for folder in os.listdir(ROOT_DIR):
    print(folder)
    count = 1
    for img in glob.glob(ROOT_DIR + "/" + folder + "/" +"*.jpg"):
     print(img)
     base_name = os.path.splitext(os.path.basename(img))[0]
     image=cv2.imread(img)
#     print(image.shape)
     image = cv2.resize(image,(600,1024),fx=2.5,fy=2.5)
     # image = cv2.resize(image,None,fxo=2.5, fy=2.5, interpolation=cv2.INTER_AREA)
     # plt.imshow(image)
     # plt.show()
     #Save Each Transformation
     if not os.path.isdir(ROOT_DIR + "/" + "RESIZED_"+folder):
         os.mkdir(ROOT_DIR + "/" + "RESIZED_"+folder)
     path = ROOT_DIR + "/" + "RESIZED_"+folder + "/" + base_name+"_"+str(count)+".jpg"
     cv2.imwrite( path,image)
#     os.rename(image,'D:/DOC_EXTRACT/train/doc_res_' +str(count)+ '.jpg')
     count=count+1