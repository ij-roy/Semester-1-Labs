# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:34:20 2023

@author: LAB
"""
'''
10. A day has 86,400 secs (24*60*60). Given a number in the range 1 to 86,400, output the current
time as hours, minutes, and seconds with a 24-hour clock. For example: 70,000 sec is 19 hours,
26 minutes, and 40 seconds.
'''

i = int(input("type a number between 1 to 86400:"))
if i<1 or i>86400:
    print("invalid input")
else:   
     h = i//3600
     j = i%3600
     m = j//60
     s = j%60
     print(h,"hours",m,"minutes",s,"seconds")
