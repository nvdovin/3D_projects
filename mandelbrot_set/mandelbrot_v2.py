from utils import *
import numpy as np
import pygame as pg


def get_Mandelbrods_set(max_iterations=10):
    accept = got_out = []
    
    for x in x_coordinates:
        for y in y_coordinates:
            c = complex(x, y)
            z = complex(0)

            for iteration in range(max_iterations):
                z = z ** 2 + c

                if abs(z) > 2:
                    if iteration == 0:
                        R = G = B = 0
                    else:
                        R = abs(round(max_iterations / iteration) - 100)
                        G = abs(round( max_iterations / iteration) - 70)
                        B = round(max_iterations / iteration)

                    x_coord, y_coord = round((x * zoom) + x_center), round((y * zoom) + y_center)
                    pg.draw.circle(sc, (R, G, B), (x_coord, y_coord), 1)
                    print(f"x: {x}, y: {y} Вылетел на {iteration}, цвет: {R, G, B}. Z = {z}")
                    break

                    

x_coordinates = y_coordinates = np.linspace(-2, 2, 200)

pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod`s set")

zoom = 180
sc.fill((5, 10, 7))

get_Mandelbrods_set(255)

pg.display.update()
cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
            