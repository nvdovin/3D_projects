import pygame as pg
from utils import *
import numpy as np
from math import *


class Sphere:
	def __init__(self, r=10):
		self.r = r
		self.ring = []
		self.sphere = []
		self.adapted = []
		self.rotate = []
		
		self.point = np.array([1, 0, 0])
		
	def get_rings(self, axe="y"):
		a = 0
		while a < pi:
			self.ring.append(rotate(axe, self.point, a)) 		# Y axe for get normal ring
			a += 0.2
	
	def get_sphere(self, axe="x", b=0):
		self.sphere.clear()
		
		for p in self.ring:
			a = 0
			while a < tau:
				self.sphere.append(rotate(axe, p, a+b))
				a += 0.2
	
	def rotate_sphere(self, axe, angle):
		self.rotate.clear()
		
		for p in self.sphere:
			self.rotate.append(rotate(axe, p, angle))
	
	def get_adapted(self):
		self.adapted.clear()
		for p in self.rotate:
			x, y, z = p[0], p[1], p[2]
			
			self.adapted.append([
			round(x *10 * h * self.r + col_c),
			round(y * 10 * h * self.r + row_c)])
			
		return self.adapted

# Pygame initializing
pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
clock = pg.time.Clock()

s = Sphere()
s.get_rings()

alpha = 0
cycle = True
while cycle:
	clock.tick(FPS)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			cycle = False

	# x yz - Mebius's lent

	sc.fill(black)
	s.get_sphere("x", alpha)			# X axe for get normal sphere
	s.rotate_sphere("xyz", alpha+0.3)
	point = s.get_adapted()
	
	for p in point:
		pg.draw.circle(sc, white, (p[0], p[1]), 4)
		# pg.draw.circle(sc, green, (p[0], p[1]-25), 4)
		# pg.draw.circle(sc, red, (p[0], p[1]+25), 4)
	
	alpha += 0.01
	pg.display.update()
	