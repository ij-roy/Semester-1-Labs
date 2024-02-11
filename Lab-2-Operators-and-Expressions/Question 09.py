# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:20:49 2023

@author: AIO-ELIB-06
"""
'''
9. You are designing a software for a bank. The bank calculates interest on their RD accounts at
7.1% p.a. You need to develop the functionality, where the user can check their returns for a
given duration and for a given monthly installment amount. Note that the bank does not allow
monthly installment less than Rs. 500/- and the duration of RD should be atleast 6 months.
Check for valid and invalid inputs.
'''
P = int(input("enter the principal amount: "))
while P<500:
    print("Error: Principal amount should not be less than 500")
    P = int(input("enter the principal amount: "))
    
n = int(input("enter time in months: "))
while n<6:
    print("Error: Time should Not Be Less Than 6 Months")
    t = int(input("enter time in months: "))
r = 7.1
I = P*(r/100)*n*(n+1)/24
A = (P*n)+I
print(f"Amount After {n} months will be {A}")
