class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration

    def brake(self, deceleration):
        self.speed = self.speed - deceleration

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newspeed):
        self.speed = newspeed


