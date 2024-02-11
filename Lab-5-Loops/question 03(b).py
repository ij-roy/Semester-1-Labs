# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:06:37 2023

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
    while k<=i:
        print('*',end=" ")
        k+=1
    print()
    i+=1
# solution is sum of this pattern plus
#bus isme * ki jgah k  space lgaya h
''' n = int(input('enter a number n :'))
i = 1
while i<=n:
    j = n
    while j>=i:
        print('*', end=' ')
        j-=1
    print()
    i+=1
'''
#this Pattern  
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
'''    