from math import *
import numpy as np


# Configurations
WIGHT  = 1700
HEIGHT = int(WIGHT * (9 / 16))
h = WIGHT / HEIGHT
col_c, row_c = WIGHT / 2, HEIGHT / 2

FPS = 60

# Camera
camera = np.array([0, 1.2, -1.5])

# Colors
black = (10, 10, 30)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)

# Rotation functions 
def rotate(axe, point, angle):
	""" в этом блоке мы вращаем точки""" 
	rotate_z = np.array([
		[cos(angle), -sin(angle), 0],
		[sin(angle), cos(angle), 0],
		[0, 0, 1]])
		
	rotate_y = np.array([
		[cos(angle), 0, sin(angle)],
		[0, 1, 0],
		[-sin(angle), 0, cos(angle)]])
		
	rotate_x = np.array([
		[1, 0, 0],
		[0, cos(angle), -sin(angle)],
		[0, sin(angle), cos(angle)]])
		
	xy = np.dot(rotate_x, rotate_y)
	xz = np.dot(rotate_x, rotate_z)
	yz = np.dot(rotate_y, rotate_z)
	xyz = np.dot(xy, yz)
		
	if axe == "x":
		return np.dot(point, rotate_x)
	elif axe == "y":
		return np.dot(point, rotate_y)
	elif axe == "z":
		return np.dot(point, rotate_z)
	elif axe == "xy":
		return np.dot(point, xy)
	elif axe == "xz":
		return np.dot(point, xz)
	elif axe == "yz":
		return np.dot(point, yz)
	elif axe == "xyz":
		return np.dot(point, xyz)
			
			
			
def get_2D_coirds(point):
	to_2D = np.array([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]])
	
	return np.dot(point, to_2D)
	

def get_distance(point):
	distance = sqrt((point[0] - camera[0]) ** 2 + (point[1] - camera[1]) ** 2 + (point[2] - camera[2]) ** 2)
	return distance * 100
