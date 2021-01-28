# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:31:36 2021

@author: 100119
"""

# test file if you want to quickly try tesseract on a license plate image
import pytesseract
import cv2
import os
import re
import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# point to license plate image (works well with custom crop function)
os.chdir('C:/Users/100119/Desktop/KTP_EXtraction')
gray = cv2.imread("dataset/1.jpg", 0)
h,w=gray.shape[:2]
gray = cv2.resize( gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(gray, (5,5), 0)
gray = cv2.medianBlur(gray, 3)
# perform otsu thresh (using binary inverse since opencv contours work better with white text)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


n_white_pix = np.sum(thresh ==255)
n_black_pix = np.sum(thresh==0)
print('Number of white pixels:', n_white_pix)
print('Number of black pixels:', n_black_pix)
if n_black_pix>n_white_pix:
    cv2.bitwise_not(thresh,thresh)
elif n_black_pix<n_white_pix:
#    pass
    cv2.bitwise_not(thresh,thresh)
else:
    pass
    
 #TP= w * h
#white= cv2.countNonZero(gray[1])
#print("Dimensions:", gray.size, "Total pixels:", TP, "White", white)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# apply dilation 
dilation = cv2.dilate(thresh, rect_kern, iterations =  1)
cv2.imshow("dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows() 
# find contours
try:
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
except:
    ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

# create copy of image
im2 = gray.copy()

plate_num = ""
# loop through contours and find letters in license plate
#for cnt in sorted_contours:
#    x,y,w,h = cv2.boundingRect(cnt)
#    height, width = im2.shape
#    
#    # if height of box is not a quarter of total height then skip
#    if height / float(h) > 6: continue
#    ratio = h / float(w)
#    # if height to width ratio is less than 1.5 skip
#    if ratio < 1.5: continue
#    area = h * w
#    # if width is not more than 25 pixels skip
#    if width / float(w) > 15: continue
#    # if area is less than 100 pixels skip
#    if area < 100: continue
#    # draw the rectangle
#    rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
#    roi = thresh[y-5:y+h+5, x-5:x+w+5]
#    roi = cv2.bitwise_not(roi)
#    roi = cv2.medianBlur(roi, 5)
    #cv2.imshow("ROI", roi)
#    #cv2.waitKey(0)
text = pytesseract.image_to_string(dilation, lang='ind',config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
#print(text)
plate_num += text
plate_num = plate_num.split('\n')  
plate_num=re.sub('[^A-Z0-9]+', ' ', plate_num[0])
print(plate_num)
#cv2.imshow("Character's Segmented", im2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#def preprocess(imgOriginal):
#    image=cv2.imread(imgOriginal)
#    imgGrayscale = extractValue(image) # We get the gray scale of the image.
#    #imgGrayscale = cv2.equalizeHist(imgGrayscale)
#    imgMaxContrastGrayscale = maximizeContrast(imgGrayscale) # contrast is the difference between light and dark in an image. High contrast images will have bright highlights and dark shadows,bold colours, and show texture in the subject. Low contrast images will have a narrow range of tones and might therefore feel flat or dull
#    height,width = imgGrayscale.shape
#    imgBlurred = np.zeros((height, width, 1), np.uint8)
#
#    imgBlurred = cv2.GaussianBlur(imgMaxContrastGrayscale, GAUSSIAN_SMOOTH_FILTER_SIZE, 0) # 2nd parameter is (height,width) of Gaussian kernel,3rd parameter is sigmaX,4th parameter is sigmaY(as not specified it is made same as sigmaX).
#    
#    imgThresh = cv2.adaptiveThreshold(imgBlurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)
#    
#    return imgGrayscale, imgThresh
#
#
####################################################################################################
#def extractValue(imgOriginal):
#    height, width, numChannels = imgOriginal.shape
#
#    imgHSV = np.zeros((height, width, 3), np.uint8)
#
#    imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)
#
#    imgHue, imgSaturation, imgValue = cv2.split(imgHSV)
#    cv2.imshow("f:",imgValue)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    return imgValue
#
#def maximizeContrast(imgGrayscale):
# 
#    height, width = imgGrayscale.shape
#
#    imgTopHat = np.zeros((height, width, 1), np.uint8)
#    imgBlackHat = np.zeros((height, width, 1), np.uint8)
#
#    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) # Same as np.ones((3,3)
#
#    imgTopHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_TOPHAT, structuringElement) # It is difference of  input image and Opening of the image
#    imgBlackHat = cv2.morphologyEx(imgGrayscale, cv2.MORPH_BLACKHAT, structuringElement) # it is difference of closing of the input image and input image.
#
#    imgGrayscalePlusTopHat = cv2.add(imgGrayscale, imgTopHat)
#    imgGrayscalePlusTopHatMinusBlackHat = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)
#    cv2.imshow("f:",imgGrayscalePlusTopHatMinusBlackHat)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    return imgGrayscalePlusTopHatMinusBlackHat
