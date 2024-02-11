# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:46:51 2023

@author: LAB
"""
'''
2. Take two lists of values as integers and perform the following operations:
1. Convert the lists into sets (set A and set B). This will retain only the unique elements.
2. Find the union, intersection, set difference (A-B), symmetric set difference ( (A-B) U (B-A) )
of the two sets.
3. Find the result of the intersection operation by using the initial two input lists. Do not use
sets and inbuilt set functions.
4. Find the result of the union operation by using the initial two input lists. Do not use sets and
inbuilt set functions.
'''
#answer 2.1
a = input("Enter integers of list 1 seperated by commas : ").split(",")
b = input("Enter integers of list 2 seperated by commas : ").split(",")
j = {int(x) for x in a}
i = {int(x) for x in b}
c = i^j

print(f"List of Unique Numbers Are : \n{c}")