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

    def getRoadHeight(self, point1, point2, currentX):
        #Defining variables
        x1 = point1.getX()
        x2 = point2.getX()
        y1 = point1.getY()
        y2 = point2.getY()

        #Graditent
        m = (y2-y1)/(x2-x1)

        #Y co-ordinate of road
        roadHeight = (m * (currentX-x1)) + y1

        return roadHeight


    def constructCar(self, canvas, position ,cam):
        canvas.draw_circle(position.copy().transformToCam(cam).getP(), 15, 5, 'Green', 'Green')



    def draw(self,canvas,cam):
        for i in range(len(self.pointsList)-1):
            point1 = self.pointsList[i].copy().transformToCam(cam)
            point2 = self.pointsList[i+1].copy().transformToCam(cam)
            canvas.draw_line(point1.getP(), point2.getP(), 5, 'white')

            self.constructCar(canvas, Vector(100,200), cam)

            print(cam.origin)



