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

    def __init2__(self,vel,pos,fuel,angle):


        self.prevTime=time.time()

    def __init__(self, position, fuel,road,cam):

        #Position vector
        self.position = position

        #Use system time
        self.prevTime = time.time()

        #Velocity and acceleration
        self.vel = Vector()
        self.acceleration = Vector()


        #tyre radius and rotation
        self.tyre_radius = 15
        self.rotation = 0


        #Constants
        self.friction = Vector(-0.05,0)
        self.maxAcceleration = 50
        self.distancePerLitre = 100


        #Fuel (Get fuel in litres from the argument)
        self.fuelDistance = fuel * self.distancePerLitre
        self.fuel = fuel

        #Get the road
        self.road = road

        #Get the camera
        self.cam = cam#to be set everytime car is created

        #Defining tyre positions
        # Front tyre
        self.tyre1p = self.position.copy().transformToCam(self.cam)

        # Back tyre
        self.tyre2p = self.position.copy().transformToCam(self.cam)

        #Defining tyre edges
        self.tyre1_offset_bottom = self.tyre1p.getY() + self.tyre_radius
        self.tyre2_offset_bottom = self.tyre2p.getY() + self.tyre_radius


    # car mechanics
    def accelerate(self):
        if self.acceleration.getX() <= self.maxAcceleration:
            self.acceleration.add(Vector(3,0))

    def brake(self):
        self.acceleration = Vector(0,0)
        if not self.vel == Vector(0,0):
            self.vel.add(Vector(0,0))

    def moveForward(self):
        if not self.acceleration==Vector(0,0):
            self.vel.add(self.acceleration)
        else:
            self.vel.add(self.friction)
        self.rotateTyreForward()
        self.useFuel()

    def reverse(self):
        if not self.acceleration==Vector(0,0):
            self.vel.subtract(self.acceleration)
        else:
            self.vel.subtract(self.friction)
        self.rotateTyreBackward()
        self.useFuel()


    # Handling sprites and images
    def rotateTyreForward(self):
        self.rotation = self.rotation + 1

    def rotateTyreBackward(self):
        self.rotation = self.rotation - 1


    #Method to reduce fuel as car travels distance
    def useFuel(self):
        self.fuelDistance = self.fuelDistance - 1
        if self.fuelDistance % self.distancePerLitre == 0:
            self.fuel = self.fuel - 1

    def updatePosition(self):
        # Front tyre
        self.tyre1p = self.position

        # Back tyre
        self.tyre2p = self.position

        #Updating offsets
        self.tyre1_offset_bottom = self.tyre1p.getY() + self.tyre_radius
        self.tyre2_offset_bottom = self.tyre2p.getY() + self.tyre_radius


    def update(self):
        self.position.add(self.vel.multiply(time.time()-self.prevTime))
        self.prevTime=time.time()

        #Updating tyre position
        self.updatePosition()
        self.applyGravity()

    def applyGravity(self):
        if self.tyre1p.getY() > self.road.getYcoord(self.position.copy().transformFromCam(self.cam).getX()+40)+self.tyre_radius:
            self.tyre1p.add(Vector(0, -1))
        if self.tyre1p.getY() < self.road.getYcoord(self.position.copy().transformFromCam(self.cam).getX()+40)+self.tyre_radius:
            self.tyre1p.add(Vector(0, 1))
        fetchedYforTyre2 = self.road.getYcoord(self.position.copy().transformFromCam(self.cam).getX()-40)
        print("tyre2 Y :" + str(self.tyre1p.getY()) + "| Road Y: " + str(fetchedYforTyre2))
        if self.tyre2p.getY() < fetchedYforTyre2 + self.tyre_radius:
            self.tyre2p.add(Vector(0, 1))
        if self.tyre2p.getY() > fetchedYforTyre2 + self.tyre_radius:
            self.tyre2p.add(Vector(0, -1))



    #Displaying the updated car on canvas
    def drawcar(self, canvas):
        # Drawing Front tyre
        self.applyGravity()
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre1p.copy().transformToCam(self.cam).getX()+40, self.tyre1p.copy().transformToCam(self.cam).getY()),
                          (self.tyre_radius*2.2, self.tyre_radius*2.2), self.rotation)

        # Drawing Back tyre
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre2p.copy().transformToCam(self.cam).getX()-40, self.tyre2p.copy().transformToCam(self.cam).getY()),
                          (self.tyre_radius * 2.2, self.tyre_radius * 2.2), self.rotation)

