# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:31:15 2020

@author: TylerFeldman
"""
from queue import Queue

def is_valid(preamble, value):
    for i in range(len(preamble)):
        complement = value - preamble[i]
        
        '''
        if complement in preamble:
            return True'''
        
        for j in range(len(preamble)):
            if i == j:
                continue
            if preamble[j] == complement:
                return True

with open('day9_input.txt') as f:
    nums = [int(num) for num in f.read().split('\n')[:-1]]
    
    # Part 1: Find the invalid number, in which its preamble doesn't contain two numbers that sum to it
    preamble_length = 25
    invalid_number = 0
    
    for i in range(preamble_length, len(nums)):
        value = nums[i]
        preamble = nums[i-preamble_length:i]
        if not is_valid(preamble, value):
            print('The invalid number is:', value)
            invalid_number = value
            break
    
    
    # Part 2: Find contiguous set of numbers that sum to the invalid number   
    nums = [num for num in nums if num < invalid_number] # Ignore values above the invalid number    
        
    # O(n^2) solution
    set_of_nums = None
    for i in range(len(nums)):
        s = nums[i]
        j = i + 1
        while (s < invalid_number and j < len(nums)):
            s += nums[j]
            if (s == invalid_number):
                set_of_nums = nums[i:j+1]
                break
            j += 1
    
    print('Encryption weakness:', max(set_of_nums)+min(set_of_nums))
        
    # O(n) solution
    contigious_sequence = []
    curr_sum = nums[0] # Keep track of running sum
    curr_list = Queue() # Keep track of previous values
    curr_list.put(nums[0])
    for i in range(1, len(nums)):
        curr_sum += nums[i]
        curr_list.put(nums[i])
        
        while (curr_sum > invalid_number): # If the running sum is larger than target value, subtract the earliest value that makes up the sum
            curr_sum -= curr_list.get()

        if (curr_sum == invalid_number): # Found it!
            while (not curr_list.empty()):
                contigious_sequence.append(curr_list.get())
        
    print('Encryption weakness:', max(contigious_sequence)+min(contigious_sequence))
    
            
    