from vector import Vector
from values import Values
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
import time

#Using simplegui load_image to import the image for the tyre

tyre_image = simplegui.load_image(Values.tyre_sprite)

class Car:

    def __init2__(self,vel,pos,fuel,angle):


        self.prevTime=time.time()

    def __init__(self, position, fuel):

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


        #Defining tyre positions
        self.tyre1x = position.getX() + 30
        self.tyre1y = position.getY()
        self.tyre2x = position.getX() - 30
        self.tyre2y = position.getY()


        #Defining tyre edges
        self.tyre1_offset_bottom = self.tyre1y + self.tyre_radius
        self.tyre2_offset_bottom = self.tyre2y + self.tyre_radius


        #Fuel
        self.fuel = fuel

        #Constants
        self.friction = Vector(-2,0)

    # car mechanics
    def accelerate(self):
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

    def reverse(self):
        if not self.acceleration==Vector(0,0):
            self.vel.add(-self.acceleration)
        else:
            self.vel.add(-self.friction)
        self.rotateTyreBackward()

    #Handling sprites and images
    def rotateTyreForward(self):
        self.rotation = self.rotation + 1

    def rotateTyreBackward(self):
        self.rotation = self.rotation - 1

    #Braking


    def updatePosition(self):
        # Front tyre
        self.tyre1x = self.position.getX() + 40
        self.tyre1y = self.position.getY()

        # Back tyre
        self.tyre2x = self.position.getX() - 40
        self.tyre2y = self.position.getY()

        #Updating offsets
        self.tyre1_offset_bottom = self.tyre1y + self.tyre_radius
        self.tyre2_offset_bottom = self.tyre2y + self.tyre_radius


    def update(self):
        self.position.add(self.vel.multiply(time.time()-self.prevTime))
        self.prevTime=time.time()

        #Updating tyre position
        self.updatePosition()

    #Method to reduce fuel as car travels distance
    def useFuel(self):
        self.fuel = self.fuel - 1

    #Displaying the updated car on canvas
    def drawcar(self, canvas):
        # Drawing Front tyre
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre1x, self.tyre1y),
                          (self.tyre_radius*2.2, self.tyre_radius*2.2), self.rotation)

        # Drawing Back tyre
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre2x, self.tyre2y),
                          (self.tyre_radius * 2.2, self.tyre_radius * 2.2), self.rotation)
