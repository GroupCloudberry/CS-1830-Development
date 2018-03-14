from keyboard_compat import KeyboardCompat
from car import Car
from vector import Vector

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui

class KeyboardGameInterface:
    def __init__(self, window):
        self.right = False
        self.left = False
        self.space = False
        self.x = False

        self.kb_compat = KeyboardCompat()
        self.window = window

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True
        elif key == simplegui.KEY_MAP['space']:
            self.space = True
        elif key == simplegui.KEY_MAP['x']:
            self.x = True
        elif self.kb_compat.escape_key_pressed(key):
            # Reset the animation on load
            self.window.pause_menu.box_reveal = 0
            self.window.frame.set_draw_handler(self.window.pause_menu.draw_canvas)


    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
        elif key == simplegui.KEY_MAP['space']:
            self.space = False
        elif key == simplegui.KEY_MAP['x']:
            self.x = False