from hud import HUD
from transition_clock import TransitionClock
from vector import Vector
from values import Values
from road import Road
from car import Car
from level_camera import LevelCamera
from keyboard_game_interface import KeyboardGameInterface
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

        self.road = Road()
        self.keyboard = KeyboardGameInterface(window)
        self.car = Car(Vector(50, 375), 100, self.road)
        self.cam = LevelCamera(self.car.position, Values.CAM_ZOOM_SENSITIVITY, Values.CAM_MOVE_SENSITIVITY,
                          Vector(Values.canvas_WIDTH, Values.canvas_HEIGHT))
        self.car.cam = self.cam
        self.interaction = Interaction(self.car, self.keyboard, self.road, self.cam)

<<<<<<< HEAD
        self.road.initSlope()

    def draw_canvas(self, canvas):

        #Check if window was just opened and display animation if true
        self.transition_clock.tick()
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)
        #Set keyup and down handlers
        self.window.frame.set_keydown_handler(self.keyboard.keyDown)
        self.window.frame.set_keyup_handler(self.keyboard.keyUp)

        self.interaction.update()
        self.car.update()
        self.car.drawcar(canvas)
        self.road.draw(canvas,self.cam)
=======
        self.keyboard = KeyboardGameInterface(window)
        self.car = Car(Vector(50, 375),100)

        self.road = Road(0)
        self.interaction = Interaction(self.car, self.keyboard, self.road)
        self.hud = HUD(window)

        # self.fps = simplegui_lib_fps.FPS()
        # self.fps.start()

    def mouse_down(self, position):
        if 180 > position[0] > 75 and 25 > position[1] > 0:
            self.hud.pause()
>>>>>>> cc63b43c917f982e59704a9e1ec86309e837d6ba

    def reveal(self, canvas):
        box_colour_left = "Teal"
        box_colour_right = "Teal"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour_left, box_colour_left)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25

    def draw_canvas(self, canvas):
        self.transition_clock.tick()
        #Set keyup and down handlers
        self.window.frame.set_keydown_handler(self.keyboard.keyDown)
        self.window.frame.set_keyup_handler(self.keyboard.keyUp)
        self.window.frame.set_mouseclick_handler(self.mouse_down)

        self.interaction.update()
        self.car.update()
        self.car.drawcar(canvas)
        self.road.drawRoad(canvas)
        self.hud.draw_hud(canvas) # see hud.py for brief documentation

        # Animated reveal transition
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)

class Interaction:
    def __init__(self, car, keyboard, road, cam):
        self.car = car
        self.keyboard = keyboard
        self.cam = cam
        self.road = road

    def update(self):
        if self.keyboard.right:
            self.car.accelerate()
            self.car.moveForward()
            print(self.car.vel)
        if self.keyboard.left:
            self.car.accelerate()
            self.car.reverse()
            print(self.car.vel)

        if not self.keyboard.left and not self.keyboard.right:
            self.car.brake()
        self.cam.setOrigin(self.car.position)


