from transition_clock import TransitionClock
from vector import Vector
from values import Values
from gameplay import GamePlay
from car import Car
from move_objects import MoveObjects

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
from values import Values


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

        self.initial_origin_vector = Vector(Values.canvas_WIDTH/2, Values.canvas_HEIGHT/2)

        #Creating camera with origin (center point) set to center point of canvas
        self.cam = MoveObjects(self.initial_origin_vector,
                               Vector(Values.canvas_WIDTH,Values.canvas_HEIGHT))

        self.final_origin = self.initial_origin_vector.copy().toBackground(self.cam)
        self.cam.setCenter(self.final_origin)

        # Road bounds (Camera)
        self.leftEnd = False
        self.rightEnd = False

        #self.car = Car(Vector(30, 100), 100, self.road,self.cam)

        self.gameplay = GamePlay(self.cam)

        #Car control booleans
        self.moveCarRight = False
        self.moveCarLeft = False
        self.moveCarUp = False
        self.moveCarDown = False

        #Level creation
        self.gameplay.createLevel1()



    def draw_canvas(self, canvas):
        #Check if window was just opened and display animation if true
        self.transition_clock.tick()
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)

        #Draw road
        self.gameplay.draw(canvas, self.cam)

        #Setting key up and down handlers and updating
        self.window.frame.set_keydown_handler(self.keydown)
        self.window.frame.set_keyup_handler(self.keyup)
        self.updateKey()

        #Car
        #self.car.drawCar(canvas)


    #Curtain animation mathod
    def reveal(self, canvas):
        box_colour_left = "Black"
        box_colour_right = "Black"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour_left, box_colour_left)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25


    def keyup(self,key):
        if key == simplegui.KEY_MAP['right']:
            self.cam.moveRight = False
            self.moveCarRight = False
        elif key == simplegui.KEY_MAP['left']:
            self.cam.moveLeft = False
            self.moveCarLeft = False
        elif key == simplegui.KEY_MAP['up']:
            self.cam.moveUp = False
        elif key == simplegui.KEY_MAP['down']:
            self.cam.moveDown = False

    def keydown(self,key):
        if key == simplegui.KEY_MAP['right']:
            self.cam.moveRight = True
            #Move car right
            self.moveCarRight = True

        elif key == simplegui.KEY_MAP['left']:
            self.cam.moveLeft = True
            #Move car left
            self.moveCarLeft = True

        elif key == simplegui.KEY_MAP['up']:
            self.cam.moveUp = True
        elif key == simplegui.KEY_MAP['down']:
            self.cam.moveDown = True

    def checkRoadEnds(self):
        if self.cam.center.getX() < self.gameplay.endOfRoad_Origin.getX():
            self.leftEnd = True

        else:
            self.leftEnd = False
        if self.cam.center.getX() > self.gameplay.endOfRoadRight_Origin.getX():
            self.rightEnd = True
        else:
            self.rightEnd = False


    def updateKey(self):
        self.checkRoadEnds()
        self.cam.move(self.leftEnd, self.rightEnd)

        #Move car
        if self.moveCarRight == True:
            self.gameplay.moveCarRight()
        elif self.moveCarLeft == True:
            self.gameplay.moveCarLeft()
        #self.cam.zoom() -- Zoom feature is disabled
