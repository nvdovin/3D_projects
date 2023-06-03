import pygame as pg
import numpy as np
from math import sqrt
import utils as u


class SphereRM:
    pg.init()

    def __init__(self, R=0.5):
        self.R = R
        self.x_line = np.linspace(-1, 1, u.WIGHT)
        self.y_line = np.linspace(-1, 1, u.HEIGHT)
        self.sphere = np.array([0, 0, 0])
        self.light = np.array([-1, -1, -1])

        self.screen = pg.display.set_mode((u.WIGHT, u.HEIGHT))

    def get_sphere(self):
        for row in range(u.WIGHT):
            for col in range(u.HEIGHT):
                for step in range(10):
                    distance = sqrt((x))

    def get_main_cycle(self):
        cycle = True
        while cycle:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    cycle = False
            self.screen.fill(u.black)


rm = SphereRM()
rm.get_main_cycle()
