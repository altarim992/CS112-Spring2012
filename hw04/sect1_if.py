#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n%2 == 0:
	print "1.", "Even"
else:
	print "1.", "Odd"
# 2. If n is odd, double it
if n%2 != 0:
	n=n*2
	print "2.", n


# 3. If n is evenly divisible by 3, add four
n=n/2
if n%3 == 0:
	n=n+4
	print "3.", n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)
if grade <= 100 and grade >= 90:
	grade="A"
elif grade < 90 and grade >= 80:
	grade="B"
elif grade < 80 and grade >= 70:
	grade="C"
elif grade < 70 and grade >= 60:
	grade="D"
elif grade < 60:
	grade="F"
print "4.", grade

