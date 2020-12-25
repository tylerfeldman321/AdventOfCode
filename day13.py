# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:49:58 2020

@author: TylerFeldman
"""

def find_earliest_bus(arrival_time, bus_values):
    time = arrival_time
    while (True):
        for bus in bus_values:
            if time % bus == 0:
                return time, bus
        time += 1

def inverse(a, n):
    # Solves the equation
    # a*t = 1 (mod n)
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    t = 0
    r = n
    newt = 1
    newr = a
    while (newr != 0):
        quotient = r // newr
        t, newt = newt, t-quotient*newt
        r, newr = newr, r-quotient*newr
        
    if (r > 1):
        return "a is not invertible"
    if (t < 0):
        t = t + n
    return t

with open('day13_input.txt', 'r') as f:
    lines = f.read().split('\n')
    
    # Part 1
    arrival_time = int(lines[0])
    bus_info = lines[1].split(',')
    bus_values = [int(bus) for bus in bus_info if bus != 'x']

    time, bus = find_earliest_bus(arrival_time, bus_values)
    print('Earliest departure time:', (time-arrival_time)*bus)
    
    
    # Part 2:
    offsets = []
    for i in range(len(bus_info)):
        if bus_info[i] != 'x':
            offsets.append(i)
    '''
    The timestamp solves the system of equations:
    time % 29 = 0
    time % 41 = 22
    time % 577 = 548
    time % 13 = 10
    time % 17 = 8
    time % 19 = 9
    time % 23 = 17
    time % 601 = 541
    time % 37 = 14
    '''
    # Can solve this through the Chinese Remainder Theorem
    a = [0, 22, 548, 10, 8, 9, 17, 541, 14] # Remainders for each equation
    m = bus_values # Divisors for each equation
    M = 1
    for mi in m: # Multiply together all of the divisors
        M *= mi
    Mi = [M // mi for mi in m] # Get a list of the product of all of the divisors, divided individually by each divisor
    y = [inverse(Mi[i], m[i]) for i in range(len(m))] # Solve the system of equations Mi*yi = 1 (mod mi)
    X = sum([a[i] * Mi[i] * y[i] for i in range(len(y))]) # Sum up each term ai*Mi*yi
    print('The timestamp is:', X % M)
    
    