# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:48:52 2020

@author: Muhammed Hassan M
"""

import pyrebase
import requests
import os
import pandas as pd
os.chdir("C:/Users/Muhammed Hassan M/Desktop/Document_field_detection")
MUZZLE_BLUR_THRESHOLD = 100
KEYPOITS_THRESHOLD = 1000

config = {
  "apiKey": "AIzaSyAWL50crLrOyEQjof0l5jMAiBWSA6vfaxY",
  "authDomain": "techvantage-docscanner.firebaseio.com",
  "databaseURL": "https://techvantage-docscanner.firebaseio.com",
  "storageBucket": "techvantage-docscanner.appspot.com",
  "serviceAccount": "C:/Users/Muhammed Hassan M/Desktop/Document_field_detection/techvantage-docscanner-firebase-adminsdk-6p89h-10199ec8b0.json"
}
firebase = pyrebase.initialize_app(config)
Storage = firebase.storage()


import numpy as np
from urllib.request import urlopen
import cv2
import datetime
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

#def Get_Cattle_Muzzle_Match(RF_ID):
#try:
#    os.mkdir(str(RF_ID))
#except:
#    pass
#try:
#    os.mkdir(str(RF_ID)+"/policy")
#
#except:
#    pass
#try:
#    os.mkdir(str(RF_ID)+"/claim")
#except:
#    pass
Files = Storage.bucket.list_blobs(prefix='user/techvantagetechies@gmail.com/Documents/')#+'policy')
#    Files = Storage.bucket.list_blobs(prefix='user/icicilombard.mobile@gmail.com/'+str(RF_ID)+'/')
for file in Files:
 print(file)
    if (file.name.find('cropped')== -1):
         image = url_to_image(file.generate_signed_url(datetime.datetime.now()+datetime.timedelta(1)))
         file_name = (file.name.split('/')[-1]).split(RF_ID)[0][:-1]
         if(file.name.find('policy')>=0):
             file_name = str(RF_ID)+'/policy/'+file_name
         else:
             file_name = str(RF_ID)+'/claim/'+file_name
         print(file_name)
         cv2.imwrite(file_name + str(RF_ID) +'.png',image)
#             if(((file.name).split('/')[-1]).lower().find('muzzle')>=0):
#                cv2.imshow(file_name, cv2.resize(image,(650,650)))
#                cv2.waitKey(0)
#                cv2.destroyAllWindows()

DATA = pd.read_excel('C:/Users/SHEIK/Downloads/Require muzzle matching status (1).xlsx')

for index,data in DATA.iterrows():
    Get_Cattle_Muzzle_Match(str(data['Tag number']))

#for RF_ID in ['990000003098224']:
#   Get_Cattle_Muzzle_Match(str(RF_ID))
##
#RF_IDS = ['990000001572464','990000003095240','990000003095721']
#for RF_ID in RF_IDS:
#    Get_Cattle_Muzzle_Match(str(RF_ID))
#
#Get_Cattle_Muzzle_Match(str(990000002936388))


#RF_ID = '990000002636501'
