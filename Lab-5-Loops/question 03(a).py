# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:19:35 2023

@author: LAB
"""
'''
3. Display the following patterns for N lines (value of N taken from the user) using while loop:
a)
*
* *
* * *
* * * *
(till N lines)
b)
      *
    * *
  * * *
* * * *
(till N lines)
c)
   *
  ***
 *****
*******
(till N lines)
'''
n = int(input('enter a number n :'))
i = 1
while i<=n:
    j = 1
    while j<=i:
        print('*', end=' ')
        j+=1
    print()
    i+=1
