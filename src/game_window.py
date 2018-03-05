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

    def start(self):
        main_menu = MainMenu(self)
        self.frame.set_draw_handler(main_menu.draw)
        self.frame.start()


if __name__ =="__main__":
    window = GameWindow()
    window.start()
