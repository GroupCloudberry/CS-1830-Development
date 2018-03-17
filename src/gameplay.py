import random
import math
from vector import Vector
from values import Values
import simpleguitk as simplegui

class GamePlay:

    def __init__(self, cam):
        #Road
        self.pointsList = list()
        self.endOfRoad_Origin = Vector(Values.canvas_WIDTH/2, Values.canvas_HEIGHT/2).copy().transformToCam(cam)
        self.endOfRoadRight_Origin = Vector(15000-(Values.canvas_WIDTH/2), Values.canvas_HEIGHT/2).copy().transformToCam(cam)

        self.point1 = Vector()
        self.point2 = Vector()

        self.position = Vector(300,100)

        self.tyre_radius = 15


#Road for level 1
    def createLevel1(self):
        negativeRoad = Vector(-50, 400)

        startingPoint = Vector(0, 400)
        straightlineEnd = Vector(300, 400)
        slope1End = Vector(600, 300)
        slope2End = Vector(900, 400)
        straightLine3end = Vector(2000, 400)
        slope4end = Vector(2400, 300)
        slope5end = Vector(2800, 300)
        straight6end = Vector(3500, 300)
        slope7end = Vector(4000, 400)
        straight8end = Vector(6000, 400)
        slope9end = Vector(6500, 200)
        slope10end = Vector(7000, 400)
        straight11end = Vector(8000, 400)
        slope12end = Vector(10000, 300)
        slope13end = Vector(12000, 300)
        slope14end = Vector(13000, 400)
        straight15end = Vector(15000, 400)

        self.pointsList.append(negativeRoad)
        self.pointsList.append(startingPoint)
        self.pointsList.append(straightlineEnd)
        self.pointsList.append(slope1End)
        self.pointsList.append(slope2End)
        self.pointsList.append(straightLine3end)
        self.pointsList.append(slope4end)
        self.pointsList.append(slope5end)
        self.pointsList.append(straight6end)
        self.pointsList.append(slope7end)
        self.pointsList.append(straight8end)
        self.pointsList.append(slope9end)
        self.pointsList.append(slope10end)
        self.pointsList.append(straight11end)
        self.pointsList.append(slope12end)
        self.pointsList.append(slope13end)
        self.pointsList.append(slope14end)
        self.pointsList.append(straight15end)

        print(len(self.pointsList))

    def createLevel2(self):
        self.pointsList.append(Vector(-50, 400))
        self.pointsList.append(Vector(0, 400))
        self.pointsList.append(Vector(700, 400))
        self.pointsList.append(Vector(700, 250))
        self.pointsList.append(Vector(1100, 350))
        self.pointsList.append(Vector(1500, 350))
        self.pointsList.append(Vector(1600, 400))
        self.pointsList.append(Vector(2000, 400))
        self.pointsList.append(Vector(2300, 200))
        self.pointsList.append(Vector(2700, 400))
        self.pointsList.append(Vector(3200, 400))
        self.pointsList.append(Vector(3400, 250))
        self.pointsList.append(Vector(3800, 400))
        self.pointsList.append(Vector(4500, 400))
        self.pointsList.append(Vector(5000, 200))
        self.pointsList.append(Vector(5350, 400))
        self.pointsList.append(Vector(6000, 400))
        self.pointsList.append(Vector(7500, 400))
        self.pointsList.append(Vector(8000, 200))
        self.pointsList.append(Vector(8300, 400))
        self.pointsList.append(Vector(8500, 400))
        self.pointsList.append(Vector(9000, 200))
        self.pointsList.append(Vector(9400, 400))
        self.pointsList.append(Vector(10000, 400))
        






    #Returns point list
    def getPointsList(self):
        return self.pointsList

    def constructCar(self, canvas ,cam):
        canvas.draw_circle(self.position.copy().transformToCam(cam).getP(), self.tyre_radius, 5, 'Green', 'Green')
        self.applyGravity()

    def moveCarRight(self):
        self.position.add(Vector(5, 0))

    def moveCarLeft(self):
        self.position.add(Vector(-5,0))

    def findRoadPoints(self, currentX):
        for i in range(len(self.pointsList)-1):
            if self.pointsList[i].getX() <= currentX:
                self.point1 = self.pointsList[i]
                self.point2 = self.pointsList[i+1]

    def applyGravity(self):
        self.findRoadPoints(self.position.getX())
        roadY = self.getRoadHeight(self.point1, self.point2, self.position.getX())
        print("Road Y Co-ordinate is at " + str(roadY))

        if self.position.getY()<= roadY - self.tyre_radius:
            self.position.add(Vector(0,4))
        elif self.position.getY()>roadY - self.tyre_radius:
            self.position.subtract(Vector(0,4))


    def getRoadHeight(self, point1, point2, currentX):
        x1 = point1.getX()
        x2 = point2.getX()
        y1 = point1.getY()
        y2 = point2.getY()

        #Gradient
        m = (y2-y1)/(x2-x1)

        roadHeight = (m*(currentX-x1)) + y1
        return roadHeight


    def draw(self,canvas,cam):
        for i in range(len(self.pointsList)-1):
            point1 = self.pointsList[i].copy().transformToCam(cam)
            point2 = self.pointsList[i+1].copy().transformToCam(cam)
            canvas.draw_line(point1.getP(), point2.getP(), 5, 'white')

        self.constructCar(canvas, cam)





