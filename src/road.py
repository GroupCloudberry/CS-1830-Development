import random
import math
from vector import Vector

import simpleguitk as simplegui
Points = list()


class Road:
    def __init__(self):
        self.pointsList=[]
        self.p1=Vector(100,100)
        self.p2=Vector(100,100)


    def initSlope(self):
        x = 0
        y = 400
        self.pointsList.append(Vector(x, y))

        for a in range(0, 50):
            k = random.randint(0, 20)
            x = x + 10
            y = k * (math.cos(2 * x))+400
            self.pointsList.append(Vector(x, y))


    def draw(self,canvas,cam):

        for a in range(0, 50):
            p1=self.p1.copy().transformToCam(cam)
            p2=self.p2.copy().transformToCam(cam)
            print(p1,p2)

            point1=self.pointsList[a].copy().transformToCam(cam)
            point2 = self.pointsList[a+1].copy().transformToCam(cam)

            canvas.draw_line(point1.getP(),point2.getP(), 1, 'Pink')


