# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:31:41 2020

@author: TylerFeldman
"""


def is_valid_1(entry):
    keys = [key_value.split(':')[0] for key_value in entry.split(' ')][:-1]
    if (('byr' in keys) and ('iyr' in keys) and ('eyr' in keys) and ('hgt' in keys) and ('hcl' in keys) and ('ecl' in keys) and ('pid' in keys)):
        return True
    return False

def is_valid_2(entry):
    pairs = [key_value.split(':') for key_value in entry.split(' ')][:-1]
    keys = [pair[0] for pair in pairs]
    values = [pair[1] for pair in pairs]
    
    if (('byr' not in keys) or ('iyr' not in keys) or ('eyr' not in keys) or ('hgt' not in keys) or ('hcl' not in keys) or ('ecl' not in keys) or ('pid' not in keys)):
        return False
    
    for i in range(len(keys)):
        if (keys[i] == 'byr'):
            if not valid_yr(values[i], 1920, 2002):
                return False
        if (keys[i] == 'iyr'):
            if not valid_yr(values[i], 2010, 2020):
                return False
        if (keys[i] == 'eyr'):
            if not valid_yr(values[i], 2020, 2030):
                return False
        if (keys[i] == 'hgt'):
            if not valid_hgt(values[i]):
                return False
        if (keys[i] == 'hcl'):
            if not valid_hcl(values[i]):
                return False
        if (keys[i] == 'ecl'):
            if not valid_ecl(values[i]):
                return False
        if (keys[i] == 'pid'):
            if not valid_pid(values[i]):
                return False
    return True

def valid_pid(value):
    if len(value) != 9:
        return False
    for digit in value:
        if digit not in '0123456789':
            return False
    return True
    
def valid_ecl(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def valid_hcl(value):
    if value[0] != '#':
        return False
    for character in value[1:]:
        if character not in "0123456789abcdef":
            return False
    if len(value[1:]) != 6:
        return False

    return True

def valid_hgt(value):
    if len(value) < 3:
        return False
    
    units = value[-2:]
    value = int(value[:-2])
    
    if units == 'cm':
        return (value >= 150 and value<= 193)
    elif units == 'in':
        return (value >= 59 and value <=76)
    return False

def valid_yr(value, minimum, maximum):
    value = int(value)
    return (value >= minimum and value <= maximum)


f = open('day4_input.txt', 'r')

valid_count = 0

current_entry = ''
line = f.readline()
while line != '':
    if (line == '\n'):
        valid_count += is_valid_2(current_entry)
        current_entry = ''
    else:
        current_entry += line.replace('\n', ' ')
    line = f.readline()
valid_count += is_valid_2(current_entry)

print(valid_count)

f.close()