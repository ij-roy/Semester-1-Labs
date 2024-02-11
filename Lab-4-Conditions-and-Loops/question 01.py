# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:03:54 2023

@author: LAB
"""
'''
1. Take a positive integer N as input and print its table as follows:
N x 1 = N
N x 2 = 2N
......
N x 20 = 20N
'''
'''
N = int(input("enter a number: "))
print(N,"x 1 = " , N*1)
print(N,"x 1 = " , N*2)
print(N,"x 1 = " , N*3)
print(N,"x 1 = " , N*4)
print(N,"x 1 = " , N*5)
print(N,"x 1 = " , N*6)
print(N,"x 1 = " , N*7)
print(N,"x 1 = " , N*8)
print(N,"x 1 = " , N*9)
print(N,"x 1 = " , N*10)
print(N,"x 1 = " , N*11)
print(N,"x 1 = " , N*12)
print(N,"x 1 = " , N*13)
print(N,"x 1 = " , N*14)
print(N,"x 1 = " , N*15)
print(N,"x 1 = " , N*16)
print(N,"x 1 = " , N*17)
print(N,"x 1 = " , N*18)
print(N,"x 1 = " , N*19)
print(N,"x 1 = " , N*20)
'''
N = int(input("enter a number"))
i = 1
while i<=20:
    print(N,"x ",i," = " , N*i)
    i=i+1
