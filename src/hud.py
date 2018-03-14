class HUD:
    """
    To implement the HUD, create a new instance of it in GameInterface using hud = HUD(), and then draw it in
    the draw_canvas(self, canvas) method of GameInterface by calling hud.draw_hud(canvas).
    """
    def __init__(self, window, score=0, lives=3):
        self.window = window

        # To update lives and score, assign a new value to the following instance variables
        self.lives = lives
        self.score = score

    def draw_score_lives(self, canvas):
        text_size = 15
        score_colour = "Teal"
        lives_colour= "White"
        width = 190
        height = 25
        x, y = self.window.__class__.WIDTH - 75, 0
        canvas.draw_polygon([(x, 0), (x - width, 0), (x - width, height), (x, height)], 1, score_colour, score_colour)
        canvas.draw_polygon([(x, 0), (x - (width / 2), 0), (x - (width / 2), height), (x, height)], 1, lives_colour, lives_colour)
        canvas.draw_text("Lives: {}".format(self.lives), (x - width + 10, height - 2), text_size, "White")
        canvas.draw_text("Score: {}".format(self.score), (x - (width / 2) + 10, height - 2), text_size, "Teal")

    def draw_pause_button(self, canvas):
        text_size = 15
        colour = "Teal"
        width = 73
        height = 25
        x, y = 75 + ((width - self.window.frame.get_canvas_textwidth("Pause", text_size)) / 2), 0
        canvas.draw_polygon([(x, 0), (x + width, 0 ), (x + width, height), (x, height)], 1, colour, colour)
        canvas.draw_text("Pause", (x + 16, 23), text_size, "White")

    def pause(self):
        self.window.hud = HUD(self.window)
        self.window.frame.set_draw_handler(self.window.pause_menu.draw_canvas)

    def draw_hud(self, canvas):
        self.draw_score_lives(canvas)
        self.draw_pause_button(canvas)

    """
    The following code for the mouse click handler should be moved to GameInterface.
    
    def mouse_down(self, postion):
    if (180) > postion[0] > 75 and 25 > postion[1] > 0:
        self.pause()
    print(postion)
        
    def draw_canvas(self, canvas):
        self.window.frame.set_mouseclick_handler(self.mouse_down)
    """
