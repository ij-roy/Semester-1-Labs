# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:19:22 2023

@author: LAB
"""
'''
6. Take a value of temperature as input (in Celsius) and convert into degree Fahrenheit. Also,
display the equivalent temperature in Kelvin.
'''

celsius = int(input("type the degree in celcius:"))
fahrenheit = celsius*9/5+32
print("the temp in fahrenheit is :", fahrenheit)
kelvin = celsius+273.15
print("the temp in kelvin is :", kelvin)
