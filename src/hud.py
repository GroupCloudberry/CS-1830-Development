class HUD:
    def __init__(self, window):
        self.window = window
        pass

    def draw_score_lives(self, canvas):
        colour = "Teal"
        width = 225
        height = 25
        x, y = self.window.__class__.WIDTH - 75, 0
        canvas.draw_polygon([(x, 0), (x - width, 0), (x - width, height), (x, height)], 1, colour, colour)

    def draw_pause_button(self, canvas):
        colour = "Teal"
        width = 82
        height = 25
        x, y = 75 + ((width - self.window.frame.get_canvas_textwidth("Pause", 18)) / 2), 0
        canvas.draw_polygon([(x, 0), (x + width, 0 ), (x + width, height), (x, height)], 1, colour, colour)
        canvas.draw_text("Pause", (x + 15, 25), 18, "White")

    def draw_canvas(self, canvas):
        self.draw_score_lives(canvas)
        self.draw_pause_button(canvas)
