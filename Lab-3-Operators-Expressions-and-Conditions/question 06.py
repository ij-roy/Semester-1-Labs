# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:57:02 2023

@author: LAB
"""
'''
6. Swap the values of two integer variables without using a third variable or multiple assignment
operation.
'''
a = int(input('enter the value of a:'))
b = int(input('enter the value of b:'))

a = a+b
b = a-b
a = a-b
print('new value of a is:',a)
print('new value of b is:',b)
