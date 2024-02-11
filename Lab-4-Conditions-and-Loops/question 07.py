# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 00:27:50 2023

@author: AIO-ELIB-06
"""
'''
7. Display the first N terms of the Fibonacci sequence starting from 1.
1, 1, 2, 3, 5, ..... till N terms
'''
n = int(input("Enter The Value of N : "))
h = 4
print("First N terms of Fibonacci Sequence is  ")
i = 1
print(i,end=', ')
j = 1
print(j,end=', ')
while h<=n:
    k = i+j
    print(k,end=", ")
    i = j
    j = k
    h+=1
print(k)    
    
