# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:40:37 2023

@author: LAB
"""
'''
5. Take a 5 digit number as input and print the reverse of the number. Do not use any in-built
functions for reversing. Check whether the input number and the reversed number are the
same. If so, print “Number is Palindrome”, else print “Number is not Palindrome”.
'''
m = int(input('type a 5 digit number'))
q =m%10
w =m//10
e =w%10
r =w//10
t =r%10
y =r//10
u =y%10
i =y//10
o =i%10
z = q*10000
x = e*1000
c = t*100
v = u*10
b = o
k = z+x+c+v+b
print(k)

if m==k:
    print('number is palindrome')
else:
        print('number is not palindrome')
'''    
print(q,e,t,u,o)
print(q)
print(w)
print(e)
print(r)
print(t)
print(y)
print(u)
print(i)
print(o)
'''
