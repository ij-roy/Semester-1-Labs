# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:10:35 2023

@author: LAB
"""
'''
2. Body mass index (BMI) is a number calculated from a person’s weight and height. According to
the Centers for Disease Control and Prevention, the BMI is a fairly reliable indicator of body fat
for most people. BMI does not measure body fat directly, but research has shown that BMI
correlates to direct measures of body fat, such as underwater weighing and dual-energy X-ray
absorptiometry. The formula for BMI is weight/height2 where weight is in kilograms and height
is in meters.
1. Write a program that prompts for metric weight and height and outputs the BMI.
2. Write a program that prompts for weight in pounds and height in inches, converts the
values to metric, and then calculates the BMI.
'''
print('units is in kilogram and metres')
w = float(input('write the weight:'))
h = float(input('write the height'))
bmi = w/h/h
print('the bmi is ',bmi) 



print('units is in pounds and inches')
w = float(input('write the weight:'))
h = float(input('write the height'))
e = w*0.453592
j = h*0.0254
bmi = e/j/j
print('the bmi is ',bmi) 
