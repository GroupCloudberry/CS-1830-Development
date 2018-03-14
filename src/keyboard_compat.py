try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class KeyboardCompat:
    """
    Compatibility class to implement fallback keys, in the event that a key binding is incompatible
    with the simplegui implementation.

    Because CodeSkulptor does not support static methods, an instance of KeyboardMediator must be created
    to utilise these methods.
    """

    def down_key_pressed(self, key):
        return key == simplegui.KEY_MAP["down"]

    def up_key_pressed(self, key):
        return key == simplegui.KEY_MAP["up"]

    def left_key_pressed(self, key):
        return key == simplegui.KEY_MAP["left"]

    def right_key_pressed(self, key):
        return key == simplegui.KEY_MAP["right"]

    def space_key_pressed(self, key):
        return key == simplegui.KEY_MAP["space"]

    def enter_key_pressed(self, key):
        # Use right arrow key as a fallback, as the Enter key is not supported by CodeSkulptor
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["return"] or key == simplegui.KEY_MAP["right"]
        return key == simplegui.KEY_MAP["right"]

    def escape_key_pressed(self, key):
        # Use lower-case p as a fallback, as the Esc key is not supported by CodeSkulptor
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["escape"] or key == simplegui.KEY_MAP["p"]
        return key == simplegui.KEY_MAP["p"]

