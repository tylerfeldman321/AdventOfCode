# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:00:16 2020

@author: TylerFeldman
"""

# Part 1
f = open('day6_input.txt', 'r')

sum_of_counts = 0
current_group_answers = ''
for x in f:
    if x == '\n':
        sum_of_counts += len(set(current_group_answers))
        current_group_answers = ''
    else:
        current_group_answers += x.replace('\n', '')
sum_of_counts += len(set(current_group_answers))

print('Part 1:', sum_of_counts)

f.close()


# Part 2
def intersection(list1, list2):
    inter = [value for value in list1 if value in list2]
    ret = ''
    return ret.join(inter)

#print(intersection('ab', 'abbc'))
sum_of_counts = 0
f = open('day6_input.txt', 'r')

groups = f.read().split('\n\n')
for group in groups:
    people = group.split('\n')
    answers = people[0]
    for i in range(1, len(people)):
        answers = intersection(answers, people[i])
    sum_of_counts += len(answers)

print('Part 2:', sum_of_counts)

f.close()

