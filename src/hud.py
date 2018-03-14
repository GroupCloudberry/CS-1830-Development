class HUD:
    def __init__(self, window):
        self.window = window
        pass

    def draw_score_lives(self, canvas):
        score_colour = "Grey"
        lives_colour= "White"
        width = 220
        height = 25
        x, y = self.window.__class__.WIDTH - 75, 0
        canvas.draw_polygon([(x, 0), (x - width, 0), (x - width, height), (x, height)], 1, score_colour, score_colour)
        canvas.draw_polygon([(x, 0), (x - (width / 2), 0), (x - (width / 2), height), (x, height)], 1, lives_colour, lives_colour)

    def draw_pause_button(self, canvas):
        text_size = 15
        colour = "Grey"
        width = 73
        height = 25
        x, y = 75 + ((width - self.window.frame.get_canvas_textwidth("Pause", text_size)) / 2), 0
        canvas.draw_polygon([(x, 0), (x + width, 0 ), (x + width, height), (x, height)], 1, colour, colour)
        canvas.draw_text("Pause", (x + 16, 23), text_size, "White")

    def mouse_down(self, postion):
        if (180) > postion[0] > 75 and 25 > postion[1] > 0:
            self.pause()
        print(postion)

    def pause(self):
        self.window.hud = HUD(self.window)
        self.window.frame.set_draw_handler(self.window.pause_menu.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_mouseclick_handler(self.mouse_down)
        self.draw_score_lives(canvas)
        self.draw_pause_button(canvas)
