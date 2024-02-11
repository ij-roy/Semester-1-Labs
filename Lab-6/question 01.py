# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:02:07 2023

@author: LAB
"""
'''
1. Find the count of vowels and consonants, words in a string using a for loop. Assume there is a
single space between consecutive words in a sentence.
'''
# que 1 find the count of vowels and consoonants, words in a string using a for loop.assume there is a single space between consecutive words in a sentence
V = 0
i = 0
C = 0
W = 1
string = str(input())
for i in (string):
    if i=='a'or i=='e' or i=='i' or i=='o' or i=='u':
        V+=1
    elif i==' ':
        W +=1
    else:
        C+=1
print('number of constant =',C)
print('number of vowels =',V)
print('number of words =',W)
        
