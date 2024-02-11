# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:04:16 2023

@author: AIO-ELIB-06
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
n = int(input('enter a number n : '))
i = 1

while i<=n:
    j = n-1
    k = 1
    while j>=i:
        print(' ', end=' ')
        j-=1
    while k<=(2*i)-1:
        print('*',end=" ")
        k+=1
    print()
    i+=1
#loop 2 will run for 2n-1 times 
#spaces part is same