#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""
import pygame
from pygame.locals import *
from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    in_rect = True
    xlist = []
    ylist = []
    for x, y in poly:
        xlist.append(x)
        ylist.append(y)
    for xval in xlist:
        if xval < rect[0]:
            in_rect = False
        elif xval > (rect[2] + rect[0]):
            in_rect = False
    for yval in ylist:
        if yval < rect[1]:
            in_rect = False
        elif yval > (rect[3] + rect[1]):
            in_rect = False
    if in_rect == False:
        return False
    else:
        return True


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly): #"create a rectangle which surounds a polygon"       
    xlist = []
    ylist = []
    for x, y in poly:
        xlist.append(x)
        ylist.append(y)
    topx = min(xlist)
    topy = min(ylist)
    width = max(xlist) - min(xlist)
    height = max(ylist) - min(ylist)
    return pygame.Rect(topx, topy, width, height)

