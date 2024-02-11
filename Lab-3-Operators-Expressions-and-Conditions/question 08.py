# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:12:04 2023

@author: LAB
"""
'''
8. Calculate the gross salary of an employee by taking as input the basic Salary.
HRA = 20% of basic salary, TA is 5% of basic salary, and DA is 10% of basic salary.
Gross Salary = Basic Salary + HRA + TA + DA
'''
basic = float(input('type the basic salary:'))
hra = basic/5
ta = basic/20
da = basic/10
gross = basic+hra+ta+da
print('Gross salary is :',gross)
