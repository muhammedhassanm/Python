# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:34:28 2020

@author: Muhammed Hassan M
"""


import os
#import tempfile
from pdf2image import convert_from_path

PDF_DIR = 'C:/Users/Muhammed Hassan M/Desktop/HDFC_ERGO/DATASET/Fir (37)_FIR (35)_FIR (33)_FIR (30)'
for pdf in os.listdir(PDF_DIR):

    filename = os.path.join(PDF_DIR,pdf)
    print(filename)
    pages = convert_from_path(filename, 300,thread_count=3)
    base_filename  =  os.path.splitext(os.path.basename(filename))[0]
    save_dir ='C:/Users/Muhammed Hassan M/Desktop/HDFC_ERGO/DATASET/IMAGES'
    count = 1
    if not os.path.isdir(save_dir+'/'+base_filename):
        os.mkdir(save_dir+'/'+base_filename)
        
    for page in pages:
        page.save(save_dir + '/' +base_filename+'/'+ base_filename + '_'+ str(count) + '.jpg')
        count += 1