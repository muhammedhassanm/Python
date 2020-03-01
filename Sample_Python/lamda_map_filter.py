# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:33:20 2020

@author: Muhammed Hassan M
"""

#Lamda
x = lambda a, b : a * b
print(x(5, 6)) # prints '30'

x = lambda a : a*3 + 3
print(x(3)) # prints '12'
#Map
def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 4, 7])
print(list(x)) # prints '[1, 16, 49]'

def multiplier_func(a, b):
    return a * b

x = map(multiplier_func, [1, 4, 7], [2, 5, 8])
print(list(x)) # prints '[2, 20, 56]'
#Filter

# Our numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Function that filters out all numbers which are odd
def filter_odd_numbers(num):

    if num % 2 == 0:
        return True
    else:
        return False

filtered_numbers = filter(filter_odd_numbers, numbers)

print(list(filtered_numbers))
# filtered_numbers = [2, 4, 6, 8, 10, 12, 14]  

#itertools
from itertools import *

# Easy joining of two lists into a list of tuples
for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
# ('a', 1)
# ('b', 2)
# ('c', 3)

# The count() function returns an interator that 
# produces consecutive integers, forever. This 
# one is great for adding indices next to your list 
# elements for readability and convenience
for i in izip(count(1), ['Bob', 'Emily', 'Joe']):
    print i
# (1, 'Bob')
# (2, 'Emily')
# (3, 'Joe')    

# The dropwhile() function returns an iterator that returns 
# all the elements of the input which come after a certain 
# condition becomes false for the first time. 
def check_for_drop(x):
    print 'Checking: ', x
    return (x > 5)

for i in dropwhile(should_drop, [2, 4, 6, 8, 10, 12]):
    print 'Result: ', i

# Checking: 2
# Checking: 4
# Result: 6
# Result: 8
# Result: 10
# Result: 12


# The groupby() function is great for retrieving bunches
# of iterator elements which are the same or have similar 
# properties

a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
for key, value in groupby(a):
    print(key, value), end=' ')
    
# (1, [1, 1, 1])
# (2, [2, 2, 2]) 
# (3, [3, 3]) 
# (4, [4]) 
# (5, [5]) 

#Generators
# (1) Using a for loop
numbers = list()

for i in range(1000):
    numbers.append(i+1)
    
total = sum(numbers)

# (2) Using a generator
 def generate_numbers(n):
     num = 0
     while num < n:
         yield num
         num += 1
 total = sum(generate_numbers(1000))
 
 # (3) range() vs xrange()
 total = sum(range(1000 + 1))
 total = sum(xrange(1000 + 1))

