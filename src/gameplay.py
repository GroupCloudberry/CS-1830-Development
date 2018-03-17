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
        self.endOfRoadRight_Origin = Vector(1000-(Values.canvas_WIDTH/2), Values.canvas_HEIGHT/2).copy().transformToCam(cam)

        self.point1 = Vector()
        self.point2 = Vector()

        self.position = Vector(300,100)

        self.tyre_radius = 15


    #Road for level 1
    def createLevel1(self):
        negativeRoad= Vector(-50, 400)

        startingPoint = Vector(0, 400)
        straightlineEnd = Vector(300, 400)

        slope1End = Vector(650, 200)

        slope2End = Vector(800, 400)

        straightLine3end = Vector(1000,400)

        self.pointsList.append(negativeRoad)
        self.pointsList.append(startingPoint)
        self.pointsList.append(straightlineEnd)
        self.pointsList.append(slope1End)
        self.pointsList.append(slope2End)
        self.pointsList.append(straightLine3end)

        print(len(self.pointsList))

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





