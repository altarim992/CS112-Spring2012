#!/usr/bin/env python
import math

class Shape(object):
    def area(self):
        pass
    def perimeter(self):
        pass

class Rect(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return (self.x * self.y)
    def perimeter(self):
        return ((self.x * 2) + (self.y * 2))

class Square(Rect):
    def __init__(self, side):
        self.x = side
        self.y = side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return ((self.radius**2) * math.pi)
    def perimeter(self):
        return ((self.radius * 2) * math.pi)

r = Rect(3, 4)
print r.area()

sq = Square(5)
print sq.perimeter()

print isinstance(sq, Rect)

c = Circle(3)
print c.area()
# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
