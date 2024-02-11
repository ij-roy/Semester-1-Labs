# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:17:48 2023

@author: LAB
"""
'''
6. Take a positive integer as input. It may be of any length. Check if it is palindrome or not. Do not
use any inbuilt reverse functions.
'''
n = int(input("enter a number n : "))
v=0

i = n
s = 0 
while i !=0:
     q = i%10
     v = q+(v*10)
     print(q,v)
     i //=10
if v==n:
    print("number is palindrome")
else:
    print("number is not palindrome")
     
