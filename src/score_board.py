import gc
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.selected_item = 0

        self.box_reveal = 0.0

    def key_down(self, key):
        if key == simplegui.KEY_MAP["escape"]:
            self.window.scoreboard = ScoreBoard(self.window)
            self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)
            gc.collect()

    def draw_boxes(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 289 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "White")
        canvas.draw_text("Scoreboard", (box1_x + 20, box1_y + 67), 50, "Black")

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.reveal()
