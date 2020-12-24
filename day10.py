# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:40:44 2020

@author: TylerFeldman
"""

with open('day10_input.txt', 'r') as f:
    adapters = [int(num) for num in f.read().split('\n')[:-1]]
    sorted_adapters = adapters.copy()
    sorted_adapters.sort()
    sorted_adapters.insert(0, 0)
    sorted_adapters.append(max(adapters)+3)
    
    diffs = [0] * (len(sorted_adapters) - 1)
    
    # Part 1: Count the number of 3- and 1-jolt differences
    one_jolt = 0
    three_jolt = 0
    for i in range(1, len(sorted_adapters)):
        diff = sorted_adapters[i] - sorted_adapters[i-1]
        diffs[i-1]=diff
        if (diff == 1):
            one_jolt += 1
        
        if (diff == 3):
            three_jolt += 1
        
    print('Number of one jolt differences times number of three jolt differences:', one_jolt * three_jolt)
    

    # Part 2: Find total number of distinct ways you can arrange the adapters to connect the charging outlet to your device
    
    # The three differences do not matter (since they cannot be replaced by anything).
    # So, we can just look at the ones differences, which can be replaced by 2 or 3 differences
    # For each sequence of ones differences, there are a number of permutations that are in d
    # The sequence of ones only range from '1' to '1111'
    string = ''.join([str(diff) for diff in diffs])
    middle_ones = [s.replace('3', '') for s in string.split('13')]
    
    d = {'': 1,
         '1': 2,
         '11': 4,
         '111': 7}
    
    running_mult = 1
    for sequence in middle_ones:
        running_mult *= d[sequence]
    
    print('Distinct ways you can arrange the adapters to connect the charging outlet:', running_mult)

    
    