import numpy as np
import pygame as pg
from math import *
from utils import *

        
def get_fractal(step=0.01, zoom=10, max_iterations=10):
    """ В этом блоке перебираем все координаты и строим последовательность """
    
    x, y, = -2, -2

    while x < 2:
        while y < 2:
            # Now we're have to create a c variable wich is complex
            # c = x + yi

            c = x + 1j * y
            z = 0
            
            for iteration in range(max_iterations):
                z = z ** 2 + c

                if abs(z) > 2:
                    sharpness = 255 / max_iterations
                    color = round((max_iterations - iteration) * sharpness)

                    pg.draw.circle(sc, (color, color, color), (x+x_center, y+y_center), 1)
                    break
                else:
                    pg.draw.circle(sc, (220, 220, 220), (x+x_center, y+y_center), 1)
        y += step
    x += step


pg.init()
sc = pg.display.set_mode((WIGHT, HEIGHT))
pg.display.set_caption("Mandelbrod's set")

clock = pg.time.Clock()

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
    
    sc.fill((5, 30, 10))
    get_fractal(50)

    pg.display.update()