try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class KeyboardMediator:
    """
    Because CodeSkulptor does not support static methods, an instance of KeyboardMediator should be created
    to utilise these methods.
    """

    def down(self, key):
        return key == simplegui.KEY_MAP["down"]

    def up(self, key):
        return key == simplegui.KEY_MAP["up"]

    def left(self, key):
        return key == simplegui.KEY_MAP["left"]

    def right(self, key):
        return key == simplegui.KEY_MAP["right"]

    def space(self, key):
        return key == simplegui.KEY_MAP["space"]

    def enter(self, key):
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["return"] or key == simplegui.KEY_MAP["right"]
        return key == simplegui.KEY_MAP["right"]

    def pause(self, key):
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["escape"] or key == simplegui == simplegui.KEY_MAP["p"]
        return key == simplegui.KEY_MAP["p"]

