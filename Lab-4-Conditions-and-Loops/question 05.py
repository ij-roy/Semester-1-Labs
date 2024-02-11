# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:09:05 2023

@author: LAB
"""
'''
5. Take a positive integer N as input and find its Factorial using a while loop. Handle invalid cases as
well.
'''
n = int(input("enter a number n : "))
i = 1
f = 1
if n<0:
  print('invalid input')
elif n==0:
  print("factorial of the number is 1")
else:
  while i<=n:
      f = f*i
      i = i+1
  print("factorial of the number is",f)
