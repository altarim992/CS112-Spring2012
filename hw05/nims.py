#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

total = int(40)
player = False
while total > 0:
	while not player:
		print total,"stones left.",
		p1 = int(raw_input("Player 1 [1-5]: "))
		if p1 > 5 or p1 < 1:
			print "Invalid number of stones."
		elif p1 > total:
			print "Not enough stones."
		else:
			total = total - p1
			if total == 0:
				print "Player 2 wins!"
				break
			else:
				player = True
	while player:
		print total,"stones left.",
		p2 = int(raw_input("Player 2 [1-5]: "))
		if p2 > 5 or p2 < 1:
			print "Invalid number of stones."
		elif p1 > total:
			print "Not enough stones."
		else:
			total = total - p2
			if total == 0:
				print "Player 1 wins!"
				break
			else:
				player = False
