# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 12:25:16 2020

@author: Muhammed Hassan M
"""

def isConvertible(str1, str2, k): 
    
    # Case A (i) 
    if ((len(str1) + len(str2)) < k): 
        return True

    # finding common length of both string 
    commonLength = 0
    for i in range(0, min(len(str1), 
                        len(str2)), 1): 
        if (str1[i] == str2[i]): 
            print(str1[i])
            print(str2[i])
            commonLength +=1
        else: 
            break

    # Case A (ii)- 
    if ((k - len(str1) - len(str2) + 2 *
                commonLength) % 2 == 0): 
        return True

    # Case B- 
    return False

# Driver Code 
if __name__ == '__main__': 
    str1 = "has1sannnnnnnnnnnnnnnnnnnnnnn"
    str2 = "hassa"
    k = 20
    if (isConvertible(str1, str2, k)): 
        print("Yes") 
    else: 
        print("No") 


