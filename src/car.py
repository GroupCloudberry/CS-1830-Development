class Car:

    speed = 10

    def __init__(self):
        self.speed = 5

    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration

    def brake(self, deceleration):
        self.speed = self.speed - deceleration

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newspeed):
        self.speed = newspeed




