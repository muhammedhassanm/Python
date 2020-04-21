# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:21:30 2020

@author: 100119
"""


import os
import cv2
import numpy as np

image_path ='C:/Users/100119/Desktop/PRUDENTIAL/dataset/data/3.jpg'
basename = os.path.splitext(os.path.basename(image_path))[0]
image  = cv2.imread(image_path)
cv2.imshow("sd",image)
cv2.waitKey(0)
# gray_img =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# im = cv2.filter2D(gray_img, -1, kernel)
image1 =cv2.resize(image,None,fx=2,fy=2)
cv2.imshow("sdf",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('C:/Users/100119/Desktop/PRUDENTIAL/dataset/2/preprocessed_2/'+basename+'.jpg',image1)
