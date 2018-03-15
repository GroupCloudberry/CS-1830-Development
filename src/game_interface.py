from transition_clock import TransitionClock
from vector import Vector
from values import Values
from road import Road
from car import Car
from level_camera import LevelCamera

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

<<<<<<< HEAD
        self.road = Road()
        self.road.initSlope()
        self.cam = LevelCamera(Vector(100, Values.canvas_HEIGHT / 2), Values.CAM_ZOOM_SENSITIVITY, Values.CAM_MOVE_SENSITIVITY, Vector(800, 600))
        self.cam.origin = Vector(400,400)
        self.car = Car(Vector(100, Values.canvas_HEIGHT / 2), 100, self.road,self.cam)


=======
>>>>>>> 428fe2567f453febc45851e3ed354384f120b7cc
    def draw_canvas(self, canvas):
        # Increment the clock counter each time a frame is drawn to facilitate time-based functionality
        self.transition_clock.tick()

        canvas.draw_line([0,400], [800,400], "10", 'white')

        # Draw the covers and incrementally reveal the underlying content
        # To cover all elements, the cover needs to be be drawn last
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)
<<<<<<< HEAD
        #Set keyup and down handlers
        self.road.draw(canvas, self.cam)
        self.window.frame.set_keydown_handler(self.keydown)
        self.window.frame.set_keyup_handler(self.keyup)
        self.car.update()
        self.car.drawcar(canvas)

        self.updateKey()

=======

        # Set key up and down handlers
>>>>>>> 428fe2567f453febc45851e3ed354384f120b7cc

    # Curtain animation mechanism
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
        if key == simplegui.KEY_MAP['r']:
            self.cam.zoomOut = False
        elif key ==  simplegui.KEY_MAP['e']:
            self.cam.zoomIn = False
        elif key ==  simplegui.KEY_MAP['right']:
            self.cam.moveRight = False

        elif key ==  simplegui.KEY_MAP['left']:
            self.cam.moveLeft = False
        elif key ==  simplegui.KEY_MAP['up']:
            self.cam.moveUp = False
        elif key ==  simplegui.KEY_MAP['down']:
            self.cam.moveDown = False

    def keydown(self,key):
        if key ==  simplegui.KEY_MAP['r']:
            self.cam.zoomOut = True
        elif key ==  simplegui.KEY_MAP['e']:
            self.cam.zoomIn = True
        elif key ==  simplegui.KEY_MAP['right']:
            self.cam.moveRight = True
        elif key ==  simplegui.KEY_MAP['left']:
            self.cam.moveLeft = True
        elif key ==  simplegui.KEY_MAP['up']:
            self.cam.moveUp = True
        elif key ==  simplegui.KEY_MAP['down']:
            self.cam.moveDown = True

    def updateKey(self):
        """"if self.cam.moveRight == True:
            self.car.accelerate()
            self.car.moveForward()
            print(self.car.vel)
        if self.cam.moveLeft == True:
            self.car.accelerate()
            self.car.reverse()
            print(self.car.vel)
        if not self.cam.moveLeft and not self.cam.moveRight:
            self.car.brake()"""
        self.cam.zoom()
        self.cam.move()