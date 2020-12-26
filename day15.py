# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:38:25 2020

@author: TylerFeldman
"""

starting_numbers = [20,9,11,0,1,2] 
d = {}

# Part 1
for i in range(len(starting_numbers)):
    d[starting_numbers[i]] = i
new_num = starting_numbers[-1]
first = True
prev_index = 0

for i in range(len(starting_numbers), 2020):
    if first:
        new_num = 0
    else:
        new_num = i-1-prev_index
    if new_num in d.keys():
        prev_index = d[new_num]
        first = False
    else:
        first = True
    d[new_num] = i

print('2020th turn:', new_num)


# Part 2. O(n) solution since adding/chaning entries in d is O(1),
# and looking if values are present in d.keys() is O(1)
d = {}
for i in range(len(starting_numbers)):
    d[starting_numbers[i]] = i
new_num = starting_numbers[-1]
first = True
prev_index = 0

for i in range(len(starting_numbers), 30000000):
    if first:
        new_num = 0
    else:
        new_num = i-1-prev_index
    if new_num in d.keys():
        prev_index = d[new_num]
        first = False
    else:
        first = True
    d[new_num] = i
    
print('30000000th turn', new_num)