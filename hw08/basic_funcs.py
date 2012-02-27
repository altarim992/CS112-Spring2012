#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
	print "hello,", name.lower()



#box(int(raw_input("Width: ")), int(raw_input("Height: ")))
#greeter(raw_input("Enter your name: "))
# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
	horizontal = "+" + "-" * (w - 2) + "+"
	vertical = "|" + " " * (w - 2) + "|"
	if type(w) == 'str' or type(h) == 'str':
		print "Error: Invalid Dimensions"
	elif w <= 0 or h <= 0:
		print "Error: Invalid Dimensions"
	else:
		if w == 1:
			horizontal = "+"
			vertical = "|"
		print horizontal
		h = h - 1
		while h > 1:
			print vertical
			h = h - 1
			if h == 1:
				print horizontal
				break



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()
