# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:19:44 2023

@author: AIO-ELIB-06
"""
'''
Enter the coefficients of a quadratic equation and display its solutions. Handle all the cases for invalid input and display the solutions till exactly 2 decimal places. You need not calculate the complex solutions.
'''
#a,b,c = map(int(input("Enter Integer Seperated By Commas "))
a, b, c = map(int, input("Enter Coefficients of x^2 , x^1 , x^0 respectively Seperated By Commas  ").split(","))
while a==0:
    print("coefficients of x^2 cannot be Zero")
    a, b, c = map(int, input("Enter Coefficients of x^2 , x^1 , x^0 respectively Seperated By Commas  ").split(","))
d = (b*b)-4*a*c
#print(e)
if d<0:
    print("Roots Are Imaginary")
e = pow(d,1/2)
x1 = (-b+e)/(2*a)
x2 = (-b-e)/(2*a)
if d==0:
    print("Roots Are Real And Equal ")
    print(f"Roots are {x1} , {x2} ")
if d>0:
    print("Roots Are Real And Distinct ")
    print(f"Roots Are {x1} , {x2} ")