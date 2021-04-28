# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:49:59 2021

@author: TOSHIBA
"""

import easyocr
import cv2
import os
img = cv2.imread('C:/Users/TOSHIBA/Desktop/KTP_EXTRACTION/ktp_images/0903 (13)-1.jpg')
# image_path = 'C:/Users/TOSHIBA/Desktop/KTP_EXTRACTION/ktp_images/0903 (13)-1.jpg'
# 
def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()
def show_wait_destroy(winname, img):
    cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
    cv2.imshow(winname, img)
    cv2.resizeWindow(winname, 600,100)
    cv2.moveWindow(winname, 0, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)
def Easy_OCR(img):
    # Text Extraction
    reader = easyocr.Reader(['id', 'en'], gpu=False)
    result = reader.readtext(img,detail=1,paragraph=False)
    txt_list =  reader.readtext(img,detail=0,paragraph=False)
    
    # Doing OCR. Get bounding boxes.
    # bounds = reader.readtext(image_path, detail=1) #detail=1 argument will only give text with its position in an image
    # bounds
    
    # Draw bounding boxes
    # loop over the results
    for (bbox, text, prob) in result:
        # display the OCR'd text and associated probability
        print("[INFO] {:.4f}: {}".format(prob, text))
        # unpack the bounding box
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        # cleanup the text and draw the box surrounding the text along
        # with the OCR'd text itself
        text = cleanup_text(text)
        cv2.rectangle(img, tl, br, (0, 255, 0), 2)
        cv2.putText(img, text, (tl[0], tl[1] - 10), \
                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        # show the output image
    show_wait_destroy("Image", img)
    return txt_list

text = Easy_OCR(img)