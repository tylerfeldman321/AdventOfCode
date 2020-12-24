# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:17:54 2020

@author: TylerFeldman
"""


def find_infinite_loop(target, connections, alternate_connections, lines_visited):
    if target in connections:
        new_targets = []
        for i in range(len(connections)):
            if connections[i] == target:
                new_targets.append(i)           
        for new_target in new_targets:
            ret = find_infinite_loop(new_target, connections, alternate_connections, lines_visited)
            if ret:
                return ret
    elif target in alternate_connections: # Means that this connection is connected to the end of the program when changed from nop to jmp or jmp to nop
        index = alternate_connections.index(target)
        if (lines_visited[index] == 0): # If the line was never vistited in part1, we know it won't be connected to the start, so it won't connect start to end
            return None
        print('found it!')
        return index

def run_program(lines):
    acc = 0
    index = 0
    lines_visited = [0] * len(lines)

    while (index != len(lines)):
        if (lines_visited[index] == 1):
            return "Infinite loop"
        
        command = lines[index].split(' ')[0]
        val = int(lines[index].split(' ')[1])
        lines_visited[index] = 1
        if (command == 'acc'):
            acc += val
            index += 1
            
        elif (command == 'jmp'):
            index += val
            
        elif (command == 'nop'):
            index += 1
    return acc


with open('day8_input.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]    
    
    # Part 1: Find value of accumulator before a line is run a second time
    lines_visited = [0] * len(lines)
    
    acc = 0
    index = 0
    while (lines_visited[index] != 1):
        command = lines[index].split(' ')[0]
        val = int(lines[index].split(' ')[1])
        lines_visited[index] = 1
        if (command == 'acc'):
            acc += val
            index += 1
            
        elif (command == 'jmp'):
            index += val
            
        elif (command == 'nop'):
            index += 1
            
    print('Accumulator value before a line is run a second time: ', acc)
    
    
    # Part 2: Find the value of the accumulator after changing a single line
    # from nop to jmp or jmp to nop to fix the infinite loop
    
    # Recursive method to find location of error
    connections = [None] * len(lines)
    alternate_connections = [None] * len(lines)
    for i in range(len(lines)):
        command = lines[i].split(' ')[0]
        val = int(lines[i].split(' ')[1])
        
        if command == 'nop':
            connections[i] = i + 1
            alternate_connections[i] = i + val
        elif command == 'jmp':
            connections[i] = i + val
            alternate_connections[i] = i + 1
        elif command == 'acc':
            connections[i] = i + 1  
           
    target = len(lines)
    index = find_infinite_loop(target, connections, alternate_connections, lines_visited)
    lines_copy = lines.copy()
    lines_copy[index] = lines_copy[index].replace('jmp', 'nop')
    acc_value = run_program(lines_copy)
    print('Value of accumulator:', acc_value)
    print('The error is on line:', index+1)
    
    
    # Brute force method
    for i in range(len(lines)):
        command = lines[i].split(' ')[0]
        if command == 'acc':
            continue
        lines_copy = lines.copy()
        if command == 'nop':
            lines_copy[i] = lines_copy[i].replace('nop', 'jmp')
            result = run_program(lines_copy)
        elif command == 'jmp':
            lines_copy[i] = lines_copy[i].replace('jmp', 'nop')
            result = run_program(lines_copy)
        if result != 'Infinite loop':
            print('Value of acc if the infinte loop is fixed:', result)
            print('Fix is on line:', i+1)
    
    
    
    