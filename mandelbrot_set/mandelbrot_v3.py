from utils import *
import pygame as pg
import numpy as np
# import numba

def get_Mandelbrots_array(max_iterations=10):
    for x_point, x in enumerate(x_coordinates):
        for y_point, y in enumerate(y_coordinates):
            c = complex(x, y)
            z = complex(0)

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

h = 0.789999333667175           # Чем больше, там левее
v = 0.157998399774343           # Чем больше, тем выше
scale = 0.81 # 8 * 10 ** -15

x_coordinates = np.linspace(-2 * scale - h, 2 * scale - h, WIGHT)
y_coordinates = np.linspace(-2 * scale - v, 2 * scale - v, HEIGHT)

array_of_values = np.zeros((WIGHT, HEIGHT))

cahnged_array = get_Mandelbrots_array(20)
pg.surfarray.blit_array(screen, cahnged_array)
# pg.draw.line(screen, WHITE, (0, 0), (WIGHT, HEIGHT), 1)
# pg.draw.line(screen, WHITE, (WIGHT, 0), (0, HEIGHT), 1)
pg.display.update()

cycle = True
while cycle:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
