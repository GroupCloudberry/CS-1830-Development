import collections
import sys

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


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
                                 1, box_colour, box_colour)
        self.canvas.draw_polygon([(self.right_cover_x, 0),
                                  (self.right_cover_x, self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2,
                                   self.window.__class__.HEIGHT),
                                  (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                                 box_colour, box_colour)
        if self.left_cover_x < 0:
            self.left_cover_x += 35
            self.right_cover_x -= 35
        else:
            exit()

    # noinspection PyTypeChecker
    def key_down(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.selected_menu_item = (self.selected_menu_item + 1) % len(MainMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP['up']:
            self.selected_menu_item = (self.selected_menu_item - 1) % len(MainMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP['right']:
            if self.selected_menu_item == MainMenuItems.START["index"]:
                self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.SCOREBOARD["index"]:
                self.window.frame.set_draw_handler(self.window.scoreboard.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.EXIT["index"]:
                print("Player exited game.")
                self.exiting = True

    # noinspection PyTypeChecker
    def draw_canvas(self, canvas):
        if self.canvas is None:
            self.canvas = canvas
        self.window.frame.set_keydown_handler(self.key_down)
        canvas.draw_text("BerryDrive", (75, 175), 90, "White", "sans-serif")
        menu_items = collections.OrderedDict([(item["index"], "White") for item in MainMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Aqua"
        for index, item in enumerate(MainMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75, 375 + (50 * index)), 40, menu_items[item["index"]], "sans-serif")
        # Animation: draw panels from edge when exiting
        if self.exiting:
            self.player_exit()
