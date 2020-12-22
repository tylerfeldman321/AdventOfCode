# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 02:51:48 2020

@author: TylerFeldman
"""

f = open("day1_input.txt", "r")
values = []
for x in f:
    values.append(int(x))



for value in values:
    complement = 2020 - value
    if complement in values:
        print(value, complement, value*complement)



for value1 in values:
    for value2 in values:
        complement = 2020 - value1 - value2
        if complement in values:
            print(value1, value2, complement, value1*value2*complement)
        

