# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:12:02 2021

@author: 100119
"""

import cv2
import numpy as np
input_image = 'D:/Hassan/kyc_retrain/kyc_04-02-2020_model_kyc-detection/resized_images/final_data/added_data_paper/train/00000_new_2.jpg'
image = cv2.imread(input_image)
(height, width) = image.shape[:2]
def create_blank(width, height, rgb_color=(0, 0,0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

# Create new blank 300x300 red image
w, h = width+100, height+100

red = (255, 0, 0)
blank_image = create_blank(w, h, rgb_color=red)


x_offset = int((w - image.shape[1])/2)
y_offset = int((h - image.shape[0])/2)

blank_image[ y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image
new_image = blank_image
#new_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2RGB)

cv2.imwrite('new.jpg', new_image)