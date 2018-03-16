from vector import Vector


class LevelCamera:
    def __init__(self, origin ,zoomSens,moveSense,dimCanv):

        self.origin = origin
        self.dim = dimCanv
        self.dimCanv=dimCanv.copy()
        self.zoomIn=False
        self.zoomOut=False
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False
        self.moveSensitivity=moveSense
        self.zoomSensitivity=zoomSens

    def ratioToCam(self):
        return(self.dimCanv.copy().divideVector(self.dim).getX())

    def ratioToCanv(self):
        return (self.dim.copy().divideVector(self.dimCanv).getX())

    def get(self):
        return(self.origin, self.dim.x)

    def setOrigin(self, carposition):
        self.origin = carposition

    def zoomin(self):
        self.dim.add(self.dim.copy().multiply(-self.zoomSensitivity))

    def zoomout(self):
        self.dim.add(self.dim.copy().multiply(self.zoomSensitivity))

    def move_down(self):
        self.origin.add(Vector(0, self.moveSensitivity))

    def move_up(self):
        self.origin.add(Vector(0, -self.moveSensitivity))

    def move_left(self):
        self.origin.add(Vector(-self.moveSensitivity, 0))

    def move_right(self):
        self.origin.add(Vector(self.moveSensitivity, 0))

    def move(self):
        if self.moveUp == True:
            self.move_up()

        if self.moveDown == True:
            self.move_down()

        if self.moveLeft == True:
            self.move_left()

        if self.moveRight == True:
            self.move_right()

    def zoom(self):
        if self.zoomOut == True:
            self.zoomout()

        if self.zoomIn == True:
            self.zoomin()

