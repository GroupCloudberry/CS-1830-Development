import collections
import math

from game_interface import GameInterface
from player_attributes import PlayerAttributes
from player_data import PlayerData

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class PauseMenuItems:
    RESUME = {"index": 0, "label": "Resume"}
    MAIN_MENU = {"index": 1, "label": "Exit to Main Menu"}
    ITEMS = [RESUME, MAIN_MENU]


class PauseMenu:
    def __init__(self, window):
        self.window = window
        self.selected_menu_item = 0

        self.box_reveal = 0.0  # Floating point for incremental reveal
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)

    def draw_boxes(self, canvas):
        background_colour = "Teal"
        text = "Paused"
        text_size = 50
        text_colour = "White"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = (self.window.frame.get_canvas_textwidth(text, text_size) + (20 * 2))
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, background_colour, background_colour)
        canvas.draw_text(text, (x + 20, y + 67), text_size, text_colour, "sans-serif")

    def draw_box_covers(self, canvas):
        x, y = 75, 75
        width = 600 - (600 * self.box_reveal)
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    # noinspection PyTypeChecker
    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in PauseMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Teal"
        for index, item in enumerate(PauseMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    def key_down(self, key):
        if key == simplegui.KEY_MAP["down"]:
            self.selected_menu_item = (self.selected_menu_item + 1) % len(PauseMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP["up"]:
            self.selected_menu_item = (self.selected_menu_item - 1) % len(PauseMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP["right"]:
            if self.selected_menu_item == PauseMenuItems.RESUME["index"]:
                self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)
            elif self.selected_menu_item == PauseMenuItems.MAIN_MENU["index"]:
                self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def mouse_down(self, position):
        # Go back to main menu when any click detected. Lives and scores automatically reset next time game is started.
        self.window.game_interface = GameInterface(self.window)
        self.exit()

    def reveal(self):
        if round(self.box_reveal, 1) < 1:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def exit(self):
        # New ScoreBoard object created to run the animation again on next load
        self.window.scoreboard = PauseMenu(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.window.frame.set_mouseclick_handler(self.mouse_down)
        self.draw_boxes(canvas)
        self.draw_box_covers(canvas)
        self.draw_menu(canvas)
        self.reveal()
