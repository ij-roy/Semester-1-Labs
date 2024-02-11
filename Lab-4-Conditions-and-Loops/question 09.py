# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:48:38 2023

@author: AIO-ELIB-06
"""
'''
Take a sentence as input and using while loop count of capital letters, small letters, digits, and special characters in the sentence. Do not use any inbuilt function.
'''
put = input("Enter A String Or Type Something : ")
a = 0
b = 0
c = 0
d = 0
i = 0
e = 0
length = len(put)
while i<length:
    if put[i].isupper():
        a+=1
    elif put[i].islower():
        b+=1
    elif put[i].isnumeric():
        c+=1
    elif put[i]==" ":
        e +=1
    else:
        d+=1
    i+=1
print(f"Above String Has {a} capital letters , {b} small letters ,{c} numbers , {d} Special characters and {e} spaces")        
        
    
    