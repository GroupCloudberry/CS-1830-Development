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

    def __init__(self, position):
        self.speed = 0
        self.tyre_radius = 15
        self.prevTime=time.time()
        self.position = position
        self.vel = Vector()
        #load images

        self.tyre1x = position.getX() + 30
        self.tyre1y = position.getY()

        self.tyre2x = position.getX() - 30
        self.tyre2y = position.getY()

        self.rotation = 0
        self.acceleration = Vector()

        #Defining tyre edges
        self.tyre1_offset = self.tyre1y + self.tyre_radius
        self.tyre2_offset = self.tyre2y + self.tyre_radius


    # car mechanics
    def accelerate(self):
        if self.acceleration.getX() <= 150:
            self.acceleration.add(Vector(3,0))
        self.vel.add(Vector(10, 0))
        self.vel.add(self.acceleration)
        self.rotation = self.rotation + 1
        print(self.acceleration)

    def reverse(self):
        self.vel.add(Vector(-10, 0))
        if self.acceleration.getX() <= 150:
            self.acceleration.add(Vector(3,0))
        self.vel.add(-self.acceleration)
        self.rotation = self.rotation - 1
        print(self.acceleration)

    def brake(self):
        self.acceleration = Vector(0,0)

    def getspeed(self):
        return self.speed

    def setspeed(self, newspeed):
        self.speed = newspeed

    def drawcar(self, canvas):
        # Drawing Front tyre
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre1x, self.tyre1y),
                          (self.tyre_radius*2.2, self.tyre_radius*2.2), self.rotation)

        # Drawing Back tyre
        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre2x, self.tyre2y),
                          (self.tyre_radius * 2.2, self.tyre_radius * 2.2), self.rotation)

    def updatePosition(self):
        # Front tyre
        self.tyre1x = self.position.getX() + 40
        self.tyre1y = self.position.getY()

        # Back tyre
        self.tyre2x = self.position.getX() - 40
        self.tyre2y = self.position.getY()

        #Updating offsets
        self.tyre1_offset = self.tyre1y + self.tyre_radius
        self.tyre2_offset = self.tyre2y + self.tyre_radius


    def update(self):
        self.position.add(self.vel.multiply(time.time()-self.prevTime))
        self.prevTime=time.time()

        #Updating tyre position
        self.updatePosition()

