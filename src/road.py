
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
import random
from values import Values

"""
Points_straight = list()
Points_smallBump = list()
Points_bigBump = list()
Points_slope = list()
Points = list()


class Keyboard:
    def _init_(self):
        self.right = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False


class Road:
    def straight(self, a):
        y = 400
        x = 0
        global Points_straight
        Points_straight.append((x, y))

        while x < a:
            x = x + 5
        Points_straight.append((x, y))
        return x

    def smallBump(self):
        # y = random.randint(390, 410)
        y = 350
        x = Road.straight(self, 300) + 50
        global Points_smallBump
        Points_smallBump.append((x, y))
        y = 400
        x = x + 50
        Points_smallBump.append((x, y))
        return x

    def bigBump(self):
        y = 300
        x = Road.smallBump(self) + 50
        global Points_bigBump
        Points_bigBump.append((x, y))
        y = 400
        x = x + 50
        Points_bigBump.append((x, y))
        return x

    def slope(self):
        y = 200
        x = 575
        global Points_slope
        Points_slope.append((x, y))
        y = 400
        x = x + 50
        # Points_slope.append((x, 400))
        return x

    def draw_handler(canvas):
        global Points_straight, Points_smallBump, Points_bigBump, Points_slope, Points
        Road.straight(canvas, 300)
        Road.smallBump(canvas)
        Road.bigBump(canvas)
        Road.slope(canvas)
        Points = Points_straight
        Points.extend(Points_smallBump)
        Points.extend(Points_bigBump)
        Points.extend(Points_slope)

        a = 0
        print(Points)
        # canvas.draw_line((301, 401), (302, 400), 10, 'Brown')
        while a < 12:
            canvas.draw_line(Points[a], Points[a + 1], 10, 'Brown')
            a = a + 1
        canvas.draw_line((600, 400), (700, 400), 10, 'Brown')


frame = simplegui.create_frame("Testing", 700, 500)
frame.set_draw_handler(Road.draw_handler)
frame.start()
"""
class Road:
    def __init__(self,position):
        self.position = position

    def drawRoad(self,canvas):
        canvas.draw_line([0, 400], [Values.canvas_WIDTH, 400], 5, 'white')
        canvas.draw_line([300, 400], [Values.canvas_WIDTH-300, 200], 5 , 'white')