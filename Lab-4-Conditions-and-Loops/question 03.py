# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:30:54 2023

@author: LAB
"""
'''
3. Take a positive integer as input and display the sum of its digits. The number can be of any
length.
'''
'''
n = int(input("enter a positive integer"))
i = n
j= 0
while i!=0:
    m = n%10
    n = n//10
    j = j+m
    i = i-1
print(j)       
 '''
n = int(input("enter a number : "))
i = n
s = 0 
while i !=0:
     q = i%10
     s += q
     i //=10
print("sum is ", s)     
