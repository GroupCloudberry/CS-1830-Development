from death_menu import DeathMenu
from game_interface import GameInterface
from main_menu import MainMenu
from pause_menu import PauseMenu
from story_screen import StoryScreen

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

if simplegui.__name__ == "simpleguitk":
    print("SQLite3 database supported.")
    from scoreboard_sqlite import ScoreBoardSQLite as ScoreBoard
else:
    print("SQLite3 database not supported on CodeSkulptor.")
    from scoreboard import ScoreBoard


class Game:

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.frame = simplegui.create_frame("BerryDrive (CS1830 Group Cloudberry)", Game.WIDTH, Game.HEIGHT)

        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.death_menu = DeathMenu(self)
        self.story_screen = StoryScreen(self)
        self.game_interface = GameInterface(self)
        self.scoreboard = ScoreBoard(self)
        self.options = None  # WIP

    def start(self):
        self.frame.set_draw_handler(self.main_menu.draw_canvas)
        self.frame.start()


if __name__ == "__main__":
    window = Game()
    window.start()

    timer = simplegui.create_timer(50, GameInterface(window).nextFrame)
    timer.start()
