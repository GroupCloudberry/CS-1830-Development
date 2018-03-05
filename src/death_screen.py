import collections
from enum import Enum, unique

from main_menu import MainMenu

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class DeathMenuItems(Enum):
    RESTART = 0
    MAIN_MENU = 1


class Death:
    def __init__(self, window):
        self.window = window
        self.selected_menu_item = 0

    def menu_key_down(self, key):
        if key == simplegui.KEY_MAP["down"]:
            self.selected_menu_item = (self.selected_menu_item + 1) % 2
        elif key == simplegui.KEY_MAP["up"]:
            self.selected_menu_item = (self.selected_menu_item - 1) % 2
        elif key == simplegui.KEY_MAP["return"]:
            if self.selected_menu_item == DeathMenuItems.RESTART.value:
                pass
            elif self.selected_menu_item == DeathMenuItems.MAIN_MENU.value:
                menu = MainMenu(self.window)
                self.window.frame.set_draw_handler(menu.draw)

    def draw(self, canvas):
        self.window.frame.set_keydown_handler(self.menu_key_down)

        box1_x = 50
        box1_y = 50
        box1_width = 357
        box1_height = 100
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Orange", "Orange")
        canvas.draw_text("You died.", (box1_x + 20, box1_y + 100), 80, "Black")

        box2_x = 50
        box2_y = box1_y + box1_height + 22
        box2_width = 220
        box2_height = 50
        canvas.draw_polygon([(box2_x, box2_y), (box2_x, box2_y + box2_height),
                             (box2_x + box2_width, box2_y + box2_height),
                             (box2_x + box2_width, box2_y)], 0, "White", "White")
        canvas.draw_text("Lives Left: 0", (box2_x + 20, box2_y + 47), 35, "Black")

        menu_items = collections.OrderedDict([(DeathMenuItems.RESTART, "White"), (DeathMenuItems.MAIN_MENU, "White")])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Orange"
        canvas.draw_text("Restart Level", (50, 400), 35, menu_items[DeathMenuItems.RESTART])
        canvas.draw_text("Back to Main Menu", (50, 440), 35, menu_items[DeathMenuItems.MAIN_MENU])
