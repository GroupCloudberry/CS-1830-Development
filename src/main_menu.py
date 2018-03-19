import collections
from keyboard_compat import KeyboardCompat

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

if simplegui.__name__ == "simpleguitk":
    print("SQLite3 database supported.")
    from scoreboard_sqlite import ScoreBoardSQLite as ScoreBoard
else:
    print("SQLite3 database not supported on CodeSkulptor.")
    from scoreboard import ScoreBoard as ScoreBoard

class MainMenuItems:
    START = {"index": 0, "label": "Start"}
    SCOREBOARD = {"index": 1, "label": "Scoreboard"}
    OPTIONS = {"index": 2, "label": "Options"}
    EXIT = {"index": 3, "label": "Exit"}
    ITEMS = [START, SCOREBOARD, OPTIONS, EXIT]


class MainMenu:
    def __init__(self, window):
        self.selected_menu_item = 0
        self.window = window
        self.kb_compat = KeyboardCompat()

        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2
        self.banner_reveal = 0.0

        self.exiting = False

    def draw_banner(self, canvas):
        bg_colour = "Teal"
        text = "BerryDrive"
        text_size = 90
        text_colour = "White"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = self.window.frame.get_canvas_textwidth(text, text_size) + (2 * 25)
        height = 123
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, bg_colour, bg_colour)
        canvas.draw_text(text, (75 + 25, 185), text_size, text_colour, "sans-serif")
        self.draw_banner_cover(canvas, width, height, x, y)

    def draw_banner_cover(self, canvas, width, height, x, y):
        # Covering polygon to facilitate slide-out animation
        canvas.draw_polygon([(x + (width * self.banner_reveal), y),
                             (x + (width * self.banner_reveal), y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    def draw_exit_covers(self, canvas):
        box_colour = "Black"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                                  (self.left_cover_x + self.window.__class__.WIDTH / 2,
                                   self.window.__class__.HEIGHT),
                                  (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                                 1, box_colour, box_colour)
        canvas.draw_polygon([(self.right_cover_x, 0),
                                  (self.right_cover_x, self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2,
                                   self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                                 box_colour, box_colour)

    def draw_launch_covers(self, canvas):
        box_colour = "Teal"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour, box_colour)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour, box_colour)

    # noinspection PyTypeChecker
    def key_down(self, key):
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(MainMenuItems.ITEMS)
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(MainMenuItems.ITEMS)
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == MainMenuItems.START["index"]:
                self.window.frame.set_draw_handler(self.window.story_screen.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.SCOREBOARD["index"]:
                self.window.scoreboard = ScoreBoard(self.window)
                self.window.frame.set_draw_handler(self.window.scoreboard.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.EXIT["index"]:
                print("Player exited game.")
                self.exiting = True

    def reveal(self, canvas):
        self.draw_launch_covers(canvas)
        if self.left_cover_x > -(self.window.__class__.WIDTH / 2):
            self.left_cover_x -= 25
            self.right_cover_x += 25
        elif round(self.banner_reveal, 1) < 1.0:
            self.banner_reveal += 0.1

    def player_exit(self, canvas):
        self.draw_exit_covers(canvas)
        if self.left_cover_x < 0:
            self.left_cover_x += 50
            self.right_cover_x -= 50
        else:
            exit()

    # noinspection PyTypeChecker
    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_banner(canvas)
        menu_items = collections.OrderedDict([(item["index"], "White") for item in MainMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Teal"
        for index, item in enumerate(MainMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75, 375 + (50 * index)), 40, menu_items[item["index"]], "sans-serif")
        self.reveal(canvas)
        if self.exiting:
            self.player_exit(canvas)
