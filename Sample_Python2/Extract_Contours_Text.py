# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:58:55 2020

@author: Muhammed Hassan M
"""


import cv2
import pytesseract
import numpy as np

image = cv2.imread('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/TIF_103/Table_12.tif',0)

thresh,img_bin = cv2.threshold(image,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img_bin = 255-img_bin
kernel_len = np.array(image).shape[1]//100
# Defining a vertical kernel to detect all vertical lines of image 
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
# Defining a horizontal kernel to detect all horizontal lines of image
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
# A kernel of 2x2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

#Use vertical kernel to detect and save the vertical lines in a jpg
image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)

image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
#cv2.imshow("image",vertical_lines)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
#Eroding and thesholding the image
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite("C:/Users/Muhammed Hassan M/Desktop/img_vh.jpg", img_vh)
bitxor = cv2.bitwise_xor(image,img_vh)
bitnot = cv2.bitwise_not(bitxor)
cv2.imshow("image",bitnot)
cv2.waitKey(0)
cv2.destroyAllWindows()

#finalimg = bitnot[x:x+h, y:y+w]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
border = cv2.copyMakeBorder(bitnot,2,2,2,2, cv2.BORDER_CONSTANT,value=[255,255])
resizing = cv2.resize(border,None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
dilation = cv2.dilate(resizing, kernel,iterations=1)
erosion = cv2.erode(dilation, kernel,iterations=2)
cv2.imshow("image",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
text = pytesseract.image_to_string(erosion)
