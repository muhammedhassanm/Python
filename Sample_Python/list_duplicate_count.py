# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:59:04 2020

@author: Muhammed Hassan M
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter
lis = [1,1,2,3,3,3,4,5,5]

def getDuplicatesWithCount(lis):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in lis:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems
# Get a dictionary containing duplicate elements in list and their frequency count
dictOfElems = getDuplicatesWithCount(lis)     
 
for key, value in dictOfElems.items():
        print(key , ' :: ', value)
