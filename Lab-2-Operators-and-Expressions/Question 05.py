# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:16:31 2023

@author: LAB
"""
'''
5. Find the area of a Circle of radius r. Only radius between 1 and 100 should be accepted.
'''

r = int(input("radius of circle is: "))
if 0<r<100:
    area = 22/7*r*r
    print("the area of circle is :", area)

    
else:
    print("invalid input")
