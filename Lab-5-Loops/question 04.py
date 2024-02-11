# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:16:44 2023

@author: AIO-ELIB-06
"""
'''
4. Take a positive integer N as input followed by repeatedly taking numbers from the user till the
time user entered -999. At the end display the count of input numbers that are divisible by N
and the count of input numbers that are not divisible by N.
'''
k = 0
a = 0
b = 0
n = int(input("Enter 1st integer n : "))
while k!=-999:
    k = int(input("Just enter numbers repeatedly [type -999 to stop] : "))
    if k%n ==0:
        a+=1
    else:
        b+=1
        
print(f"Count of numbers entered that are divisible by n are {a}")
print(f"Count of numbers entered that are not divisible by n are {b-1}")    
     