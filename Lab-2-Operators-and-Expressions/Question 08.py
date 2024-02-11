# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:24:50 2023

@author: LAB
"""
'''
8. The a value of year as input and find whether it is a leap year or not. Consider all the cases of
valid and invalid inputs. Write down the test cases for the same.
'''
year = int(input("type the year: "))
leap = year%4 
if leap ==0 :
    print("this is a leap year")
else:
        print("this is not a leap year")
