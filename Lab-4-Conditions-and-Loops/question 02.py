# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:16:57 2023

@author: LAB
"""
'''
2. Take 2 numbers as input (X and Y) and a third number N. Display all the numbers between X and
Y (X < i <= Y) that are divisible by N.
'''
x = int(input("enter 1st number "))
y = int(input("enter 2st number "))
n = int(input("enter  the  number N: "))
i = x+1
while(x<i and i<=y):
    
    if  i%n==0:
        print(i)
    i=i+1    


 
