# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:02:40 2021

@author: kevmm
"""

a = (input("Enter your numbers here:(Must use comma's to seperate your numbers!) "))
c = a.split(",")
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

if  "," in a:
    d = a.index(",")
    print(d)
    print(c[0+1:len(a)])
    
    for x in range(len(a)):
        print(a[x])
    