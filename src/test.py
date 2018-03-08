import collections
import sys
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
        self.canvas = None

        self.left_cover_x = -(self.window.__class__.WIDTH / 2)
        self.right_cover_x = (self.window.__class__.WIDTH / 2) * 2

        self.exiting = False

    def player_exit(self):
        box_colour = "Black"
        self.canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                                  (self.left_cover_x + self.window.__class__.WIDTH / 2,
                                   self.window.__class__.HEIGHT),
                                  (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                                 0, box_colour, box_colour)
        self.canvas.draw_polygon([(self.right_cover_x, 0),
                                  (self.right_cover_x, self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2,
                                   self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 0,
                                 box_colour, box_colour)
        if self.left_cover_x < 0:
            self.left_cover_x += 35
            self.right_cover_x -= 35
        else:
            sys.exit()

    # noinspection PyTypeChecker
    def draw_canvas(self, canvas):
        if self.canvas is None:
            self.canvas = canvas
        canvas.draw_text("BerryDrive", (75, 175), 90, "White", "sans-serif")
        menu_items = collections.OrderedDict([(item, "White") for item in MainMenuItems])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Aqua"
        for index, item in enumerate(MainMenuItems):
            canvas.draw_text(item.value["label"], (75, 375 + (50 * index)), 40, menu_items[item], "sans-serif")
        # Animation: draw panels from edge when exiting
        if self.exiting:
            self.player_exit()


class GameWindow:
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.frame = simplegui.create_frame("BerryDrive (CS1830 Group Cloudberry)", GameWindow.WIDTH, GameWindow.HEIGHT)

        self.main_menu = MainMenu(self)

    def start(self):
        self.frame.set_draw_handler(self.main_menu.draw_canvas)
        self.frame.start()


if __name__ == "__main__":
    window = GameWindow()
    window.start()