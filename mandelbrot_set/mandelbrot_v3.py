from utils import *
import pygame as pg
import numpy as np
from math import *


def get_Mandelbrots_array(max_iterations=10):
    for x_point, x in enumerate(x_coordinates):
        for y_point, y in enumerate(y_coordinates):
            c = complex(x, y)
            z = complex(0)

            for iteration in range(max_iterations):
                z = z ** 2 + c
                color = 0

                if abs(z) > 2:
                    if iteration == 0:
                        break
                    else:
                        color = round(iteration / max_iterations * 255)
                        break
            array_of_values[x_point][y_point] = color
    
    # Block for taking the statistics
    # for x in array_of_values:
    #     for y in x:
    #         statistics.write(str(f"{y}; "))

    return array_of_values

statistics = open("statistics.txt", "w")

pg.init()
screen = pg.display.set_mode((WIGHT, HEIGHT))
screen.fill((BLACK))
pg.display.set_caption("Array method")

h = 0.79
v = 0.15
scale = 0.004

x_coordinates = np.linspace(-2 * scale - h, 2 * scale - h, WIGHT)
y_coordinates = np.linspace(-2 * scale - v, 2 * scale - v, HEIGHT)

array_of_values = np.zeros((WIGHT, HEIGHT))

cahnged_array = get_Mandelbrots_array(90)
pg.surfarray.blit_array(screen, cahnged_array)
pg.display.update()

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
