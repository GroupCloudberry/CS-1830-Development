import random
import math
from vector import Vector

import simpleguitk as simplegui

Points = list()


class Road:
    def __init__(self):
        self.pointsList = []
        self.allPoints = []
        self.p1 = Vector(500, 500)
        self.p2 = Vector(500, 500)

    def initSlope(self):
        x = 0
        y = 400
        self.pointsList.append(Vector(x, y))

        m = 0
        n = 5 * (math.cos(m)) + 400
        self.allPoints.append(Vector(m, n))

        for a in range(0, 300):
            x = x + 10
            y = 2 * (math.cos(x)) + 400
            self.pointsList.append(Vector(x, y))

        for b in range(0, 3000):
            m += 1;
            # n = 2 * (math.cos(m)) + 400

            if (m % 5 == 0):
                n = 5 * (math.cos(m)) + 400
            elif (m % 3 == 0):
                n = 9 * (math.cos(m)) + 400
            else:
                n = 8 * (math.cos(m)) + 400
            self.allPoints.append(Vector(m, n))

    def getYcoord(self, x):
        if (x % 5 == 0):
            y = 5 * (math.cos(x)) + 400
        elif (x % 3 == 0):
            y = 9 * (math.cos(x)) + 400
        else:
            y = 8 * (math.cos(x)) + 400

        return y

    def draw(self, canvas, cam):

        for a in range(0, 300):
            p1 = self.p1.copy().transformToCam(cam)
            p2 = self.p2.copy().transformToCam(cam)
            print(p1, p2)

            point1 = self.pointsList[a].copy().transformToCam(cam)
            point2 = self.pointsList[a + 1].copy().transformToCam(cam)

            canvas.draw_line(point1.getP(), point2.getP(), 3, 'Pink')

        print(self.getYcoord(8))