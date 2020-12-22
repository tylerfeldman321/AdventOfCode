# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:06:11 2020

@author: TylerFeldman
"""

f = open("day3_input.txt", "r")

grid = []
for x in f:
    grid.append(x.replace('\n', ''))

'''
for row in range(total_rows):
    if grid[row][column % total_columns] == '#':
        tree_count += 1   
    column += 3'''

def num_trees(d_row, d_column, grid):
    total_rows = len(grid)
    total_columns = len(grid[0])
    row = 0
    column = 0
    tree_count = 0
    while (row < total_rows):
        if grid[row][column % total_columns] == '#':
            tree_count += 1
        column += d_column
        row += d_row
    return tree_count

print(num_trees(1, 1, grid)* num_trees(1, 3, grid)* num_trees(1, 5, grid)* num_trees(1, 7, grid)* num_trees(2, 1, grid))
    
f.close()