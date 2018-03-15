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
        self.right_cover_x = Values.canvas_WIDTH / 2


    def draw_canvas(self, canvas):

        #Check if window was just opened and display animation if true
        self.transition_clock.tick()
        if self.left_cover_x > - Values.canvas_WIDTH / 2:
            self.reveal(canvas)
        #Set keyup and down handlers

    #Curtain animation mathod
    def reveal(self, canvas):
        box_colour_left = "Black"
        box_colour_right = "Black"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, Values.canvas_HEIGHT),
                             (self.left_cover_x + Values.canvas_WIDTH / 2, Values.canvas_HEIGHT),
                             (self.left_cover_x + Values.canvas_WIDTH / 2, 0)],
                            1, box_colour_left, box_colour_left)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, Values.canvas_HEIGHT),
                             (self.right_cover_x + Values.canvas_WIDTH / 2, Values.canvas_HEIGHT),
                             (self.right_cover_x + Values.canvas_WIDTH / 2, 0)], 1,
                            box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25