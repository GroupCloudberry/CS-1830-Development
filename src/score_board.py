try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.selected_item = 0
        pass

    def key_down(self, key):
        pass

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
