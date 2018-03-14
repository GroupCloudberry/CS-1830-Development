import math

from player_attributes_sqlite import PlayerAttributesSQLite
from player_data import PlayerData
from scoreboard import ScoreBoard

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class ScoreBoardMenuItems:
    DELETE_ALL = {"index": 0, "label": "Delete all players"}
    MAIN_MENU = {"index": 1, "label": "Back to Main Menu"}
    ITEMS = [DELETE_ALL, MAIN_MENU]


class ScoreBoardSQLite(ScoreBoard):
    def __init__(self, window):
        super().__init__(window)
        self.players = self.load_players()
        self.pages = 1 if len(self.players) == 0 else math.ceil(len(self.players) / 7)

    @staticmethod
    def load_players():
        db = PlayerData(PlayerData.DATABASE_NAME)
        return [PlayerAttributesSQLite.load(key) for key in db.get_all_ids()]

    # noinspection PyTypeChecker
    def key_down(self, key):
        if self.keyboard.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.keyboard.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.keyboard.space_key_pressed(key):
            self.page = (self.page + 1) % self.pages
        elif self.keyboard.enter_key_pressed(key):
            if self.selected_menu_item == ScoreBoardMenuItems.DELETE_ALL["index"]:
                PlayerAttributesSQLite.delete_all_players()
                self.players = self.load_players()
            elif self.selected_menu_item == ScoreBoardMenuItems.MAIN_MENU["index"]:
                self.exit()

    def exit(self):
        # New ScoreBoard object created to run the animation and reload data on next load
        self.window.scoreboard = ScoreBoardSQLite(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_title_and_instructions(canvas)
        self.draw_players(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.reveal()
