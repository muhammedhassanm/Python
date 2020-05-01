# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:41:44 2020

@author: Muhammed Hassan M
"""

import cv2
import glob
count=1
for tif_path in glob.glob('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/TIF/*.tif'):
    print(tif_path)
    im = cv2.imread(tif_path,1)
    im = cv2.resize(im,(600,1024),fx=2.5,fy=2.5)
    cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/RESIZED_PNG/Well_Log_'+str(count)+'.png',im)
    count+=1
#im = cv2.imread('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/s_0fa7b4aa381f4331652edfe4363013a8.tif',1)
#cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/JPG/Well_Log_103'+str(count)+'.jpg',im)