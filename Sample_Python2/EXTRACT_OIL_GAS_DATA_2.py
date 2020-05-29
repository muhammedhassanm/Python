# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:12:09 2020

@author: Muhammed Hassan M
"""


import cv2
import pytesseract
import os
import imutils
import numpy as np
import re
import json

CONFIG = '-l eng --oem 1 --psm 6' 
#CONFIG = '-l eng --oem 3 --psm 6 -c preserve_interword_spaces=0'
CCFW_DICT = dict()

COMPANY = ""
COMPANY_LIST = []
COMPANY_SUBSTRING_LIST = ["COMPANY"]

COUNTY = ""
COUNTY_LIST  =[]
COUNTY_SUBSTRING_LIST = ["COUNTY"]

FIELD = ""
FIELD_LIST =[]
FIELD_SUBSTRING_LIST =["FIELD"]

WELL =""
WELL_LIST = []
WELL_SUBSTRING_LIST = ["WELL"]

API_NO =''
API_NO_LIST =[]

FILE_NO = ''
FILE_NO_LIST = []


IMAGE_PATH = 'C:/Users/Muhammed Hassan M/Desktop/Images/TIF_35_Table_6.jpg'
image = cv2.imread(IMAGE_PATH)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imwrite('C:/Users/Muhammed Hassan M/Desktop/sdf.jpg',gray)
TEXT = pytesseract.image_to_string(gray,config=CONFIG)
TEXT = TEXT.upper()
TEXT = TEXT.replace(" L","")
TEXT = TEXT.replace("--","")
TEXT = TEXT.replace("__"," ")
TEXT = TEXT.replace(":","")
TEXT = TEXT.replace("|","")
TEXT = TEXT.replace("-","")
TEXT = TEXT.replace("4252532017","4232332917")
TEXT = TEXT.replace("4249532589","4249332589")
TEXT = TEXT.replace("4249352589","4249332589")
TEXT = TEXT.replace("4232532917","4232332917")
TEXT = TEXT.replace("1245539271","4243539271")
TEXT = TEXT.replace("212753651","4212733651")
TEXT = TEXT.replace("WOSIS0","MD8150")
TEXT_LIST = TEXT.split("\n")
if len(TEXT_LIST)!=0:
    for i in range(len(TEXT_LIST)): 
    
        if any(substring in TEXT_LIST[i] for substring in COMPANY_SUBSTRING_LIST):
#            print(TEXT_LIST[i])
            COMPANY_LIST.append(TEXT_LIST[i])
            COMPANY = COMPANY_LIST[0].split("COMPANY")
            COMPANY = COMPANY[1]+' '+'COMPANY'.strip()
            COMPANY = re.sub('[^A-Z a-z 0-9]+', '', COMPANY)
        elif COMPANY=='':
            COMPANY ="NAN"
        else:
            pass
        if any(substring in TEXT_LIST[i] for substring in COUNTY_SUBSTRING_LIST):
#            print(TEXT_LIST[i])
            COUNTY_LIST.append(TEXT_LIST[i])
            COUNTY = COUNTY_LIST[0].partition("COUNTY")
            COUNTY = COUNTY[2].strip()
            COUNTY = COUNTY.partition('STATE')[0].strip()
            COUNTY = re.sub('[^A-Z a-z 0-9]+', '', COUNTY)
        elif COUNTY=='':
            COUNTY = "NAN"
        else:
            pass
        if any(substring in TEXT_LIST[i] for substring in FIELD_SUBSTRING_LIST):
#            print(TEXT_LIST[i])
            FIELD_LIST.append(TEXT_LIST[i])
            FIELD = FIELD_LIST[0].partition("FIELD")
            FIELD = FIELD[2].strip()
            FIELD = re.sub('[^A-Z a-z 0-9]+', '', FIELD)
        elif FIELD=='':
            FIELD = "NAN"
        else:
            pass
        if any(substring in TEXT_LIST[i] for substring in WELL_SUBSTRING_LIST):
            print(TEXT_LIST[i])
            WELL_LIST.append(TEXT_LIST[i])
            WELL = WELL_LIST[0].partition("WELL")
            WELL = WELL[2].strip()
            WELL = re.sub('[^A-Z a-z 0-9]+', '', WELL)
            
        elif WELL== '':
            WELL = "NAN"
        else:
            pass
        if any(substring in TEXT_LIST[i] for substring in COUNTY_SUBSTRING_LIST):
            print(TEXT_LIST[i])
            API_NO_LIST.append(TEXT_LIST[i])
            API_NO = API_NO_LIST[0].partition("COUNTY")
            API_NO = API_NO[0]
            API_NO = re.sub('[^0-9]*$', '', API_NO)
        elif API_NO=='':
            API_NO = "NAN"
        else:
            pass
        if any(substring in TEXT_LIST[i] for substring in WELL_SUBSTRING_LIST):
            print(TEXT_LIST[i])
            FILE_NO_LIST.append(TEXT_LIST[i])
            FILE_NO = FILE_NO_LIST[0].partition("WELL")
            FILE_NO = FILE_NO[0]
            FILE_NO = re.sub('[^A-Z a-z 0-9]+', '', FILE_NO)
#            FILE_NO = FILE_NO.replace("S","5")
        elif FILE_NO=='':
            FILE_NO = "NAN"
        else:
            pass
CCFW_DICT.update({'FILE NO':FILE_NO,'API_NO':API_NO,'Company':COMPANY,'County':COUNTY,'Field':FIELD,'Well':WELL})
_json = json.dumps(CCFW_DICT)
print(_json) 
        
            



