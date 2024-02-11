# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:49:05 2023

@author: AIO-ELIB-06
"""
'''
7. Display the pattern using nested loops:
   *
  * *
 * * *
* * * *
(till N lines)

'''
n = int(input('enter a number n : '))
i = 1

while i<=n:
    j = n-1
    k = 1
    while j>=i:
        print(' ', end='')
        j-=1
    while k<=i:
        
        print('*',end=" ")
        k+=1
    print()
    i+=1
#ho gya bs pta ni kese 
'''
are yaar dekho
spaces me end jo tha wo 1 space ki jgah 0 space kr dia 
2i-1 ki jgah i likh dia  
aur ho gya'''