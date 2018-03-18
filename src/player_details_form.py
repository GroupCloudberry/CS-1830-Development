from keyboard_compat import KeyboardCompat
from values import Values

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

if simplegui.__name__ == "simpleguitk":
    from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
else:
    from player_attributes import PlayerAttributes


class PlayerDetailsForm:

    def __init__(self, window, attributes_from_game=None):
        self.window = window
        self.kb_compat = KeyboardCompat()

        self.box_reveal = 0.0
        self.menu_reveal = (Values.canvas_WIDTH * 2)

        self.player_name = ""
        self.attributes_from_game = attributes_from_game if attributes_from_game is not None else None

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
            self.store()
            self.exit()
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

    def reveal(self):
        if round(self.box_reveal, 1) < 1:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def store(self):
        player_attributes = PlayerAttributes.create(self.player_name)
        if self.attributes_from_game is not None:
            attr = self.attributes_from_game
            player_attributes.set_params(level=attr.level, high_score=attr.high_score,
                                              currency=attr.currency, lives=attr.lives)
        player_attributes.close()

    def exit(self):
        if self.attributes_from_game is None:
            self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)
        else:
            self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_box_covers(canvas)
        self.draw_text(canvas)
        self.draw_name(canvas)
        self.reveal()