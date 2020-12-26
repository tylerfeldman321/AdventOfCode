# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:20:32 2020

@author: TylerFeldman
"""

def to_36bit_binary(val, string=''):
    return bin(val).replace('0b', '').zfill(36)

def apply_mask_to_value(mask, binary):
    new_binary = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            new_binary += mask[i]
        else:
            new_binary += binary[i]
    return int(new_binary, 2)

def apply_mask_to_mem_address(mask, address):
    new_address = ''
    for i in range(len(mask)):
        if mask[i] == '0':
            new_address += address[i]
        else:
            new_address += mask[i]
    return new_address

def find_possible_mem_addresses(mem_address, possible_addresses=[], count=1):
    X_count = mem_address.count('X')
    if not X_count:
        return int(mem_address, 2)
    else:
        possible_addresses.append(find_possible_mem_addresses(mem_address.replace('X', '0', 1), possible_addresses, count+1))
        possible_addresses.append(find_possible_mem_addresses(mem_address.replace('X', '1', 1), possible_addresses, count+1))
    
    if possible_addresses and count == 1:
        return [address for address in possible_addresses if address]



with open('day14_input.txt') as f:
    
    groups =[line.split('\n')[:-1] for line in f.read().split('mask =')][1:]
    
    # Part 1
    mem = {}
    masks = [group[0].replace(' ', '') for group in groups]
    assignments = [group[1:] for group in groups]
    
    for i in range(len(masks)):
        for assignment in assignments[i]:
            mem_address = int(assignment.split('[')[1].split(']')[0])
            val = int(assignment.split(' ')[-1])
            binary = to_36bit_binary(val)
            decimal = apply_mask_to_value(masks[i], binary)
            mem[mem_address] = decimal
                
    print('Sum of values stored in memory:', sum(mem.values()))
    
    # Part 2
    mem = {}
    for i in range(len(masks)):
        for assignment in assignments[i]:
            mem_address = assignment.split('[')[1].split(']')[0]
            val = int(assignment.split(' ')[-1])
            new_address = apply_mask_to_mem_address(masks[i], to_36bit_binary(int(mem_address)))
            addresses = find_possible_mem_addresses(new_address, [])
            for address in addresses:
                mem[address] = val
                
    print('Sum of values stored in memory:', sum(mem.values()))