from utils import *
import numpy as np
import pygame as pg


def get_Mandelbrods_set(max_iterations=10):
    accept = got_out = []
    
    for x, x_point in enumerate(x_coordinates):
        for y, y_point in enumerate(y_coordinates):
            c = x_point + y_point * 1j
            z = 0

            for iteration in range(max_iterations):
                z = z ** 2 + c

                if abs(z) > 2:
                    if iteration == 0:
                        color = 255
                    else:
                        sharpness = 255 / iteration
                        color = round(number)((max_iterations / iteration) * sharpness)

                    return x_point, y_point, color

                else:
                    color = (0, 0, 0)
                    return (x_point, y_point, color)


x_coordinates = y_coordinates = np.linspace(-2, 2, 30)

pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod`s set")

zoom = 10

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False

    sc.fill((5, 10, 7))

    x, y, color = get_Mandelbrods_set()
    x, y = x + round((x_center) * zoom), round((y + y_center) * zoom)

    pg.draw.circle(sc, (color, color, color), (x, y), 2)

    pg.display.update()