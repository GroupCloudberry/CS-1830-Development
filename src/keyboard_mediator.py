try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class KeyboardMediator:
    def __init__(self):
        pass

    def down(self, key):
        return key == simplegui.KEY_MAP["down"]

    def up(self, key):
        return key == simplegui.KEY_MAP["up"]

    def left(self, key):
        return key == simplegui.KEY_MAP["left"]

    def right(self, key):
        return key == simplegui.KEY_MAP["right"]

    def enter(self, key):
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["enter"] or key == simplegui == simplegui.KEY_MAP["right"]
        return key == simplegui.KEY_MAP["right"]

    def pause(self, key):
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["escape"] or key == simplegui == simplegui.KEY_MAP["p"]
        return key == simplegui.KEY_MAP["p"]

