# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:48:26 2020

@author: TylerFeldman
"""

def is_valid(minimum, maximum, c, password):
    counts = password.count(c)
    if (counts >= minimum and counts <= maximum):
        return True
    else:
        return False
    
def is_valid_2(minimum, maximum, c, password):
    
    if ((password[minimum-1]==c) ^ (password[maximum-1]==c)):
        return True
    else:
        return False


f = open("day2_input.txt", "r")

valid_passwords = 0

for x in f:
    c = x.split(":")[0][-1]
    minimum = int(x.split(":")[0].split(" ")[0].split("-")[0])
    maximum = int(x.split(":")[0].split(" ")[0].split("-")[1])
    password = x.split(":")[1].replace(" ", "")
    valid = is_valid_2(minimum, maximum, c, password)
    if valid:
        valid_passwords +=1 
    print(minimum, maximum, c, password, valid)
    
print(valid_passwords)

    
f.close()