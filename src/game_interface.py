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


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

    def draw_canvas(self, canvas):
        # Increment the clock counter each time a frame is drawn to facilitate time-based functionality
        self.transition_clock.tick()

        canvas.draw_line([0,400], [800,400], "10", 'white')

        # Draw the covers and incrementally reveal the underlying content
        # To cover all elements, the cover needs to be be drawn last
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)

        # Set key up and down handlers

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
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25