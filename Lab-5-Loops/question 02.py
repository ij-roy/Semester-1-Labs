# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:12:27 2023

@author: LAB
"""

''' 
take a positive integer N as input and display all the numbers that are not divisible by N and lie 
in the range 1 - 1000 . use continue statement with while loop.
'''
n= int(input('enter a number n: '))
i = 1
while i<=1000:
    if i%n ==0:
        print(i)
    i+=1
