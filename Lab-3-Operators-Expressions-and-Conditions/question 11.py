# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:35:42 2023

@author: LAB
"""
'''
11. Take a 3 digit number as input. Check if it is an Armstrong number or not. E.g. 13 + 53 + 33 = 153
'''
a = int(input('type three digit number:'))
q=a%10
w=a//10
e=w%10
r=w//10
t=r%10
x=(q*q*q)+(e*e*e)+(t*t*t)
'''
print(q)
print(w)
print(e)
print(r)
print(t)
print(x)
'''
if x==a:
    print('it is an armstrong number')
else:
    print('it is not an armstrong number')
