try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class StoryPage:
    def __init__(self):
        self.accent_colour = "Teal"
        self.container1_img = None
        self.container2_img = None
        self.container1_text = ""
        self.container2_text = ""


class StoryScreenMenuItems:
    SKIP = {"index": 0, "label": "Skip->"}
    ITEMS = [SKIP]


class StoryScreen:
    def __init__(self, window):
        self.window = window
        self.box_reveal = 0.0

        # Testing variables to be removed after completion
        self.testpage = StoryPage()
        self.testpage.container1_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae odio sit amet metus rutrum accumsan. Aliquam vehicula arcu non arcu hendrerit lobortis. Curabitur eget ante ut est vulputate viverra. Aenean sed nisl rutrum, luctus magna sit amet, semper arcu. Nunc felis mi, cursus vel aliquam at, hendrerit ac libero. Nunc a consequat tortor, id elementum odio. Mauris tempor ipsum in dui iaculis, vel dapibus sem faucibus. In porta consectetur accumsan. Etiam dignissim turpis non nunc consectetur consequat."

        self.page = 0
        self.pages = [self.testpage]
        self.image_box_width = 100
        self.reflow_text()

    def dismiss(self):
        pass

    def key_down(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.dismiss()

    def draw_boxes(self, canvas):
        box1_text = "Welcome"
        box1_text_size = 25
        box1_width = (self.window.frame.get_canvas_textwidth(box1_text, box1_text_size) + (15 * 2)) * self.box_reveal
        box1_height = 45
        box1_x = 75
        box1_y = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 0, "Black", "Teal")
        canvas.draw_text(box1_text, (box1_x + 15, box1_y + 37), box1_text_size, "Black", "sans-serif")

    def draw_menu(self, canvas):
        canvas.draw_text(StoryScreenMenuItems.SKIP["label"], (self.window.__class__.WIDTH - 75 -
                            self.window.frame.get_canvas_textwidth(StoryScreenMenuItems.SKIP["label"], 25),
                          self.window.__class__.HEIGHT - 75), 25, "Teal", "sans-serif")
        canvas.draw_text("Page {}/{}".format(self.page + 1, len(self.pages)), (self.window.__class__.WIDTH - 75 -
                        self.window.frame.get_canvas_textwidth("Page {}/{}".format(self.page + 1, len(self.pages)), 13),
                        75 + 30), 13, "Grey", "sans-serif")

    def reflow_text(self):
        # Algorithm to reflow overflowing lines of text
        overflowing_words = 0
        containers = [[[word for word in self.pages[self.page].container1_text.split()]],
                      [[word for word in self.pages[self.page].container2_text.split()]]]
        container_width = self.window.__class__.WIDTH - (75 * 2) - self.image_box_width
        for container in containers:
            for index, sentence in enumerate(container):
                if self.window.frame.get_canvas_textwidth(" ".join(sentence), 25) > container_width:
                    container.append([])
                while self.window.frame.get_canvas_textwidth(" ".join(sentence), 25) > container_width:
                    container[index + 1].append(sentence.pop())
                    overflowing_words += 1
        print("Reflowed {} words into {} lines.".
              format(str(overflowing_words), sum([len(container) for container in containers])))

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_menu(canvas)
        self.reveal()
