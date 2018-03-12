from Vector import Vector


class Camera:
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



    def move(self):

        if self.moveUp==True:
            self.origin.add(Vector(0,-self.moveSensitivity))
        if self.moveDown==True:
            self.origin.add(Vector(0,self.moveSensitivity))

        if self.moveLeft == True:
            self.origin.add(Vector(-self.moveSensitivity,0))
        if self.moveRight == True:
            self.origin.add(Vector(self.moveSensitivity,0))


    def zoom(self):
        if self.zoomOut == True:
            self.dim.add(self.dim.copy().multiply(self.zoomSensitivity))

        if self.zoomIn == True:

                self.dim.add(self.dim.copy().multiply(-self.zoomSensitivity))

    def ratioToCam(self):
        return(self.dimCanv.copy().divideVector(self.dim).getX())

    def ratioToCanv(self):
        return (self.dim.copy().divideVector(self.dimCanv).getX())

    def get(self):
        return(self.origin, self.dim.x)
