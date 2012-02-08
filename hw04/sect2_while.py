#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num=raw_input("Enter a number: ")
num=int(num)

while num%3 != 0:
	num=raw_input("Try again: ")
	num=int(num)
else:
	print "1.", num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num
#CODE GOES HERE
while num > 0:
	print "    ",num,"..."
	num=num-1
if num == 0:
	print "    ",num


# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.
num = int(raw_input("3. Countdown from: "))
while num > 0 and num%3 == 0:
	print "    ",num,"..."
	num=num-3
while num > 0:
	if num%3 != 0 and num%2 == 0:
		print "    ",num,"..."
		num=num-2
		if num%2 == 0:
			print "    ",num,"..."
			num=num-2
	else:
		print "    ",num,"..."
		num=num-1
if num == 0:
	print "    ",num
