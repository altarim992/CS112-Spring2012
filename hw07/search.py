#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums = input_nums()
nums = sorted(nums)
print "I have sorted your numbers"
print nums

search = int(raw_input("Which number should I find: "))
lo = 0
hi = len(nums) - 1

while hi >= lo:
    mid = (hi + lo)/2
    if nums[mid] < search:
        lo = mid + 1
    elif nums[mid] > search:
        hi = mid - 1
    else:
        print "Found", search, "at", mid
        break

else:
    print "Could not find", search
