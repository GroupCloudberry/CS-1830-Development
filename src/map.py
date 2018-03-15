from keyboard_compat import KeyboardCompat

class Map:

    boundaries = {
        # Format: "item_name": [(min_x, max_x), (min_y, max_y)]
        "item1": [(100, 400), (100, 200)],
        "item2": [(100, 500), (400, 500)]
    }

    def __init__(self, window):
        self.window = window
        self.canvas = None
        self.kb_compat = KeyboardCompat()

        self.debug_points = []

    def mouse_down_debug(self, position):
        """
        Draw a green circle if mouse click registered within any defined boundary, or a red circle if otherwise.
        Remember to call self.draw_debug_points(self, canvas) in self.draw_canvas(self, canvas)
        """
        bounds = __class__.boundaries
        for item in bounds:
            if bounds[item][0][1] >= position[0] >= bounds[item][0][0] and\
               bounds[item][1][1] >= position[1] >= bounds[item][1][0]:
                self.debug_points.append((position[0], position[1], "Green"))
                return
        self.debug_points.append((position[0], position[1], "Red"))

    def draw_debug_points(self, canvas):
        for point in self.debug_points:
            self.canvas.draw_circle((point[0], point[1]), 7, 4, point[2])

    def draw_canvas(self, canvas):
        self.canvas = canvas
        self.draw_debug_points(canvas)
        self.window.frame.set_mouseclick_handler(self.mouse_down_debug)