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
        self.tyre1 = [position.getX(), position.getY()]
        self.tyre2 = [position.getX() + 100, position.getY()]
        self.vel = Vector(0,0)
        #load images

        self.rotation = 0


    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration

    def brake(self, deceleration):
        self.speed = self.speed - deceleration

    def getspeed(self):
        return self.speed

    def setspeed(self, newspeed):
        self.speed = newspeed

    def drawcar(self, canvas):
        #Drawing tyres
        #tyre1

        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre1[0], self.tyre1[1]),
                          (self.tyre_radius*2.2, self.tyre_radius*2.2), self.rotation)

        canvas.draw_image(tyre_image, (tyre_image.get_width() / 2, tyre_image.get_height() / 2),
                          (tyre_image.get_width(), tyre_image.get_height()), (self.tyre2[0], self.tyre2[1]),
                          (self.tyre_radius * 2.2, self.tyre_radius * 2.2), self.rotation)


    def update(self):


        self.position.add(self.vel.multiply(time.time()-self.prevTime))
        self.prevTime=time.time()

        self.tyre1 = [self.position.getX(), self.position.getY()]
        self.tyre2 = [self.position.getX()+100, self.position.getY()]
