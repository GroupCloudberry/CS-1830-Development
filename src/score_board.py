import collections
import math

from player_attributes import PlayerAttributes
from player_data import PlayerData

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class ScoreBoardMenuItems:
    DELETE_ALL = {"index": 0, "label": "Delete all players"}
    MAIN_MENU = {"index": 1, "label": "Back to Main Menu"}
    ITEMS = [DELETE_ALL, MAIN_MENU]
    

class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.selected_menu_item = 1

        self.box_reveal = 0.0  # Floating point for incremental reveal
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)
        self.players_reveal = False  # Instantaneous reveal when True

        self.players = self.load_players()
        self.page = 0
        self.pages = 1 if len(self.players) == 0 else math.ceil(len(self.players) / 7)

    def exit(self):
        # New ScoreBoard object created to run the animation again on next load
        self.window.scoreboard = ScoreBoard(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    # noinspection PyTypeChecker
    def key_down(self, key):
        if key == simplegui.KEY_MAP["escape"]:
            self.exit()
        elif key == simplegui.KEY_MAP["down"]:
            self.selected_menu_item = (self.selected_menu_item + 1) % len(ScoreBoardMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP["up"]:
            self.selected_menu_item = (self.selected_menu_item - 1) % len(ScoreBoardMenuItems.ITEMS)
        elif key == simplegui.KEY_MAP["next"] or key == simplegui.KEY_MAP["right"]:
            self.page = (self.page + 1) % self.pages
        elif key == simplegui.KEY_MAP["prior"] or key == simplegui.KEY_MAP["left"]:
            self.page = (self.page - 1) % self.pages
        elif key == simplegui.KEY_MAP["return"]:
            if self.selected_menu_item == ScoreBoardMenuItems.DELETE_ALL["index"]:
                PlayerAttributes.delete_all_players()
                self.players = self.load_players()
            elif self.selected_menu_item == ScoreBoardMenuItems.MAIN_MENU["index"]:
                self.exit()

    def draw_boxes(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 289 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "Yellow")
        canvas.draw_text("Scoreboard", (box1_x + 20, box1_y + 67), 50, "Black", "sans-serif")
        # Draw instruction labels
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Use Page Up and Page Down keys", (box1_x + box1_width + 30, box1_y + 35), 20,
                         hint_colour, "sans-serif")
        canvas.draw_text("or left and right arrows to browse", (box1_x + box1_width + 30, box1_y + 35 + 25), 20,
                         hint_colour, "sans-serif")

    # noinspection PyTypeChecker
    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in ScoreBoardMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Yellow"
        for index, item in enumerate(ScoreBoardMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    @staticmethod
    def load_players():
        db = PlayerData(PlayerData.DATABASE_NAME)
        return [PlayerAttributes.load(key) for key in db.get_all_ids()]

    def draw_players(self, canvas):
        players_per_page = 7
        players_already_shown = self.page * players_per_page
        players_not_yet_shown = len(self.players) - players_already_shown
        for i in range(min(players_not_yet_shown, players_per_page)):
            index = i + players_already_shown
            canvas.draw_text("{}. {} (score: {})".format(self.players[index].id, self.players[index].name,
                                self.players[index].high_score), (125, 212 + (35 * i)), 25,
                             "White" if self.players_reveal else "Black", "sans-serif")
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Page {}/{}".format(self.page+1, self.pages), (self.window.__class__.WIDTH - 75 -
                            self.window.frame.get_canvas_textwidth("Page {}/{} ".format(self.page+1, self.pages), 20),
                          self.window.__class__.HEIGHT - 75), 20, hint_colour, "sans-serif")

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0
        elif self.players_reveal == False:
            self.players_reveal = True

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_menu(canvas)
        self.draw_players(canvas)
        self.reveal()
