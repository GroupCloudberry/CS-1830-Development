import collections
from enum import Enum, unique

from player_attributes import PlayerAttributes
from player_data import PlayerData

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


@unique
class ScoreBoardMenuItems(Enum):
    DELETE_ALL = {"index": 0, "label": "Delete all players"}
    MAIN_MENU = {"index": 1, "label": "Back to Main Menu"}
    

class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.selected_menu_item = 1

        self.box_reveal = 0.0
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)

        self.players = []

    def exit(self):
        # New ScoreBoard object created to run the animation again on next load
        self.window.scoreboard = ScoreBoard(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    # noinspection PyTypeChecker
    def key_down(self, key):
        if key == simplegui.KEY_MAP["escape"]:
            self.exit()
        elif key == simplegui.KEY_MAP["down"]:
            self.selected_menu_item = (self.selected_menu_item + 1) % len(ScoreBoardMenuItems)
        elif key == simplegui.KEY_MAP["up"]:
            self.selected_menu_item = (self.selected_menu_item - 1) % len(ScoreBoardMenuItems)
        elif key == simplegui.KEY_MAP["return"]:
            if self.selected_menu_item == ScoreBoardMenuItems.MAIN_MENU.value["index"]:
                self.exit()

    def draw_boxes(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 289 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "Yellow")
        canvas.draw_text("Scoreboard", (box1_x + 20, box1_y + 67), 50, "Black")

    # noinspection PyTypeChecker
    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item, "White") for item in ScoreBoardMenuItems])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Yellow"
        for index, item in enumerate(ScoreBoardMenuItems):
            canvas.draw_text(item.value["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30, menu_items[item])

    def load_players(self):
        db = PlayerData(PlayerData.DATABASE_NAME)
        for key in db.get_all_ids():
            self.players.append(PlayerAttributes.load(key))

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_menu(canvas)
        self.load_players()
        self.reveal()
