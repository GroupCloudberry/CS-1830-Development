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
    SKIP = {"index": 0, "label": "Skip->"}
    ITEMS = [SKIP]


class StoryScreen:
    def __init__(self, window):
        self.window = window
        self.box_reveal = 0.0

        # Testing variables to be removed after completion
        self.test_page = StoryPage({"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                           "Donec sed lorem in sem elementum pretium at ut eros. "
                                           "Quisque sollicitudin arcu nulla, eu venenatis lorem tristique hendrerit. "
                                           "Nam gravida tincidunt placerat. Sed sed nisl nec orci bibendum condimentum.",
                                   "image": 1},
                                   {"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                            "Donec sed lorem in sem elementum pretium at ut eros. "
                                            "Quisque sollicitudin arcu nulla, eu venenatis lorem tristique hendrerit. "
                                            "Nam gravida tincidunt placerat. Sed sed nisl nec orci bibendum condimentum.",
                                    "image": 1},
                                   )
        self.page = 0
        self.pages = [self.test_page]
        self.text = ["", ""]
        self.images =[None, None]

        self.text_size = 20
        self.image_size = 150 # Value of 100 would be 100x100
        self.reflow_content()

    def reflow_content(self):
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

    def draw_boxes(self, canvas):
        bg_colour = "Teal"
        text = "Welcome"
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
            for line_number, line in enumerate(self.text[index]):
                margin_left = self.image_size if (index + 1) % 2 == 0 else 0
                container_spacing = 30 + ((self.text_size + 2) * len(self.text[index - 1])) if index > 0 else 0
                canvas.draw_text(line, (75 + margin_left, 165 + ((self.text_size + 2) * line_number)
                                        + container_spacing), self.text_size, "White")

    def draw_menu(self, canvas):
        canvas.draw_text(StoryScreenMenuItems.SKIP["label"], (self.window.__class__.WIDTH - 75 -
                            self.window.frame.get_canvas_textwidth(StoryScreenMenuItems.SKIP["label"], 25),
                          self.window.__class__.HEIGHT - 75), 25, "Teal", "sans-serif")

    def draw_page_number(self, canvas):
        canvas.draw_text("Page {}/{}".format(self.page + 1, len(self.pages)), (self.window.__class__.WIDTH - 75 -
                        self.window.frame.get_canvas_textwidth("Page {}/{}".format(self.page + 1, len(self.pages)), 13),
                        75 + 30), 13, "Grey", "sans-serif")

    def key_down(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.dismiss()
        elif key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["space"]:
            if self.page == len(self.pages) - 1:
                self.dismiss()
            else:
                self.page += 1
        elif key == simplegui.KEY_MAP["up"]:
            if not self.page == 0:
                self.page -= 1

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1

    def dismiss(self):
        pass

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_text(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.reveal()
