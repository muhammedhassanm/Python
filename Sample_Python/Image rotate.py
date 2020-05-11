# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:59:16 2020

@author: Vivekanandan | Techvantage
"""

import warnings
import numpy as np
from PIL import Image
from scipy.ndimage import interpolation as inter

warnings.filterwarnings("ignore")

def find_score(arr, angle):
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score

def Rotate_Image(img):
    img1=img.crop((0,0,200,400))
    wd, ht = img1.size
    pix = np.array(img1.convert('1').getdata(), np.uint8)
    bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)

    angles = np.arange(0, 360, 90)
    scores = []
    for angle in angles:
        hist, score = find_score(bin_img, angle)
        scores.append(score)

    best_score = max(scores)
    best_angle = angles[scores.index(best_score)]

    rotated=img.rotate(best_angle, expand=True)
   
    return rotated

img = Image.open('C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/CONTOURS_DETECTED TIF/TIF_59/TIF_59_Table_4.jpg')
image = Rotate_Image(img)
image.save('C:/Users/Muhammed Hassan M/Desktop/kaka.jpg')
