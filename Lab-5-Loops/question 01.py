# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:03:45 2023

@author: LAB
"""
'''
1. Take a positive integer N between 1 – 20 and display the tables of all the numbers from 1 to N as
follows:
1 x 1 = 1
......
1 x 20 = 20
2 x 1 = 2
.......
N x 20 = 20N
'''
n = int(input('enter a number between 1 to 20: '))
i = 1
j = 1
while j<=n:
    i=1
    while i<=20:
        print(j,'x',i,'=',j*i )
        i+=1
        if i==21:
            break
        
    j+=1
