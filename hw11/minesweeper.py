#!/usr/bin/env python

import pygame
from pygame import *

GRAY = 80, 80, 80
RED = 255, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
RECT_SIZE = RECT_WIDTH, RECT_HEIGHT = 80, 60
MINE_GRID = [[0,0,0,0,0,0,0,0,1],
             [0,0,0,0,1,0,0,0,0],
             [0,0,1,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,0],
             [0,1,0,0,0,0,0,1,0]]

pts = []
x = 0
y = 0
for i in range(10):
    row_list = [(x, y)]
    for j in range(10):
        x += RECT_WIDTH
        row_list.append((x, y))
    pts.append(row_list)
    x = 0
    y += RECT_HEIGHT

rects = []
for row in range(10):
    for pt in range(10):
        rects.append(pygame.Rect(pts[row][pt], RECT_SIZE))

def check_mines(x, y):
    x = (x/80) - 1
    y = (y/60) - 1
    mines = dict()
    values = [MINE_GRID[y-1][x-1],
              MINE_GRID[y-1][x],
              MINE_GRID[y-1][x+1],
              MINE_GRID[y][x-1],
              MINE_GRID[y][x+1],
              MINE_GRID[y+1][x-1],
              MINE_GRID[y+1][x],
              MINE_GRID[y+1][x+1]]
    total = []
    if y == 0:
        if x == 0:
            total.append(values[4],
                         values[6],
                         values[7])
        else:
            total.append(values[3:])
    elif y == 60:
        if x == 80:
            total.append(values[0],
                         values[1],
                         values[3])
        else:
            total.append(values[:6])
    elif MINE_GRID[y][x] == 1:
        mines = "BOOM!"
        return mines
    for num in total:
        if num not in mines:
            mines[num] = 1
        else:
            mines[num] += 1
    if 1 not in mines:
        mines = None
        return mines
    print mines
    return mines[1]

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
bounds = screen.get_rect()
numfont = pygame.font.Font(None, 80)
done = False
clicked = []

while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    clicked.append(rect)
               
    screen.fill(WHITE)
    
    for rect in rects:
        pygame.draw.rect(screen, GRAY, rect)
        pygame.draw.rect(screen, BLACK, rect, 5)

    for box in clicked:
        clicked_x = box.left
        clicked_y = box.top
        print clicked_x, clicked_y
        mines = check_mines(clicked_x, clicked_y)
        if mines != None:
            if mines == 1:
                color = BLUE
            elif mines == 2:
                color = GREEN
            elif mines == 3:
                color = RED
            else:
                color = RED
            num = str(mines)
            text = numfont.render(num, True, color)
            loc = text.get_rect()
            loc.center = box.center
            screen.blit(text, loc)
        else:
            pygame.draw.rect(screen, WHITE, box)

    pygame.display.flip()
    clock.tick(FPS)

