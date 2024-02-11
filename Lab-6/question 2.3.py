# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:01:56 2023

@author: LAB
"""
n = int(input('enter the number:'))
a = 0
b = 1
c = 0
for i in range(n):
    for j in range(i):
        a=a+(1/b)
        b+=1
    c=c+a
print(f'{c:.9f}')