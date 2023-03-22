import numpy as np
import pygame as pg
from math import *
from utils import *

        
def get_fractal(zoom=10, max_iterations=10):
    """ В этом блоке перебираем все координаты и строим последовательность """

    for x in range(WIGHT):
        for y in range(HEIGHT):
            c = (x - x_center) * h * zoom + (y - y_center) * h * zoom * -1
            z = 0
            for iteration in range(max_iterations):
                z = z ** 2 + c

                if abs(z) > 2:
                    sharpness = 255 // max_iterations
                    color = (iteration // max_iterations) * sharpness
                    pg.draw.circle(sc, (color, color, color), (x, y), 3)
                    break
                else:
                    pg.draw.circle(sc, (255, 255, 255), (x, y), 3)


pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod's set")

clock = pg.time.Clock()

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
    
    sc.fill((5, 4, 10))
    get_fractal(5)

    pg.display.update()