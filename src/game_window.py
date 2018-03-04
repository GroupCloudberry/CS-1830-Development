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
        self.frame.start()


if __name__ =="__main__":
    window = GameWindow()
    window.start()