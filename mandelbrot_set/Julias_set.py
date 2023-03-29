from utils import *
import pygame as pg
import numpy as np
import numba
from math import sin, cos


@numba.njit(fastmath=True)
def get_Mandelbrots_array(array_of_values, max_iterations=10, alpha=0):
    for x_point, x in enumerate(x_coordinates):
        for y_point, y in enumerate(y_coordinates):
            c = complex(-sin(alpha), cos(alpha))
            z = complex(x, y)

            for iteration in range(max_iterations):
                z = z ** 2 + c
                color = 0

                if z.real ** 2 + z.imag ** 2 > 4:
                    if iteration == 0:
                        break
                    else:
                        color = round(iteration / max_iterations * 255)
                        break
            array_of_values[x_point][y_point] = color

    return array_of_values


pg.init()
screen = pg.display.set_mode((WIGHT, HEIGHT))
screen.fill(BLACK)
pg.display.set_caption("Array method")
clock = pg.time.Clock()

h = 0  #0.7451580731
v = 0  #0.1125749152
scale = 1           # 5 * 10 ** -10
infinity = 30

x_coordinates = np.linspace(-2 * scale - h, 2 * scale - h, WIGHT)
y_coordinates = np.linspace(-2 * scale - v, 2 * scale - v, HEIGHT)

array_of_values = np.zeros((WIGHT, HEIGHT))
alpha = 0

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False

    clock.tick(30)

    changed_array = get_Mandelbrots_array(array_of_values, infinity, alpha)
    pg.surfarray.blit_array(screen, changed_array)

    # pg.draw.line(screen, "white", (0, 0), (WIGHT, HEIGHT), 1)
    # pg.draw.line(screen, "white", (0, HEIGHT), (WIGHT, 0))

    alpha += 0.05
    pg.display.update()
