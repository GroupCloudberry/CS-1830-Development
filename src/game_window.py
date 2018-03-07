from death_menu import DeathMenu
from game_interface import GameInterface
from main_menu import MainMenu
from score_board import ScoreBoard

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class GameWindow:

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.frame = simplegui.create_frame("BerryDrive (CS1830 Group Cloudberry)", GameWindow.WIDTH, GameWindow.HEIGHT)

        self.main_menu = MainMenu(self)
        self.death_menu = DeathMenu(self)
        self.game_interface = GameInterface(self)
        self.scoreboard = ScoreBoard(self)
        self.options = None  # WIP

    def start(self):
        self.frame.set_draw_handler(self.main_menu.draw_canvas)
        self.frame.start()


if __name__ == "__main__":
    window = GameWindow()
    window.start()
