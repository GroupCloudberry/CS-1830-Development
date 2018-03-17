from vector import Vector
from values import Values
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
import time
from level_camera import LevelCamera
#Using simplegui load_image to import the image for the tyre
tyre_image = simplegui.load_image(Values.tyre_sprite)


class Car:

    def __init__(self, position, fuel,road,cam):
        #Car center position
        #Position vector
        self.original_position = position.copy().transformToCam(cam)
        self.position = position.copy().transformToCam(cam)

        #System Time
        self.prevTime = time.time()

        #Tyre attributes
        self.tyre_radius = 15
        #Tyre1
        self.tyre1 = Vector(self.position.getX() + 40, self.position.getY())

        # Tyre2
        self.tyre2 = Vector(self.position.getX() - 40, self.position.getY())

        #Fuel
        self.fuel = fuel
        self.fuel_distance = fuel*1000

        #Road
        self.road = road
        self.roadPoints = road.getPointsList()
        self.road_thickness = 5

        #Cam
        self.cam = cam


        #Road points
        self.point1 = 0
        self.point2 = 0

        #Mechanics
        #Velocity vector
        self.velocity = Vector()

        #Setting constans
        self.maxHorizontalvelocity = 200

        #constants
        self.movementDistance = 0

    def findRoadPoints(self, currentX):
        point1 = 0
        point2 = 0
        for i in range (len(self.roadPoints)-1):
            if currentX <= self.roadPoints[i].getX():
                point1 = self.roadPoints[i-1]
                point2 = self.roadPoints[i]
                break
        self.point1 = point1
        self.point2 = point2


    def applyGravity(self, roadHeight):
        if self.position.getY()<=roadHeight - self.tyre_radius - self.road_thickness:
            self.position.add(Vector(0, 2))

        if self.position.getY()>roadHeight - self.tyre_radius - self.road_thickness:
            self.position.subtract(Vector(0,2))

    def getHorizontalvelocity(self):
        return self.velocity.getX()

    def moveRight(self):
        if self.getHorizontalvelocity()<= self.maxHorizontalvelocity:
            self.velocity.add(Vector(1,0))

    def moveLeft(self):
        if self.getHorizontalvelocity()*-1 <= self.maxHorizontalvelocity:
            self.velocity.subtract(Vector(1,0))

    def setVelocityZero(self):
        yForce = self.velocity.getY()
        self.velocity = Vector(0, yForce)

    def reduceHorizontalVelocity(self):
        if self.velocity.getX()>=0:
            if self.velocity.getX()>3:
                self.velocity.subtract(Vector(3,0))
            if self.velocity.getX()<=3:
                if self.velocity.getX()>0:
                    self.velocity.subtract(Vector(1,0))
        if self.velocity.getX()<0:
            if self.velocity.getX()<-3:
                self.velocity.add(Vector(3,0))
            if self.velocity.getX()>=-3:
                if self.velocity.getX()<0:
                    self.velocity.add(Vector(1,0))

    def updateHorizontalPosition(self):
        self.position.add(Vector(self.velocity.getX()/10, 0))
        self.cam.moveSensitivity = self.velocity.getX()/10

    def drawCar(self, canvas):
        newposition = self.position.copy().transformFromCam(self.cam)
        canvas.draw_circle((newposition.getX(), newposition.getY()), self.tyre_radius, 5, 'Green', 'Green')

        currentX = newposition.getX() + (newposition.getX()-self.cam.origin.getX())
        self.findRoadPoints(currentX)
        roadHeight = self.road.getRoadHeight(self.point1, self.point2, currentX)
        self.applyGravity(roadHeight)
        self.updateHorizontalPosition()
        print("velocity : " + str(self.velocity) + " Position: " + str(self.position) + " CurrentX: " + str(currentX) + " cam Origin: " + str(self.cam.origin))
        print(self.movementDistance)


