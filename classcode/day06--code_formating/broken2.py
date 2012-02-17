#!/usr/bin/env python

from random import randint

s = 1
input_range = int(raw_input())
rand_list = []

#create list of random numbers with user inputted length
for num in range(input_range):
    rand_list.append(randint(0,20))
print rand_list

#sort list from low to high
while s:
    s = 0
    for i in range(1,input_range):
        if rand_list[i-1] > rand_list[i]:
            t1 = rand_list[i-1]
            t2 = rand_list[i]
            rand_list[i-1] = t2
            rand_list[i] = t1
            s = 1
print rand_list
