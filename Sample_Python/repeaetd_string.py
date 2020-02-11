# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 13:40:29 2020

@author: Muhammed Hassan M
"""

# Complete the repeatedString function below.
def repeatedString(s, n):
    n_per_string = s.count('a')
    n_per_substring = s[0:n%len(s)].count('a')
    return int(n_per_string * (n/len(s)) + n_per_substring)
 
if __name__ == '__main__':

    s = "aba"
    n = 10
    result = repeatedString(s, n)