import pygame as pg
from utils import *
import numpy as np
from math import *


class Sphere:
	def __init__(self, r=10):
		self.r = r

		self.ring_coordinates = []
		self.sphere_coordinates = []
		self.adapted_coordinates = []
		self.rotated_coordinates = []
		self.distanced_coordinates = []
		
		self.point = np.array([1, 0, 0])
		
	def get_rings_coordinates(self, axe="y"):
		a = 0
		while a < pi:
			self.ring_coordinates.append(rotate(axe, self.point, a)) 		# Y axe for get normal ring
			a += 0.2
	
	def get_spheres_coordinates(self, axe="x", b=0):
		self.sphere_coordinates.clear()
		
		for p in self.ring_coordinates:
			a = 0
			while a < tau:
				self.sphere_coordinates.append(rotate(axe, p, a+b))
				a += 0.2

	def get_rotated_sphere(self, axe, angle):
		self.rotated_coordinates.clear()
		
		for p in self.sphere_coordinates:
			self.rotated_coordinates.append(rotate(axe, p, angle))

	def get_distance_to_camera(self, threfore=0):
			self.distanced_coordinates.clear()

			for p in self.rotated_coordinates:
				distance = get_distance(p)
				print(distance)
				if distance > threfore:
					self.distanced_coordinates.append(p)

	def get_adapted_coordinates(self):
		self.adapted_coordinates.clear()
		
		for p in self.distanced_coordinates:
			x, y, z = p[0], p[1], p[2]
			
			self.adapted_coordinates.append([
			round(x * 100 * h * self.r + col_c),
			round(y * 100 * h * self.r + row_c)])
			
		return self.adapted_coordinates

# Pygame initializing
pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
clock = pg.time.Clock()

s = Sphere(2)
s.get_rings_coordinates()

alpha = 0
cycle = True
while cycle:
	clock.tick(FPS)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			cycle = False

	# x yz - Mebius's lent

	sc.fill(black)
	s.get_spheres_coordinates("x", alpha)			# X axe for get normal sphere
	s.get_rotated_sphere("xyz", alpha+0.3)
	s.get_distance_to_camera()
	point = s.get_adapted_coordinates()
	
	for p in point:
		pg.draw.circle(sc, white, (p[0], p[1]), 4)
	
	alpha += 0.01
	pg.display.update()
	