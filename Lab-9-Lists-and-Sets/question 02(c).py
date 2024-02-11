# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:14:19 2023

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
#question 2.3

a = input("Enter integers of list 1 seperated by commas : ").split(",")
#b = input("Enter integers of list 2 seperated by commas : ").split(",")
i = [int(x) for x in a]
#j = [int(x) for x in b]
n1 = i.len()
print(n1)    

'''
l1 = [8,9,0]
print(l1.len)

list = []
#n2 = j.len()
for p in range(n1):
    for q in range(n2):
        if p==q:
            if q not in list:
                list.append(q)
print(list)        
'''