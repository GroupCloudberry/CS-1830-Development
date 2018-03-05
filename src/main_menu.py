import sys, collections
from enum import Enum, unique

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class MenuItems(Enum):
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
            if self.selected_menu_item == MenuItems.START.value:
                self.window.frame.set_draw_handler(self.window.draw_game_interface)
            if self.selected_menu_item == MenuItems.EXIT.value:
                print("Player exited game.")
                sys.exit()

    def draw(self, canvas):
        self.window.frame.set_keydown_handler(self.menu_key_down)

        menu_items = collections.OrderedDict([(MenuItems.START, "White"), (MenuItems.SCOREBOARD, "White"),
                      (MenuItems.OPTIONS, "White"), (MenuItems.EXIT, "White")])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Orange"

        canvas.draw_text("Game Name", (50, 150), 90, "White")
        canvas.draw_text("Start", (50, 300), 40, menu_items[MenuItems.START])
        canvas.draw_text("Scoreboard", (50, 350), 40, menu_items[MenuItems.SCOREBOARD])
        canvas.draw_text("Options", (50, 400), 40, menu_items[MenuItems.OPTIONS])
        canvas.draw_text("Exit", (50, 450), 40, menu_items[MenuItems.EXIT])
