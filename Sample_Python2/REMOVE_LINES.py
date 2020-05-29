# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:38:29 2020

@author: Muhammed Hassan M
"""

import cv2
import numpy as np
import pytesseract
img = cv2.imread('C:/Users/Muhammed Hassan M/Desktop/Images/TIF_101_Table_2 (2).jpg')
config = r' --psm 6'
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# edges = cv2.Canny(img,100,110)
#
# masked_data = cv2.bitwise_and(img, img, mask=edges)
kernel = np.ones((2,2),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(img,kernel,iterations = 0)
# inpain = cv2.inpaint(img,masked_data,10,cv2.INPAINT_NS)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# erosion = cv2.erode(img,kernel,iterations = 1)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#
# cv2.imwrite('closing.png',opening)
cv2.imwrite('output.png',dilation)
text =  pytesseract.image_to_string(dilation, config=config)
print(text)
# =============================================================================
# img = cv2.bitwise_not(img)
# th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
# cv2.imshow("th2", th2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("th2.jpg", th2)
# 
# horizontal = th2
# vertical = th2
# rows,cols = horizontal.shape
# horizontalsize = int(cols / 30)
# horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,1))
# horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
# horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))
# cv2.imshow("horizontal", horizontal)
# cv2.imwrite("horizontal.jpg", horizontal)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# verticalsize = int(rows / 30)
# verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
# vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
# vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))
# cv2.imshow("vertical", vertical)
# cv2.imwrite("vertical.jpg", vertical)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# vertical = cv2.bitwise_not(vertical)
# cv2.imshow("vertical_bitwise_not", vertical)
# cv2.imwrite("vertical_bitwise_not.jpg", vertical)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# #step1
# edges = cv2.adaptiveThreshold(vertical,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,-2)
# cv2.imshow("edges", edges)
# cv2.imwrite("edges.jpg", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# #step2
# kernel = np.ones((2, 2), dtype = "uint8")
# dilated = cv2.dilate(edges, kernel)
# cv2.imshow("dilated", dilated)
# cv2.imwrite("dilated.jpg", dilated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# # step3
# smooth = vertical.copy()
# 
# #step 4
# smooth = cv2.blur(smooth, (4,4))
# cv2.imshow("smooth", smooth)
# cv2.imwrite("smooth.jpg", smooth)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# #step 5
# (rows, cols) = np.where(img == 0)
# vertical[rows, cols] = smooth[rows, cols]
# 
# cv2.imshow("vertical_final", vertical)
# cv2.imwrite("vertical_final.jpg", vertical)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================
