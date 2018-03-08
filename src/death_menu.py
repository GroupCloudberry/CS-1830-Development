import collections
from enum import Enum, unique
from transition_clock import TransitionClock

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class DeathMenuItems(Enum):
    RESTART = 0
    MAIN_MENU = 1


class DeathMenu:
    def __init__(self, window):
        self.window = window
        self.selected_menu_item = 0

        self.transition_clock = TransitionClock()
        self.box1_reveal = 0.0
        self.box2_reveal = 0.0
        self.menu_reveal = 0.0

    def key_down(self, key):
        if key == simplegui.KEY_MAP["down"]:
            self.selected_menu_item = (self.selected_menu_item + 1) % 2
        elif key == simplegui.KEY_MAP["up"]:
            self.selected_menu_item = (self.selected_menu_item - 1) % 2
        elif key == simplegui.KEY_MAP["return"]:
            if self.selected_menu_item == DeathMenuItems.RESTART.value:
                pass
            elif self.selected_menu_item == DeathMenuItems.MAIN_MENU.value:
                self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def draw_boxes(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 357 * self.box1_reveal
        box1_height = 100
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "Orange")
        canvas.draw_text("You died.", (box1_x + 20, box1_y + 100), 80, "Black")

        box2_x = 75
        box2_y = box1_y + box1_height + 22
        box2_width = 220 * self.box2_reveal
        box2_height = 50
        canvas.draw_polygon([(box2_x, box2_y), (box2_x, box2_y + box2_height),
                             (box2_x + box2_width, box2_y + box2_height),
                             (box2_x + box2_width, box2_y)], 0, "Black", "White")
        canvas.draw_text("Lives Left: 0", (box2_x + 20, box2_y + 47), 35, "Black")

    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(DeathMenuItems.RESTART, "White"), (DeathMenuItems.MAIN_MENU, "White")])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Orange"
        canvas.draw_text("Restart Level", (75, 475), 35, menu_items[DeathMenuItems.RESTART])
        canvas.draw_polygon([(275 * self.menu_reveal, 475), (275 * self.menu_reveal, 475 - 35),
                             (275, 475 - 35), (275, 475)], 0, "Black", "Black")
        canvas.draw_text("Back to Main Menu", (75, 525), 35, menu_items[DeathMenuItems.MAIN_MENU])
        canvas.draw_polygon([(375 * self.menu_reveal, 525), (385 * self.menu_reveal, 525 - 35),
                             (375, 525 - 35), (375, 525)], 0, "Black", "Black")

    def reveal(self):
        if round(self.box1_reveal, 1) < 1.0:
            self.box1_reveal += 0.1
        elif round(self.box2_reveal, 1) < 1.0:
            self.box2_reveal += 0.1
        else:
            if self.transition_clock.transition(30):
                self.menu_reveal = 1.0

    def draw_canvas(self, canvas):
        self.transition_clock.tick()
        self.window.frame.set_keydown_handler(self.key_down)

        self.draw_boxes(canvas)
        self.draw_menu(canvas)
        self.reveal()