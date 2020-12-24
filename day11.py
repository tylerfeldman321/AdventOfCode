# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:15:00 2020

@author: TylerFeldman
"""
import copy

def get_new_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            seat = grid[i][j]
            if (seat == 'L'):
                if no_adj_occupied_seats(i, j, grid):
                    new_grid[i][j] = '#'
            elif (seat == '#'):
                if four_plus_adj_occupied_seats(i, j, grid):
                    new_grid[i][j] = 'L'
            else:
                new_grid[i][j] = '.'
    return new_grid

def no_adj_occupied_seats(i, j, grid):
    seats = [[i-1, j], [i+1, j], [i, j-1], [i, j+1], [i-1, j+1], [i-1, j-1], [i+1, j-1], [i+1, j+1]]
    for seat in seats:
        if in_bounds(seat[0], seat[1], grid):
            if (grid[seat[0]][seat[1]]=='#'):
                return False
    return True

def four_plus_adj_occupied_seats(i, j, grid):
    adj_occupied_seats = 0
    seats = [[i-1, j], [i+1, j], [i, j-1], [i, j+1], [i-1, j+1], [i-1, j-1], [i+1, j-1], [i+1, j+1]]
    for seat in seats:
        if in_bounds(seat[0], seat[1], grid):
            if (grid[seat[0]][seat[1]]=='#'):
                adj_occupied_seats += 1
    if (adj_occupied_seats >= 4):
        return True
    return False

    
    
def get_new_grid_visible(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            seat = grid[i][j]
            if (seat == 'L'):
                if no_visible_occupied_seats(i, j, grid):
                    new_grid[i][j] = '#'
            elif (seat == '#'):
                if five_plus_visible_occupied_seats(i, j, grid):
                    new_grid[i][j] = 'L'
            else:
                new_grid[i][j] = '.'
    return new_grid

def no_visible_occupied_seats(i, j, grid):
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]]
    for direction in directions:
        if find_visible_seat(i, j, grid, direction[0], direction[1]) == '#':
            return False
    return True


def five_plus_visible_occupied_seats(i, j, grid):
    occupied_seats = 0
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]]
    for direction in directions:
        if find_visible_seat(i, j, grid, direction[0], direction[1]) == '#':
            occupied_seats += 1
    if occupied_seats >= 5:
        return True
    return False

def find_visible_seat(i, j, grid, d_hor, d_ver):
    i += d_ver
    j += d_hor
    while (in_bounds(i, j, grid)):
        if (grid[i][j] == 'L'):
            return 'L'
        if (grid[i][j] == '#'):
            return '#'
        i += d_ver
        j += d_hor
    return None



def in_bounds(i, j, grid):
    if ((i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))):
        return True
    return False

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print('')
    
    

with open('day11_input.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')[:-1]]
    
    
    # Part 1: Find # of occupied seats after the seating arrangement stabilizes
    prev_grid = copy.deepcopy(grid)
    new_grid = get_new_grid(grid)
    
    while (new_grid != prev_grid):
        prev_grid = copy.deepcopy(new_grid)
        new_grid = get_new_grid(prev_grid)
    
    num_occupied_seats = 0
    for line in new_grid:
        num_occupied_seats += ''.join(line).count('#')
    print('Number of occupied seats after seating arangement stabilizes:', num_occupied_seats)
        

    # Part 2: Repeat, but with visible seats instead of adj seats
    prev_grid = copy.deepcopy(grid)
    new_grid = get_new_grid_visible(grid)
    
    while (new_grid != prev_grid):
        prev_grid = copy.deepcopy(new_grid)
        new_grid = get_new_grid_visible(prev_grid)
    
    num_occupied_seats = 0
    for line in new_grid:
        num_occupied_seats += ''.join(line).count('#')
    print('Number of occupied seats after seating arangement stabilizes with visible conditions:', num_occupied_seats)
    
    