# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:11:24 2023

@author: LAB
"""
'''
Question1. Take a list of positive integers as input in a list and perform the following operations:
1. Remove duplicate elements. Do not use sets or any other in-built functions except len().
2. Remove duplicate elements by typecasting into sets and displaying resulting elements in the
same order as they appear in the input list
'''
a = input("Enter numbers seperated by commas : ").split(",")
lst = [int(x) for x in a]
lstt = []
for ij in lst:
    if ij not in lstt:
        lstt.append(ij)
print(f"List Without Any Repeatition \n{lstt}")