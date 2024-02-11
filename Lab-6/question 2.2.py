# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:56:57 2023

@author: LAB
"""

n = int(input('enter a number:'))
x = int(input('enter a constant number:'))
a = 0
c = 1
b= 1
for i in range(n-1):
    a = a+(((x**c)/b))
    c+=1
    b+=1
a+=1
print(f'{a:..9f}')
    