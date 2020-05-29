# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:21:15 2020

@author: Muhammed Hassan M
"""

from tika import parser

file = 'C:/Users/Muhammed Hassan M/Desktop/1.pdf'
# Parse data from file
file_data = parser.from_file(file)
# Get files text content
text = file_data['content']
print(text)