from transition_clock import TransitionClock

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

    def draw(self, canvas):
        self.transition_clock.tick()
        canvas.draw_text("For actual game content.", (50, 150), 25, "White")
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)

    def reveal(self, canvas):
        box_colour_left = "Orange"
        box_colour_right = "Orange"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            0, box_colour_left, box_colour_left)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 0,
                            box_colour_right, box_colour_right)
        self.left_cover_x -= 15
        self.right_cover_x += 15
