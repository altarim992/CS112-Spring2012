#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1.", sum(nums)


# 2. Print every even number in nums
print "2. even numbers"

#CODE GOES HERE
even = []

for i in range(len(nums)):
	if nums[i]%2 == 0:
		even.append(nums[i])

print even
# 3. Does nums only contain even numbers? 

#CODE GOES HERE
if len(even) == len(nums):
	only_even=True
else:
	only_even=False

print "3.",
if only_even == True:
	print "only even"
else:
	print "some odd"

# 4. Generate a list every odd number less than 100. Hint: use range()
odd_num = []
for x in range(len(nums)):
	if nums[x]%2 != 0 and nums[x] < 100:
		odd_num.append(nums[x])
print "4.", odd_num

# 5. [ADVANCED]  Multiply each element in nums by its index
mult = []
for z in range(len(nums)):
	mult.append(nums[z]*z)
print "5.", mult
