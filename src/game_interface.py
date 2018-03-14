from hud import HUD
from transition_clock import TransitionClock
from vector import Vector
from values import Values
from road import Road
from car import Car
from keyboard_game_interface import KeyboardGameInterface
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
#from SimpleGUICS2Pygame import simplegui_lib_fps


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

        self.keyboard = KeyboardGameInterface(window)
        self.car = Car(Vector(50, 375),100)

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
    def __init__(self, car, keyboard, road):
        self.car = car
        self.keyboard = keyboard

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



