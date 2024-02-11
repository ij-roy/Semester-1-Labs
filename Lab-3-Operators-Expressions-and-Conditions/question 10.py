# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:26:39 2023

@author: LAB
"""
'''
10. Find the largest of 3 numbers using nested if else condition.
'''
a = float(input('enter 1st number:'))
b = float(input('enter 2nd number:'))
c = float(input('enter 3rd number:'))
print('largest number is')
if a>b:
    if a>c:
        print(a)
    else:
       print(c)
else:
    if b>c:
        print(c)
    else:
        print(b)
            
    
