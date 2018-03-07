import sys
import collections
from enum import Enum, unique

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class MainMenuItems(Enum):
    START = 0
    OPTIONS = 1
    SCOREBOARD = 2
    EXIT = 3


class MainMenu:
    def __init__(self, window):
        self.selected_menu_item = 0
        self.window = window

    def menu_key_down(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.selected_menu_item = (self.selected_menu_item + 1) % 4
        elif key == simplegui.KEY_MAP['up']:
            self.selected_menu_item = (self.selected_menu_item - 1) % 4
        elif key == simplegui.KEY_MAP['return']:
            if self.selected_menu_item == MainMenuItems.START.value:
                self.window.frame.set_draw_handler(self.window.game_interface.draw)
            elif self.selected_menu_item == MainMenuItems.EXIT.value:
                print("Player exited game.")
                sys.exit()

    def draw(self, canvas):
        self.window.frame.set_keydown_handler(self.menu_key_down)

        menu_items = collections.OrderedDict([(MainMenuItems.START, "White"), (MainMenuItems.SCOREBOARD, "White"),
                                              (MainMenuItems.OPTIONS, "White"), (MainMenuItems.EXIT, "White")])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Orange"

        canvas.draw_text("BerryDrive", (75, 175), 90, "White")
        canvas.draw_text("Start", (75, 375), 40, menu_items[MainMenuItems.START])
        canvas.draw_text("Scoreboard", (75, 425), 40, menu_items[MainMenuItems.SCOREBOARD])
        canvas.draw_text("Options", (75, 475), 40, menu_items[MainMenuItems.OPTIONS])
        canvas.draw_text("Exit", (75, 525), 40, menu_items[MainMenuItems.EXIT])
