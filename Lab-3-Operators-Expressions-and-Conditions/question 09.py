# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:16:36 2023

@author: LAB
"""
'''
9. Further, in the above question, find the income tax slab in which the employee lies.
Gross Salary Income Tax
< Rs. 3 LPA 0%
Rs. 3,00,000 – Rs. 10,00,000 10% of the gross salary
Rs. 10,00,000 – Rs. 25,00,000 20% of the gross salary
Above Rs. 25,00,000 30% of the gross salary
'''
basic = float(input('type the basic salary:'))
hra = basic/5
ta = basic/20
da = basic/10
gross = basic+hra+ta+da
#print('gross salary is :',gross)
if gross<300000:
    print('no income tax for you')
elif gross>=300000 and gross<1000000:
    print('income tax is 10%', gross/10)
elif gross>=1000000 and gross<2500000:
    print('income tax is 20%', gross*2/10)
else:
    print('income tax is 30%', gross*3/10)

    
