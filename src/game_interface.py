from transition_clock import TransitionClock
from vector import Vector
from values import Values
from road import Road
from car import Car
from keyboard import Keyboard
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

        self.keyboard = Keyboard()
        self.car = Car(Vector(50, 375))
        self.road = Road(0)
        self.interaction = Interaction(self.car, self.keyboard, self.road)


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
        self.road.drawRoad(canvas)



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
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25


class Interaction:
    def __init__(self, car, keyboard, road):
        self.car = car
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            if self.car.position.getX() < Values.canvas_WIDTH*0.2:
                self.car.vel.add(Vector(0.5, 0))
            self.car.rotation = self.car.rotation + 1
        if self.keyboard.left:
            if self.car.position.getX() > 50:
                self.car.vel.add(Vector(-0.5, 0))
            self.car.rotation = self.car.rotation - 1