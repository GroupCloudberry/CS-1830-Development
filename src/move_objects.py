from vector import Vector


class MoveObjects:
    def __init__(self, center, canvas_DIM):

        self.center = center
        self.DIM = canvas_DIM
        self.canvas_DIM=canvas_DIM.copy()
        self.moveLeft=False
        self.moveRight=False
        self.speed=5

    def setCenter(self, carposition):
        self.center = carposition

    def move_left(self):
        self.center.add(Vector(-self.speed, 0))

    def move_right(self):
        self.center.add(Vector(self.speed, 0))

    def move(self,leftEnd, rightEnd):
        if self.moveLeft == True and not leftEnd:
            self.move_left()

        if self.moveRight == True and not rightEnd:
            self.move_right()
