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
        canvas.draw_circle(self.position.copy().transformToCam(cam).getP(), 15, 5, 'Green', 'Green')
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
        print("Car is between " + str(self.point1.getP()) + " and " + str(self.point2.getP()))


    def getRoadHeight(self):
        pass


    def draw(self,canvas,cam):
        for i in range(len(self.pointsList)-1):
            point1 = self.pointsList[i].copy().transformToCam(cam)
            point2 = self.pointsList[i+1].copy().transformToCam(cam)
            canvas.draw_line(point1.getP(), point2.getP(), 5, 'white')

        self.constructCar(canvas, cam)




