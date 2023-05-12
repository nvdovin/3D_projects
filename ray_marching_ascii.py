import numpy as np
import os


class RayMarching:
    WIGHT = 120
    HEIGHT = 30
    h = WIGHT / HEIGHT

    def __init__(self, R=0.2, max_steps=10, depth=-2):
        self.max_steps = max_steps
        self.R = R
        self.screen = [[" " for n in range(self.WIGHT)] for m in range(self.HEIGHT)]

        self.x_line = np.linspace(-1, 1, self.WIGHT)
        self.y_line = np.linspace(1, -1, self.HEIGHT)

        self.sphere = np.array([0, 0, 0])
        self.tor = np.array([0, -0.3, 0])

        self.light = np.array([-0.8, 0.8, -2])
        self.camera = np.array([0, 0, depth])

        self.gradient = " -~+=loxIOSXG%#@"

    def show_it(self):
        """ This module can show us rendered model """

        os.system("cls")
        RayMarching.get_sphere(self)

        for row in self.screen:
            print("".join(row))

    def get_sphere(self):
        """ This module return us ready 3D sphere, created by RayMarching """

        for x_point, x in enumerate(self.x_line):
            for y_point, y in enumerate(self.y_line):
                z = 0
                for step in range(self.max_steps):
                    distance = np.sqrt(
                        (x - self.sphere[0]) ** 2 * self.h +
                        (y - self.sphere[1]) ** 2 +
                        (z - self.sphere[2]) ** 2
                    ) - self.R
                    # distance = np.sqrt(np.sqrt(((x - self.tor[0]) ** 2 + (z - self.tor[2])) - self.R) ** 2 + (y - self.tor[1])) - (self.R - 0.1)

                    z += distance

                    # test
                    # print(f"({round(x, 3)};{round(y, 3)} - dist({round(distance, 2)})")

                    if distance < 0.01:
                        self.screen[y_point][x_point] = self.gradient[len(self.gradient)-1]
        return self


R = 0.8
max_steps = 20
depht = -1

rm = RayMarching(R, max_steps, depht)
rm.show_it()
