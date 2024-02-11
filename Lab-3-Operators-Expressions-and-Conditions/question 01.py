# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:03:38 2023

@author: LAB
"""
'''
1. If the lengths of the two parallel sides of a trapezoid are X meters and Y meters, respectively,
and the height is H meters, what is the area of the trapezoid? Write Python code to output the
area by taking X, Y and H as input from the user.
'''

# que 1 formula of trapezoid
X = int(input('length of the 1st parallel side:'))
Y = int(input('length of the 2nd parallel side:'))
Z = int(input('height of the trapezoid:'))56
area = ((X+Y)/2)*Z 
print('area of trapezoi is :',area)
