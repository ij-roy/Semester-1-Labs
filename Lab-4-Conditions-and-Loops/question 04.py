# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:55:45 2023

@author: LAB
"""
'''
4. Take a positive integer N as input followed by repeatedly taking numbers from the user till the
time user entered -999. At the end display the count of input numbers that are divisible by N
and the count of input numbers that are not divisible by N.
'''
n = int(input("enter a number N : "))
s = 0
t = 0
c=0
v=0
while t != -999:
    t = int(input())
    if t%n==0:
        c = c+1
    else:
        v = v+1
    s = t+s
#print("sum of all numers till now is",s+999) 
print("numbers divided by N are :",c)
print("numbers not divided by N are :",v)
    
