# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:07:20 2020

@author: Muhammed Hassan M
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

file = 'C:/Users/Muhammed Hassan M/Desktop/sheikh/W2.jpg'

#im1 = cv2.imread(file, 0)
im1 = cv2.imread(file,0)

ret,thresh_value = cv2.threshold(im1,180,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)
_,contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cordinates = []
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cordinates.append((x,y,w,h))
    #bounding the images
    if y<500 or y>500 and y<1000:
        
        cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),1)
        
plt.imshow(im1)
cv2.namedWindow('detecttable', cv2.WINDOW_NORMAL)
cv2.imwrite('detecttable.jpg',im1)
