import collections
import math

from keyboard_compat import KeyboardCompat

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class ScoreBoardMenuItems:
    DELETE_ALL = {"index": 0, "label": "Delete all players"}
    MAIN_MENU = {"index": 1, "label": "Back to Main Menu"}
    ITEMS = [DELETE_ALL, MAIN_MENU]
    

class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.selected_menu_item = 1

        self.box_reveal = 0.0  # Floating point for incremental reveal
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)
        self.players_reveal = False  # Instantaneous reveal when True

        self.page = 0
        self.players = []
        self.pages = 1 if len(self.players) == 0 else math.ceil(len(self.players) / 7)

    def draw_title_and_instructions(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 289 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 1, "Black", "Yellow")
        canvas.draw_text("Scoreboard", (box1_x + 20, box1_y + 67), 50, "Black", "sans-serif")
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Use spacebar key to change", (box1_x + box1_width + 30, box1_y + 35), 20,
                         hint_colour, "sans-serif")
        canvas.draw_text("pages", (box1_x + box1_width + 30, box1_y + 35 + 25), 20,
                         hint_colour, "sans-serif")

    def draw_players(self, canvas):
        players_per_page = 7
        players_already_shown = self.page * players_per_page
        players_not_yet_shown = len(self.players) - players_already_shown
        for i in range(min(players_not_yet_shown, players_per_page)):
            index = i + players_already_shown
            canvas.draw_text("{}. {} (high score: {}, lives: {})".format(self.players[index].id, self.players[index].name,
                                self.players[index].high_score, self.players[index].lives),  (125, 212 + (35 * i)), 25,
                             "White" if self.players_reveal else "Black", "sans-serif")

    def draw_page_number(self, canvas):
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Page {}/{}".format(self.page+1, self.pages), (self.window.__class__.WIDTH - 75 -
                            self.window.frame.get_canvas_textwidth("Page {}/{} ".format(self.page+1, self.pages), 20),
                          self.window.__class__.HEIGHT - 75), 20, hint_colour, "sans-serif")

    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in ScoreBoardMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Yellow"
        for index, item in enumerate(ScoreBoardMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    def key_down(self, key):
        print(key)
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.kb_compat.space_key_pressed(key):
            self.page = (self.page + 1) % self.pages
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == ScoreBoardMenuItems.DELETE_ALL["index"]:
                print("SQLite database unsupported in CodeSkulptor.")
            elif self.selected_menu_item == ScoreBoardMenuItems.MAIN_MENU["index"]:
                self.exit()
        elif self.kb_compat.escape_key_pressed(key):
            self.exit()

    def exit(self):
        # New ScoreBoard object created to run the animation and reload data on next load
        self.window.scoreboard = ScoreBoard(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0
        elif not self.players_reveal:
            self.players_reveal = True

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_title_and_instructions(canvas)
        self.draw_players(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.reveal()
