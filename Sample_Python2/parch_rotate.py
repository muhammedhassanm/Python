# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:02:32 2020

@author: Muhammed Hassan M
"""

from PIL import  Image,ImageSequence
from pdf2image import convert_from_path
from scipy.ndimage import interpolation as inter
import cv2
import numpy as np


image_path = 'C:/Users/Muhammed Hassan M/Desktop/TIF_50_Table_0.jpg'
def sharpen(img):

    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    return img

def find_score(arr, angle):
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score

def Rotate_Image(img):
    wd, ht = img.size
    pix = np.array(img.convert('1').getdata(), np.uint8)
    bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)
    angles = np.arange(-5, 6, 1)
    scores = []
    for angle in angles:
        hist, score = find_score(bin_img, angle)
        scores.append(score)

    best_score = max(scores)
    best_angle = angles[scores.index(best_score)]


    img = np.array(img.convert('RGB'))
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 0.5)
    rotated = cv2.warpAffine(img, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

image = Image.open(image_path)
#image = image.rotate(90)
#image.save("asd.jpg")
img=image
image = Rotate_Image(image)
cv2.imshow("1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
