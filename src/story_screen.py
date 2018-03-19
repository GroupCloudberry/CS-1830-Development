from keyboard_compat import KeyboardCompat

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class StoryPage:
    def __init__(self, container1=None, container2=None):
        self.accent_colour = "Teal"
        self.container1 = {"text": "", "image": None} if container1 is None else container1
        self.container2 = {"text": "", "image": None} if container2 is None else container2


class StoryScreenMenuItems:
    NEXT = {"index": 0, "label": "Next [->]"}
    ITEMS = [NEXT]


class StoryScreen:
    """
    Needs *a lot* of refactoring, subject to time constraints.
    """
    def __init__(self, window, pages):
        self.window = window
        self.box_reveal = 0.0
        self.kb_compat = KeyboardCompat()

        # Testing variables to be removed after completion
        self.page = 0
        self.pages = pages
        self.text = ["", ""]
        self.images =[None, None]

        self.text_size = 20
        self.image_size = 150 # Value of 100 would be 100x100
        self.reflow_text()
        self.preload_images()

    def reflow_text(self):
        # Algorithm to reflow overflowing lines of text
        # For each container on this page, split up the container text into words and put them into a list
        containers = [[[word for word in self.pages[self.page].container1["text"].split()]],
                      [[word for word in self.pages[self.page].container2["text"].split()]]]
        container_width = [self.window.__class__.WIDTH - (75 * 2) - (0 if container["image"] is None else self.image_size)
                           for container in [self.pages[self.page].container1, self.pages[self.page].container2]]
        for containers_index, container in enumerate(containers):
            # Iterate through each line in a container
            for lines_index, line in enumerate(container):
                if self.window.frame.get_canvas_textwidth(" ".join(line), self.text_size) > container_width[containers_index]:
                    # Create a new line in that container if overflowing
                    container.append([])
                while self.window.frame.get_canvas_textwidth(" ".join(line), self.text_size) > container_width[containers_index]:
                    container[lines_index + 1].insert(0, line.pop())
            self.text[containers_index] = container

    def preload_images(self):
        for index, container in enumerate([self.pages[self.page].container1, self.pages[self.page].container2]):
            if container["image"] is not None:
                self.images[index] = simplegui.load_image(container["image"])
            else:
                self.images[index] = None

    def draw_boxes(self, canvas):
        bg_colour = "Teal"
        text = "Introduction"
        text_size = 25
        text_colour = "Black"
        width = (self.window.frame.get_canvas_textwidth(text, text_size) + (15 * 2)) * self.box_reveal
        height = 45
        x, y = 75, 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, bg_colour, bg_colour)
        canvas.draw_text(text, (x + 15, y + 37), text_size, text_colour, "sans-serif")

    def draw_text(self, canvas):
        for index, container in enumerate([self.pages[self.page].container1, self.pages[self.page].container2]):
            for line_index, line in enumerate(self.text[index]):
                margin_left = self.image_size if (index + 1) % 2 == 0 and container["image"] is not None else 0
                x_offset = 15 if (index + 1) % 2 == 0 and container["image"] is not None else 0
                container_spacing = 90 + ((self.text_size + 2) * len(self.text[index - 1])) if index > 0 else 0
                canvas.draw_text(line, (75 + margin_left + x_offset, 165 + ((self.text_size + 2) * line_index)
                                        + container_spacing), self.text_size, "White", "sans-serif")

    def draw_images(self, canvas):
        for index, container in enumerate([self.pages[self.page].container1, self.pages[self.page].container2]):
            if self.images[index] is not None:
                container_spacing = 105 + ((self.text_size + 2) * len(self.text[index - 1])) if index > 0 else 0
                x = self.image_size if (index + 1) % 2 == 0 else self.window.__class__.WIDTH - self.image_size
                canvas.draw_image(self.images[index], (self.image_size / 2, self.image_size /2), (self.image_size, self.image_size),
                                  (x, 200 + container_spacing), (self.image_size, self.image_size))

    def draw_menu(self, canvas):
        canvas.draw_text(StoryScreenMenuItems.NEXT["label"], (self.window.__class__.WIDTH - 75 -
               self.window.frame.get_canvas_textwidth(StoryScreenMenuItems.NEXT["label"], 25),
                self.window.__class__.HEIGHT - 75), 25, "Teal", "sans-serif")

    def draw_page_number(self, canvas):
        canvas.draw_text("Page {}/{}".format(self.page + 1, len(self.pages)), (self.window.__class__.WIDTH - 75 -
                        self.window.frame.get_canvas_textwidth("Page {}/{}".format(self.page + 1, len(self.pages)), 13),
                        75 + 30), 13, "Grey", "sans-serif")

    def draw_navigation_hint(self, canvas):
        canvas.draw_text("Press up and down or left and right arrow keys to change page.", (75, self.window.__class__.HEIGHT - 93), 12,
                         "Grey", "sans-serif")
        canvas.draw_text("Or press space bar to skip.", (75, self.window.__class__.HEIGHT - 75), 12,
                         "Grey", "sans-serif")

    def key_down(self, key):
        if self.kb_compat.enter_key_pressed(key) or key == simplegui.KEY_MAP["down"]:
            self.page_down()
        elif key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["up"]:
            self.page_up()
        elif self.kb_compat.escape_key_pressed(key) or key == simplegui.KEY_MAP["space"]:
            self.dismiss()

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1

    def page_up(self):
        self.page = (self.page - 1) % len(self.pages)
        self.reflow_text()
        self.preload_images()

    def page_down(self):
        if self.page + 1 == len(self.pages):
            self.dismiss()
        else:
            self.page = (self.page + 1) % len(self.pages)
            self.reflow_text()
            self.preload_images()

    def dismiss(self):
        self.page = 0
        self.reflow_text()
        self.preload_images()
        self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_text(canvas)
        self.draw_images(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.draw_navigation_hint(canvas)
        self.reveal()
