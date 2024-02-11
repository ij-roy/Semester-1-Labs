# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:00:38 2023

@author: LAB
"""

e= float(input('enter the epsillon value: '))
sum = 0
f1 = 1/2
f2 = (1/2)+(1/4)
i = 3
while abs(f2-f1)>e:
    f = (1/2)**i
    f1=f2
    f2=f2+f
    i=i+1
print(f2,i-1)
