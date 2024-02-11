# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:31:44 2023

@author: LAB
"""

n = int(input('enter the number N : '))
a = 0
b = 1
for i in range(n):
    a = a+(1/b)
print(f'{a:.9f}')
        