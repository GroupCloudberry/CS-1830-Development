import collections
import math

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

    def exit(self):
        # New ScoreBoard object created to run the animation again on next load
        self.window.scoreboard = PauseMenu(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    # noinspection PyTypeChecker
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

    def draw_boxes(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 199 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "Teal")
        canvas.draw_text("Paused", (box1_x + 20, box1_y + 67), 50, "Black", "sans-serif")

    # noinspection PyTypeChecker
    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in PauseMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Teal"
        for index, item in enumerate(PauseMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def draw_canvas(self, canvas):
        print(self.window.frame.get_canvas_textwidth("Paused", 50))
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_menu(canvas)
        self.reveal()
