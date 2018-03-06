from death_menu import DeathMenu
from game_interface import GameInterface
from main_menu import MainMenu

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class GameWindow:

    WIDTH = 700
    HEIGHT = 500

    def __init__(self):
        self.frame = simplegui.create_frame("CS1830 Group Cloudberry", GameWindow.WIDTH, GameWindow.HEIGHT)

        self.main_menu = MainMenu(self)
        self.death_menu = DeathMenu(self)
        self.game_interface = GameInterface(self)

    def start(self):
        self.frame.set_draw_handler(self.main_menu.draw)
        self.frame.start()


if __name__ =="__main__":
    window = GameWindow()
    window.start()
