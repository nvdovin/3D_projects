from utils import *
import numpy as np
import pygame as pg


def get_Mandelbrods_set(max_iterations=10):
    accept = got_out = []
    
    for x in x_coordinates:
        for y in y_coordinates:
            c = complex(x, y)
            z = complex(0)

            x_coord, y_coord = round((x * zoom) + x_center), round((y * zoom) + y_center)

            for iteration in range(max_iterations):
                R=G=B=0
                z = z ** 2 + c

                if abs(z) > 2:
                    if iteration == 0:
                        R = 10
                        G = 7
                        B = 12
                        # statistics.write(f"x: {x}, y: {y} Вылетел на {iteration}, цвет: {R, G, B}. Z = {z}\n")
                        
                    else:
                        R = round((iteration / max_iterations) * 100)
                        G = round((iteration / max_iterations) * 100)
                        B = round((iteration / max_iterations) * 255)
                    # statistics.write(f"x: {x}, y: {y} Вылетел на {iteration}, цвет: {R, G, B}. Z = {z}\n")
                    break
            pg.draw.circle(sc, (R, G, B), (x_coord, y_coord), 1)
                

# statistics = open("statistics.txt", "w", encoding="utf-8")

zoom, density = 290, 800
x_coordinates = np.linspace(-2.1, 1.8, density)
y_coordinates = np.linspace(-1.8, 1.8, density)

pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod`s set")

sc.fill((10, 7, 12))

get_Mandelbrods_set(25)

pg.display.update()
cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
            