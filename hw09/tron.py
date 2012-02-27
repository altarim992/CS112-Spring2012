#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *

RED = 255,0,0
BLUE = 0,0,255
p1_x, p1_y = 200, 300
p1_dx, p1_dy = 1, 0
p2_x, p2_y = 600, 300
p2_dx, p2_dy = -1, 0
player1 = []
player2 = []

def draw_player1(surf, pos, color, size=5, width=5):
	x, y = pos
	draw.rect(surf, color, (x, y, width, size))

def draw_player2(surf, pos, color, size=5, width=5):
	x, y = pos
	draw.rect(surf, color, (x, y, width, size))

def move(x, y, dx, dy, bounds):
	x += dx
	y += dy
	return x, y, dx, dy

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
screen_bounds = screen.get_rect()
done = False
start = False
while not done:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		elif event.type == KEYDOWN and event.type == K_ESCAPE:
			done = True
		elif event.type == KEYDOWN and event.key == K_SPACE:
			start = True
	while start:
		p1_x, p1_y, p1_dx, p1_dy = move(p1_x, p1_y, p1_dx, p1_dy, screen_bounds)
		p2_x, p2_y, p2_dx, p2_dy = move(p2_x, p2_y, p2_dx, p2_dy, screen_bounds)
		if [p1_x, p1_y] in player1 or [p1_x, p1_y] in player2:
			start = False
		elif [p2_x, p2_y] in player1 or [p2_x, p2_y] in player2:
			start = False
		elif p1_x == screen_bounds.left or p1_x == screen_bounds.right:
			start = False
		elif p1_y == screen_bounds.top or p1_y == screen_bounds.bottom:
			start = False
		elif p2_x == screen_bounds.left or p2_x == screen_bounds.right:
			start = False
		elif p2_y == screen_bounds.top or p2_y == screen_bounds.bottom:
			start = False
		else:
			player1.append([p1_x, p1_y])
			player2.append([p2_x, p2_y])
		for i in range(len(player1)):
			draw_player1(screen, player1[i], RED)
		for n in range(len(player2)):
			draw_player2(screen, player2[n], BLUE)
		pygame.display.flip()
		clock.tick(500)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_w:
					p1_dx, p1_dy = 0, -1
				elif event.key == K_a:
					p1_dx, p1_dy = -1, 0
				elif event.key == K_s:
					p1_dx, p1_dy = 0, 1
				elif event.key == K_d:
					p1_dx, p1_dy = 1, 0
				elif event.key == K_UP:
					p2_dx, p2_dy = 0, -1
				elif event.key == K_LEFT:
					p2_dx, p2_dy = -1, 0
				elif event.key == K_DOWN:
					p2_dx, p2_dy = 0, 1
				elif event.key == K_RIGHT:
					p2_dx, p2_dy = 1, 0
