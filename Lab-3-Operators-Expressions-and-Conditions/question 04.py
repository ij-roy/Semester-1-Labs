# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:25:53 2023

@author: LAB
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 00:27:50 2023

@author: AIO-ELIB-06
"""
'''
4. Take a 3 digit number as input and find the sum of its digits. Also, check if the sum is divisible by
3 or not.
'''
a = int(input('type 3 digit number:'))
while a <100 or a>999:
    print("'Error : Enter a 3 digit Number")
    a = int(input('type 3 digit number:'))
    
q = a%10
w = a//10
e = w%10
r = w//10
t = r%10
i = q+e+t
print(f"Sum of its digits are {i} ")
if i%3 ==0:
    print("Number is divisible by 3")
else:
    print(("Number is Not divisible by 3"))
#print(q)
#print(w)
#print(e)
#print(r)
#print(t)
