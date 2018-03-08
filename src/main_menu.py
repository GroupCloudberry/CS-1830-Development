import sys
import collections
from enum import Enum, unique

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class MainMenuItems(Enum):
    START = {"index": 0, "label": "Start"}
    SCOREBOARD = {"index": 1, "label": "Scoreboard"}
    OPTIONS = {"index": 2, "label": "Options"}
    EXIT = {"index": 3, "label": "Exit"}


class MainMenu:
    def __init__(self, window):
        self.selected_menu_item = 0
        self.window = window

    # noinspection PyTypeChecker
    def key_down(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.selected_menu_item = (self.selected_menu_item + 1) % len(MainMenuItems)
        elif key == simplegui.KEY_MAP['up']:
            self.selected_menu_item = (self.selected_menu_item - 1) % len(MainMenuItems)
        elif key == simplegui.KEY_MAP['return']:
            if self.selected_menu_item == MainMenuItems.START.value["index"]:
                self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.SCOREBOARD.value["index"]:
                self.window.frame.set_draw_handler(self.window.scoreboard.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.EXIT.value["index"]:
                print("Player exited game.")
                sys.exit()

    # noinspection PyTypeChecker
    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        canvas.draw_text("BerryDrive", (75, 175), 90, "White")
        menu_items = collections.OrderedDict([(item, "White") for item in MainMenuItems])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Aqua"
        for index, item in enumerate(MainMenuItems):
            canvas.draw_text(item.value["label"], (75, 375 + (50 * index)), 40, menu_items[item])
