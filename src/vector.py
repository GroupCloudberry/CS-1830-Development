
import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def getP(self):
        return (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def copy(self):
        v = Vector(self.x, self.y)
        return v

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def divide(self, k):
        self.x /= k
        self.y /= k
        return self

    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def multiplyVector(self, other):
        self.x *= other.x
        self.y *= other.y
        return self.y

    def divideVector(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def toBackground(self, mover):
        self.subtract(mover.center)
        ratio=mover.dimCanv.copy().divideVector(mover.dim)
        self.multiplyVector(ratio)
        self.add(mover.dimCanv.copy().divide(2))
        return self
