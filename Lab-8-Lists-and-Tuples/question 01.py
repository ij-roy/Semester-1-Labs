# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:10:26 2023

@author: LAB
"""
'''
1. Write programs for the following by taking list of integers of arbitrary length as user input. Do 
not use any inbuilt list functions other than len().
1. Find the sum of the elements in the list.
2. Find the product of the elements in the list.
3. Find the largest element in the list of integers.
'''
lst = input('enter integers seperated by space :').split()
jjk = [int(x) for x in lst]
sum = 0
mul = 1
max = 0

for i in jjk:
    sum = i+sum
    mul = i*mul
    if i>max:
        max=i
print(f"sum of all the numbers is : {sum}")
print(f"multiplication of all the numbers is : {mul}")
print(f"largest numbers of all the numbers is : {max}")

    
   