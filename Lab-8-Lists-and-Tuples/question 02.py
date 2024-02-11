# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:27:17 2023

@author: LAB
"""
'''
2. Take a list of integers as input and sort the elements of the list by taking another list and
incrementally appending values in the 2nd list. (Do not use the inbuilt sorting function).
'''
lst = input('enter integers seperated by space :').split()
jjk = [int(x) for x in lst]
ijk=[]
while len(jjk)!=0:
    t = min(jjk)
    ijk.append(t)
    del jjk[jjk.index(t)]
   # jjk.remove(t)
print(ijk)