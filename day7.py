# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:55:49 2020

@author: TylerFeldman
"""
from queue import Queue

with open('day7_input.txt') as f:
    
    bags_that_contain_shinygold = []
    
    lines = f.read().split('\n')
    bags = []
    contains = []
    quantities = []
    for line in lines:
        if line == '':
            break
        
        bags.append(''.join(line.split(' ')[:2]))
        bag_contains = []
        bag_quantities = []
        for bag in line.split('contain')[1].split(','):
            bag_contains.append(''.join(bag.split(' ')[-3:-1]))
            bag_quantities.append(int(bag.split(' ')[1].replace('no', '0')))
            
        contains.append(bag_contains)
        quantities.append(bag_quantities)
        
    
    # Part 1: Find how many different colored bags can contain our shinygold bag
    seen = []
    q = Queue()
    q.put('shinygold')
    while (not q.empty()):
        cur = q.get_nowait()
        for i in range(len(bags)):
            if bags[i] not in seen and cur in contains[i]:
                q.put(bags[i])
                seen.append(bags[i])
                
    print('Bags that can contain shinygold:', len(seen))
    
    
    # Part 2: Find how many individual bags are inside the single shiny gold bag  
    bag_count = 0
    q = Queue()
    q.put(['shinygold', 1])
    while (not q.empty()):
        cur_bag = q.get_nowait()
        if (cur_bag[0] == 'noother'):
            continue
        index = bags.index(cur_bag[0])
        cur_contains = contains[index]
        cur_quantities = quantities[index]
        for i in range(len(cur_contains)):
            new_bag_quantity = cur_quantities[i]*cur_bag[1]
            q.put([cur_contains[i], new_bag_quantity])
            bag_count += new_bag_quantity
            
    print('My shiny gold bag must contain {} bags'.format(bag_count))
        
    
        
