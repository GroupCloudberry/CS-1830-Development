from keyboard_compat import KeyboardCompat

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

class PlayerDetailsForm:

    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()

        self.box_reveal = 0.0
        self.menu_reveal = (self.window.__class__.WIDTH * 2)

        self.player_name = ""

    def draw_boxes(self, canvas):
        background_colour = "Yellow"
        text = "Save Player"
        text_size = 25
        text_colour = "Black"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = (self.window.frame.get_canvas_textwidth(text, text_size) + (20 * 2))
        height = 40
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, background_colour, background_colour)
        canvas.draw_text(text, (x + 20, y + + 35), text_size, text_colour, "sans-serif")

    def draw_box_covers(self, canvas):
        x, y = 75, 75
        width = 600 - (600 * self.box_reveal)
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    def draw_text(self, canvas):
        text1 = "Type your name and then press the right arrow key or Enter to save your progress."
        text2 = "Use the left arrow key or back space to delete the last character or space x3 to clear."
        text_size = 15
        text_colour = "White"
        x, y = x, y = 75, 115
        canvas.draw_text(text1, (x, y + 40), text_size, text_colour, "sans-serif")
        canvas.draw_text(text2, (x, y + 60), text_size, text_colour, "sans-serif")

    def draw_name(self, canvas):
        text = "{}".format(self.player_name)
        text_size = 20
        text_colour = "White"
        x, y = x, y = 105, 210
        canvas.draw_text(text, (x, y), text_size, text_colour, "sans-serif")

    def key_down(self, key):
        if self.kb_compat.enter_key_pressed(key):
            pass
            # Save player
        elif self.kb_compat.backspace_key_pressed(key):
            self.player_name = self.player_name[:len(self.player_name) - 1] if len(self.player_name) >= 1 \
                else ""
        elif key == simplegui.KEY_MAP["space"]:
            if self.player_name[len(self.player_name) - 2:] == "  ":
                self.player_name = ""
            else:
                self.player_name += chr(key)
        elif 90 >= key >= 65 or 57 >= key >= 48:
            if self.player_name[len(self.player_name) - 1:] == " ":
                self.player_name += chr(key).upper()
            elif len(self.player_name):
                self.player_name += chr(key).lower()
            else:
                self.player_name += chr(key)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_text(canvas)
        self.draw_name(canvas)