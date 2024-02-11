# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:44:54 2023

@author: LAB
"""
'''
3. Take a list of integers as input and sort the elements of the list in-place, i.e., do not use any
other list for storing the result, only the values in the list are swapped to form the sorted list.
(Do not use the inbuilt sorting function). 
'''
lst = input('enter integers seperated by space :').split()
jjk = [int(x) for x in lst]
n = len(jjk)
for i in range(n):
    for j in range(0,n-i-1):
        if jjk[j]>jjk[j+1]:
            x=0
            x=jjk[j]
            jjk[j]=jjk[j+1]
            jjk[j+1]=x
            
print(jjk)