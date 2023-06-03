import numpy as np
import os


WIGHT, HEIGHT = 120, 30
FOV = np.pi / 3
perspective = 1 / np.tan(FOV/2)
aspect = WIGHT / HEIGHT
colours = " .-~=crox(JORX0$%@"


class RayMarching:
    def __init__(self):
        self.screen = [[colours[0] for n in range(WIGHT)] for m in range(HEIGHT)]
        self.sphere = np.array([0, 0, 0])
        self.cube = np.array([0, 0, 0])
        
        self.radius = 0.8
        self.board = 0.7

        self.RO = np.array([0, 0, -2])

        self.x_line = np.linspace(-1, 1, WIGHT)
        self.y_line = np.linspace(1, -1, HEIGHT)

    def sphere_SDF(self, point):
        """ Returns the distance to sphere`s surface """
        
        return self.lenght(point, self.sphere) - self.radius

    def cube_SDF(self, point):
        """ Returns the distance to cube """

        return min(np.abs(point) - self.board)

    def show_screen(self):
        """ Shows the screen with all the result """

        os.system("cls")
        for row in self.screen:
            print("".join(row))

    @staticmethod
    def lenght(point1, point2=(0, 0, 0)):
        return np.sqrt(
            (point2[0] - point1[0]) ** 2 * aspect +
            (point2[1] - point1[1]) ** 2 +
            (point2[2] - point1[2]) ** 2
        )

    def calculate_surface(self):
        """ Here we're calculating all the surface pixels """

        for y_, y in enumerate(self.y_line):
            for x_, x in enumerate(self.x_line):
                z = -2
                for step in range(len(colours)-1):
                    point = [x, y, z]
                    distance = self.sphere_SDF(point)

                    if distance < 0.1:
                        self.screen[y_][x_] = colours[step]
                        break

                    elif distance > 10:
                        self.screen[y_][x_] = " "

                    z += distance
        self.show_screen()


rm = RayMarching()
rm.calculate_surface()