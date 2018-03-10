from vector import Vector
from values import Values
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


#Using simplegui load_image to import the image for the tyre

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week5-triangle2.png")


class Car:
    def __init__(self,position):
        self.speed = 0
        self.tyre_radius = 15

        self.position = position
        self.tyre1 = [position.getX(), position.getY()]
        self.tyre2 = [position.getX() + 100, position.getY()]
        self.vel = Vector()
        #load images


    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration

    def brake(self, deceleration):
        self.speed = self.speed - deceleration

    def getspeed(self):
        return self.speed

    def setspeed(self, newspeed):
        self.speed = newspeed

    def drawcar(self, canvas):
        global tyre_img
        #Drawing tyres
        #tyre1

        canvas.draw_image(image, (image.get_width() / 2, image.get_height() / 2), (image.get_width(), image.get_height()), (200,200), (100,100))
        canvas.draw_circle(self.tyre1, self.tyre_radius, 0, 'White', 'White')
        canvas.draw_circle(self.tyre2, self.tyre_radius, 0, 'White', 'White')


    def update(self):
        self.position.add(self.vel)
        self.tyre1 = [self.position.getX(), self.position.getY()]
        self.tyre2 = [self.position.getX()+100, self.position.getY()]
        self.vel.multiply(0.85)



