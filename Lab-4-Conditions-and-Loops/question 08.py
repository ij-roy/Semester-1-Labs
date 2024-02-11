# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:18:14 2023

@author: AIO-ELIB-06
"""
'''
Take an integer as input and check if it is prime or not. Handle invalid conditions and make your code efficient by minimizing the number of loop iterations.
'''
n = int(input("Enter A number : "))
while n<2:
    print("Invalid Number")
    n = int(input("Entar A valid Number :"))
i = 2
while i<=(n/2):
    if i ==(n/2) or i ==(n/2)-(1/2):
        print("Given Number Is A Prime Number")
        break
    if n%i==0:
        print(("Given number is not a prime number"))
        break
    ##if i ==(n):
      #  print("Given Number Is A Prime Number")
    i+=1

#if i == (n/2):
 #   print("It is a prime number")

            