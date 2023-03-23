from utils import *
import numpy as np
import pygame as pg
import time


def get_Mandelbrods_set(max_iterations=10):
    accept = got_out = []
    
    for x in x_coordinates:
        for y in y_coordinates:
            c = x + y * 1j
            z = 0

            for iteration in range(max_iterations):
                z = z ** 2 + c

                if abs(z) > 2:
                    if iteration == 0:
                        color = 255
                    else:
                        sharpness = 255 / max_iterations
                        color = round((max_iterations / iteration) * sharpness)

                    x_coord, y_coord = round((x * zoom) + x_center), round((y * zoom) + y_center)
                    pg.draw.circle(sc, (color, color, color), (x_coord, y_coord), 2)
                    print(f"x: {x}, y: {y} Вылетел на {iteration}, цвет: {color}")
                    break
                else:
                    color = 0

                    x_coord, y_coord = round((x * zoom) + x_center), round((y * zoom) + y_center)
                    print(f"x: {x}, y: {y} Удовлетворяет, цвет: {color}")
                    pg.draw.circle(sc, (color, color, color), (x_coord, y_coord), 2)
                    break

                    

x_coordinates = y_coordinates = np.linspace(-2, 2, 30)

pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod`s set")

zoom = 50

sc.fill((5, 10, 7))

get_Mandelbrods_set()

pg.display.update()
cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
            