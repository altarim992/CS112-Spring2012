#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

length = len(nums)
for x in range(length):
    index = x
    for i in range(x + 1, length):
        if nums[i] < nums[index]:
            index = i
    nums[x], nums[index] = nums[index], nums[x]

print "After sort:"
print nums
