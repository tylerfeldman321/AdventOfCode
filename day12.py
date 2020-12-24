# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:31:40 2020

@author: TylerFeldman
"""
import math

with open('day12_input.txt') as f:
    lines = f.read().split('\n')[:-1]

    
    # Part 1: Find Manhattan distance between start and end location after executing the commands
    position = [0, 0]
    index = 2
    d_NSWE = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    d_RL = {'R': 1, 'L': -1}
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command in 'NSWE':
            position[0] += d_NSWE[command][0]*value
            position[1] += d_NSWE[command][1]*value
        if command == 'F':
            position[0] += directions[index][0]*value
            position[1] += directions[index][1]*value
        if command in 'RL':
            value = value // 90
            index = (index + d_RL[command]*value) % 4
        
    print('Manhattan distance for part 1:', abs(position[0]) + abs( position[1]))
    
    
    # Part 2: Find Manhattan distance between start and end location after executing the commands with waypoints
    position = [0, 0]
    index = 2
    d_NSWE = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    waypoint = [10, 1]
    reverse = {90:270, 180:180, 270:90}
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command in 'NSWE':
            waypoint[0] += d_NSWE[command][0]*value
            waypoint[1] += d_NSWE[command][1]*value
        if command == 'F':
            position[0] += waypoint[0]*value
            position[1] += waypoint[1]*value
        
        if command in 'RL':
            if command == 'L':
                value = reverse[value]
                
            s = round(math.sin(math.radians(value)))
            c = round(math.cos(math.radians(value)))
            new_x = waypoint[0] * c + waypoint[1] * s
            new_y = -waypoint[0] * s + waypoint[1] * c
            waypoint[0] = new_x
            waypoint[1] = new_y
        
    print('Manhattan distance for part 2:', abs(position[0]) + abs(position[1]))