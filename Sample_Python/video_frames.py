# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:47:47 2020

@author: 100119
"""


import cv2
vidcap = cv2.VideoCapture('C:/Users/100119/Pictures/AKARSH ZF/SOCKS_DATA/drive-download-20201219T094324Z-001/1_ (9).mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite('C:/Users/100119/Pictures/AKARSH ZF/SOCKS_DATA/VIDEO_FRAMES/image_'+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
#count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)