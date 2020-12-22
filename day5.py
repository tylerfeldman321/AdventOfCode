# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:05:21 2020

@author: TylerFeldman
"""

def compute_seat_id(line):
    row_info = line[:7]
    col_info = line[7:]
    row = int(row_info.replace('F', '0').replace('B', '1'), 2)
    col = int(col_info.replace('R', '1').replace('L', '0'), 2)

    return (row * 8 + col), row, col


f = open('day5_input.txt', 'r')

seat_ids = []
highest_seat_id = 0
lowest_seat_id = 100000
seat_id_sum = 0

for x in f:
    seat_id, row, col = compute_seat_id(x)
    seat_ids.append(seat_id)
    seat_id_sum += seat_id
    highest_seat_id = max(highest_seat_id, seat_id)
    lowest_seat_id = min(lowest_seat_id, seat_id)
    
    
total_seat_id_sum = 0
for i in range(lowest_seat_id, highest_seat_id+1):
    total_seat_id_sum += i    

print('Highest seat id:', highest_seat_id)
print('My seat id:', total_seat_id_sum - seat_id_sum)
