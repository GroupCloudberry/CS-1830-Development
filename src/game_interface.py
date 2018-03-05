try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class GameInterface:
    def __init__(self, window):
        self.window = window

    def draw(self, canvas):
        canvas.draw_text("For actual game content.", (50, 150), 25, "White")
