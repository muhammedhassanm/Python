# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:07:22 2020

@author: Muhammed Hassan M
"""



import os
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image
IMAGE_PATH ='C:/Users/Muhammed Hassan M/Desktop/Images/TIF_35_Table_6.jpg'                  
basename = os.path.splitext(os.path.basename(IMAGE_PATH))[0]
config = r'--psm 6'
#page_str = pytesseract.image_to_string(Image.open(IMAGE_PATH), lang="eng", config='--psm 6')
image = cv2.imread(IMAGE_PATH) 

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Apply dilation and erosion to remove some noise
image = cv2.resize(image,None,fx=2.5,fy=2.5)

retval, thresh_gray = cv2.threshold(image,thresh= 200, maxval=255,type=cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)

cv2.bitwise_not(thresh_gray,thresh_gray)
kernel = np.ones((3,3), np.uint8)
image = cv2.dilate(thresh_gray, kernel, iterations=1)
image = cv2.erode(image, kernel, iterations=1)
image = cv2.adaptiveThreshold(cv2.bilateralFilter(image,9,75,75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
image = cv2.GaussianBlur(image,(999,999),1)
#image = cv2.resize(image,None,fx=1.5,fy=1 .5)

cv2.imshow("1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("C:/Users/Muhammed Hassan M/Desktop/Images/PREPROCESSED/1.jpg",image)

  # Detect contours for following box detection
_,contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#def sort_contours(cnts, method="left-to-right"):
#    # initialize the reverse flag and sort index
#    reverse = False
#    i = 0
#    # handle if we need to sort in reverse
#    if method == "right-to-left" or method == "bottom-to-top":
#        reverse = True
#    # handle if we are sorting against the y-coordinate rather than
#    # the x-coordinate of the bounding box
#    if method == "top-to-bottom" or method == "bottom-to-top":
#        i = 1
#    # construct the list of bounding boxes and sort them from top to
#    # bottom
#    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
#    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
#    key=lambda b:b[1][i], reverse=reverse))
#    # return the list of sorted contours and bounding boxes
#    return (cnts, boundingBoxes)
#
## Sort all the contours by top to bottom.
#contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")
#
##Create list box to store all boxes in  
#box = []
## Get position (x,y), width and height for every contour and show the contour on image
#count =1
#for c in contours:
#    x, y, w, h = cv2.boundingRect(c)
#    area = cv2.contourArea(c)
#    archlength= (cv2.arcLength(c,closed=True))
##    if (w<500 and h<500):
#    if area >5000    :
#        
#        image = cv2.rectangle(image,(x,y),(x+w,y+h),(0, 255, 0),2)
#        cv2.drawContours(image,c, -1, (0, 255, 0), 3)
##        cv2.imwrite(str(count)+".jpg",image)
#        text =  pytesseract.image_to_string(image[y:y+h, x:x+w], config=config)
#        print(text)
#        cv2.imshow("1",image[y:y+h, x:x+w] )
#        cv2.waitKey(0)
#        count+=1
#        box.append([x,y,w,h])
        
#cv2.destroyAllWindows( )
#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text =  pytesseract.image_to_string(image, config=config )
print(text)




#==========================================================
#import re
#osd= pytesseract.image_to_osd(image1)
#osd.split("\n")
#angle = re.search('(?<=Rotate: )\d+', osd).group()
#script = re.search('(?<=Script: )\d+', osd).group()
#print("angle: ", angle)
#print("script: ", script)


  
#rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
#d = pytesseract.image_to_data(rgb, output_type=Output.DICT)
#print(d.keys())
#n_boxes = len(d['text'])
#for i in range(n_boxes):
#    if int(d['conf'][i]) > 90:
#        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#        img = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#cv2.imshow('img', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()