try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
import random
import math
import time
import collections

tyre_image = simplegui.load_image('https://i.imgur.com/m7e5j6O.png')
car_image = simplegui.load_image('https://i.imgur.com/dtyG7HO.png')
image_link = simplegui.load_image('https://i.imgur.com/ZhPTrBH.jpg')

# berry_image_link = simplegui.load_image('https://i.imgur.com/erLYnGU.png')

berry_image_link = simplegui.load_image('https://i.imgur.com/IPlsY2L.png')

# berry_merchant_image = simplegui.load_image('https://i.imgur.com/iQIBDHX.png')

berry_merchant_image = simplegui.load_image('https://i.imgur.com/78r4LwF.png')

bear_image = simplegui.load_image('https://i.imgur.com/284X6gP.png')
end_of_road_image = simplegui.load_image('https://i.imgur.com/PRF2gZe.png')

# Commented code for audio
# sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')

timer_counter_bm = 0
frame_bm = 0
frame_bear = 0


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
        self.images = [None, None]

        self.text_size = 20
        self.image_size = 150  # Value of 100 would be 100x100
        self.reflow_text()
        self.preload_images()

    def reflow_text(self):
        # Algorithm to reflow overflowing lines of text
        # For each container on this page, split up the container text into words and put them into a list
        containers = [[[word for word in self.pages[self.page].container1["text"].split()]],
                      [[word for word in self.pages[self.page].container2["text"].split()]]]
        container_width = [
            self.window.__class__.WIDTH - (75 * 2) - (0 if container["image"] is None else self.image_size)
            for container in [self.pages[self.page].container1, self.pages[self.page].container2]]
        for containers_index, container in enumerate(containers):
            # Iterate through each line in a container
            for lines_index, line in enumerate(container):
                if self.window.frame.get_canvas_textwidth(" ".join(line), self.text_size) > container_width[
                    containers_index]:
                    # Create a new line in that container if overflowing
                    container.append([])
                while self.window.frame.get_canvas_textwidth(" ".join(line), self.text_size) > container_width[
                    containers_index]:
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
                canvas.draw_text(" ".join(line), (75 + margin_left + x_offset, 165 + ((self.text_size + 2) * line_index)
                                             + container_spacing), self.text_size, "White", "sans-serif")

    def draw_images(self, canvas):
        for index, container in enumerate([self.pages[self.page].container1, self.pages[self.page].container2]):
            if self.images[index] is not None:
                container_spacing = 105 + ((self.text_size + 2) * len(self.text[index - 1])) if index > 0 else 0
                x = self.image_size if (index + 1) % 2 == 0 else self.window.__class__.WIDTH - self.image_size
                canvas.draw_image(self.images[index], (self.image_size / 2, self.image_size / 2),
                                  (self.image_size, self.image_size),
                                  (x, 200 + container_spacing), (self.image_size, self.image_size))

    def draw_menu(self, canvas):
        canvas.draw_text(StoryScreenMenuItems.NEXT["label"], (self.window.__class__.WIDTH - 75 -
                                                              self.window.frame.get_canvas_textwidth(
                                                                  StoryScreenMenuItems.NEXT["label"], 25),
                                                              self.window.__class__.HEIGHT - 75), 25, "Teal",
                         "sans-serif")

    def draw_page_number(self, canvas):
        canvas.draw_text("Page {}/{}".format(self.page + 1, len(self.pages)), (self.window.__class__.WIDTH - 75 -
                                                                               self.window.frame.get_canvas_textwidth(
                                                                                   "Page {}/{}".format(self.page + 1,
                                                                                                       len(self.pages)),
                                                                                   13),
                                                                               75 + 30), 13, "Grey", "sans-serif")

    def draw_navigation_hint(self, canvas):
        canvas.draw_text("Press up and down or left and right arrow keys to change page.",
                         (75, self.window.__class__.HEIGHT - 93), 12,
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
        self.box_reveal = 0.0

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_text(canvas)
        self.draw_images(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.draw_navigation_hint(canvas)
        self.reveal()


class StoryInitialiser:

    def __init__(self, window):
        self.window = window
        self.pages = []

        self.pages.append(StoryPage(
            {
                "text": "Driver: Help the driver collect as many berries as possible so that "
                        "the alien will spare her another day.",
                "image": "https://i.imgur.com/tmWglsb.jpg"
            },
            {
                "text": "Alien: He comes from a planet far away and his only focus in life is eating berries; "
                        "he will spare only those who will provide him with enough berries for at least a day.",
                "image": "https://i.imgur.com/UUIBWmV.png"
            }
        ))
        self.pages.append(StoryPage(
            {
                "text": "Berries: Each berry collected is worth 2 coins while the berry merchants "
                        "carry at at least 10 berries each.",
                "image": "https://i.imgur.com/wmvmRww.jpg"
            },
            {
                "text": "The Bear: Be careful not to let the bear get too close. If the bear catches you, you lose one life!",
                "image": "https://i.imgur.com/MYcG4Nm.jpg"
            }
        ))

        self.story_screen = StoryScreen(self.window, self.pages)


class PlayerDetailsForm:

    def __init__(self, window, attributes_from_game=None):
        self.window = window
        self.kb_compat = KeyboardCompat()

        self.box_reveal = 0.0
        self.menu_reveal = (Values.canvas_WIDTH * 2)

        self.player_name = ""
        self.attributes_from_game = attributes_from_game if attributes_from_game is not None else None

    def draw_boxes(self, canvas):
        background_colour = "Yellow"
        text = "Save Player"
        text_size = 25
        text_colour = "Black"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = (self.window.frame.get_canvas_textwidth(text, text_size) + (20 * 2))
        height = 40
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, background_colour, background_colour)
        canvas.draw_text(text, (x + 20, y + + 35), text_size, text_colour, "sans-serif")

    def draw_box_covers(self, canvas):
        x, y = 75, 75
        width = 600 - (600 * self.box_reveal)
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    def draw_text(self, canvas):
        text1 = "Type your name and then press the right arrow key or Enter to save your progress."
        text2 = "Use the left arrow key or back space to delete the last character or space x3 to clear."
        text_size = 15
        text_colour = "White"
        x, y = x, y = 75, 115
        canvas.draw_text(text1, (x, y + 40), text_size, text_colour, "sans-serif")
        canvas.draw_text(text2, (x, y + 60), text_size, text_colour, "sans-serif")

    def draw_name(self, canvas):
        text = "{}".format(self.player_name)
        text_size = 20
        text_colour = "White"
        x, y = x, y = 105, 210
        canvas.draw_text(text, (x, y), text_size, text_colour, "sans-serif")

    def key_down(self, key):
        if self.kb_compat.enter_key_pressed(key):
            self.store()
            self.exit()
            # Save player
        elif self.kb_compat.backspace_key_pressed(key):
            self.player_name = self.player_name[:len(self.player_name) - 1] if len(self.player_name) >= 1 \
                else ""
        elif key == simplegui.KEY_MAP["space"]:
            if self.player_name[len(self.player_name) - 2:] == "  ":
                self.player_name = ""
            else:
                self.player_name += chr(key)
        elif 90 >= key >= 65 or 57 >= key >= 48:
            if self.player_name[len(self.player_name) - 1:] == " ":
                self.player_name += chr(key).upper()
            elif len(self.player_name):
                self.player_name += chr(key).lower()
            else:
                self.player_name += chr(key)

    def reveal(self):
        if round(self.box_reveal, 1) < 1:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def store(self):
        player_attributes = PlayerAttributes.create(self.player_name)
        if self.attributes_from_game is not None:
            attr = self.attributes_from_game
            player_attributes.set_params(level=attr.level, high_score=attr.high_score,
                                         currency=attr.currency, lives=attr.lives)
        player_attributes.close()

    def exit(self):
        if self.attributes_from_game is None:
            self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)
        else:
            self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_boxes(canvas)
        self.draw_box_covers(canvas)
        self.draw_text(canvas)
        self.draw_name(canvas)
        self.reveal()


class PauseMenuItems:
    RESUME = {"index": 0, "label": "Resume"}
    SAVE_PLAYER = {"index": 1, "label": "Save Player"}
    MAIN_MENU = {"index": 2, "label": "Exit to Main Menu"}
    ITEMS = [RESUME, SAVE_PLAYER, MAIN_MENU]


class PauseMenu:
    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.selected_menu_item = 0

        self.box_reveal = 0.0  # Multiplier for incremental reveal
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)

    def draw_boxes(self, canvas):
        background_colour = "Teal"
        text = "Paused"
        text_size = 50
        text_colour = "White"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = (self.window.frame.get_canvas_textwidth(text, text_size) + (20 * 2))
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, background_colour, background_colour)
        canvas.draw_text(text, (x + 20, y + 67), text_size, text_colour, "sans-serif")

    def draw_box_covers(self, canvas):
        x, y = 75, 75
        width = 600 - (600 * self.box_reveal)
        height = 75
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    # noinspection PyTypeChecker
    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in PauseMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Teal"
        for index, item in enumerate(PauseMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 450 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    def key_down(self, key):
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(PauseMenuItems.ITEMS)
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(PauseMenuItems.ITEMS)
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == PauseMenuItems.RESUME["index"]:
                self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)
            elif self.selected_menu_item == PauseMenuItems.SAVE_PLAYER["index"]:
                self.window.frame.set_draw_handler(self.window.player_details_form.draw_canvas)
            elif self.selected_menu_item == PauseMenuItems.MAIN_MENU["index"]:
                self.exit()
        elif self.kb_compat.escape_key_pressed(key):
            self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)

    def mouse_down(self, position):
        # Go back to main menu when any click detected. Lives and scores automatically reset next time game is started.
        self.exit()

    def reveal(self):
        if round(self.box_reveal, 1) < 1:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0

    def exit(self):
        # New GameInterface object created to restart anew
        self.window.game_interface = GameInterface(self.window)
        self.window.main_menu.banner_reveal = 0.0
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.window.frame.set_mouseclick_handler(self.mouse_down)
        self.draw_boxes(canvas)
        self.draw_box_covers(canvas)
        self.draw_menu(canvas)
        self.reveal()


class DeathMenuItems:
    RESTART = 0
    MAIN_MENU = 1
    ITEMS = [RESTART, MAIN_MENU]


class DeathMenu:
    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.selected_menu_item = 0

        self.transition_clock = TransitionClock()
        self.box1_reveal = 0.0
        self.box2_reveal = 0.0
        self.menu_reveal = 0.0

    def draw_title_banner(self, canvas):
        box_x = 75
        box_y = 75
        box_width = 357 * self.box1_reveal
        box_height = 100
        canvas.draw_polygon([(box_x, box_y), (box_x, box_y + box_height),
                             (box_x + box_width, box_y + box_height),
                             (box_x + box_width, box_y)], 1, "Black", "Orange")
        canvas.draw_text("You died.", (box_x + 20, box_y + 100), 80, "Black", "sans-serif")

    def draw_lives_banner(self, canvas):
        box_x = 75
        box_y = 75 + 100 + 22
        box_width = 220 * self.box2_reveal
        box_height = 50
        canvas.draw_polygon([(box_x, box_y), (box_x, box_y + box_height),
                             (box_x + box_width, box_y + box_height),
                             (box_x + box_width, box_y)], 1, "Black", "White")
        canvas.draw_text("Lives Left: 0", (box_x + 20, box_y + 47), 35, "Black", "sans-serif")

    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(DeathMenuItems.RESTART, "White"), (DeathMenuItems.MAIN_MENU, "White")])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Orange"
        canvas.draw_text("Restart Level", (75, 475), 35, menu_items[DeathMenuItems.RESTART])
        canvas.draw_polygon([(275 * self.menu_reveal, 475), (275 * self.menu_reveal, 475 - 35),
                             (275, 475 - 35), (275, 475)], 1, "Black", "Black", "sans-serif")
        canvas.draw_text("Back to Main Menu", (75, 525), 35, menu_items[DeathMenuItems.MAIN_MENU])
        canvas.draw_polygon([(375 * self.menu_reveal, 525), (385 * self.menu_reveal, 525 - 35),
                             (375, 525 - 35), (375, 525)], 1, "Black", "Black", "sans-serif")

    def key_down(self, key):
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % 2
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % 2
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == DeathMenuItems.RESTART:
                self.window.game_interface = GameInterface(self.window)
                self.window.frame.set_draw_handler(self.window.game_interface.draw_canvas)
            elif self.selected_menu_item == DeathMenuItems.MAIN_MENU:
                self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def reveal(self):
        if round(self.box1_reveal, 1) < 1.0:
            self.box1_reveal += 0.1
        elif round(self.box2_reveal, 1) < 1.0:
            self.box2_reveal += 0.1
        else:
            if self.transition_clock.transition(30):
                self.menu_reveal = 1.0

    def draw_canvas(self, canvas):
        self.transition_clock.tick()
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_title_banner(canvas)
        self.draw_lives_banner(canvas)
        self.draw_menu(canvas)
        self.reveal()


class ScoreBoardMenuItems:
    DELETE_ALL = {"index": 0, "label": "Delete all players"}
    MAIN_MENU = {"index": 1, "label": "Back to Main Menu"}
    ITEMS = [DELETE_ALL, MAIN_MENU]


class ScoreBoard:

    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.selected_menu_item = 1

        self.box_reveal = 0.0  # Floating point for incremental reveal
        self.menu_reveal = -(self.window.__class__.WIDTH * 2)
        self.players_reveal = False  # Instantaneous reveal when True

        self.page = 0
        self.players = []
        self.pages = 1 if len(self.players) == 0 else math.ceil(len(self.players) / 7)

    def draw_title_and_instructions(self, canvas):
        box1_x = 75
        box1_y = 75
        box1_width = 289 * self.box_reveal
        box1_height = 75
        canvas.draw_polygon([(box1_x, box1_y), (box1_x, box1_y + box1_height),
                             (box1_x + box1_width, box1_y + box1_height),
                             (box1_x + box1_width, box1_y)], 1, "Black", "Yellow")
        canvas.draw_text("Scoreboard", (box1_x + 20, box1_y + 67), 50, "Black", "sans-serif")
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Use spacebar key to change", (box1_x + box1_width + 30, box1_y + 35), 20,
                         hint_colour, "sans-serif")
        canvas.draw_text("pages", (box1_x + box1_width + 30, box1_y + 35 + 25), 20,
                         hint_colour, "sans-serif")

    def draw_players(self, canvas):
        players_per_page = 7
        players_already_shown = self.page * players_per_page
        players_not_yet_shown = len(self.players) - players_already_shown
        for i in range(min(players_not_yet_shown, players_per_page)):
            index = i + players_already_shown
            canvas.draw_text(
                "{}. {} (high score: {}, lives: {})".format(self.players[index].id, self.players[index].name,
                                                            self.players[index].high_score, self.players[index].lives),
                (125, 212 + (35 * i)), 25,
                "White" if self.players_reveal else "Black", "sans-serif")

    def draw_page_number(self, canvas):
        hint_colour = "White" if self.menu_reveal == 0 else "Black"
        canvas.draw_text("Page {}/{}".format(self.page + 1, self.pages), (self.window.__class__.WIDTH - 75 -
                                                                          self.window.frame.get_canvas_textwidth(
                                                                              "Page {}/{} ".format(self.page + 1,
                                                                                                   self.pages), 20),
                                                                          self.window.__class__.HEIGHT - 75), 20,
                         hint_colour, "sans-serif")

    def draw_menu(self, canvas):
        menu_items = collections.OrderedDict([(item["index"], "White") for item in ScoreBoardMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Yellow"
        for index, item in enumerate(ScoreBoardMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75 - self.menu_reveal, 480 + (42 * index)), 30,
                             menu_items[item["index"]], "sans-serif")

    def key_down(self, key):
        print(key)
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(ScoreBoardMenuItems.ITEMS)
        elif self.kb_compat.space_key_pressed(key):
            self.page = (self.page + 1) % self.pages
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == ScoreBoardMenuItems.DELETE_ALL["index"]:
                print("SQLite database unsupported in CodeSkulptor.")
            elif self.selected_menu_item == ScoreBoardMenuItems.MAIN_MENU["index"]:
                self.exit()
        elif self.kb_compat.escape_key_pressed(key):
            self.exit()

    def exit(self):
        # New ScoreBoard object created to run the animation and reload data on next load
        self.window.scoreboard = ScoreBoard(self.window)
        self.window.frame.set_draw_handler(self.window.main_menu.draw_canvas)

    def reveal(self):
        if round(self.box_reveal, 1) < 1.0:
            self.box_reveal += 0.1
        elif self.menu_reveal < 0:
            self.menu_reveal = 0
        elif not self.players_reveal:
            self.players_reveal = True

    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_title_and_instructions(canvas)
        self.draw_players(canvas)
        self.draw_menu(canvas)
        self.draw_page_number(canvas)
        self.reveal()


class MainMenuItems:
    START = {"index": 0, "label": "Start"}
    SCOREBOARD = {"index": 1, "label": "Scoreboard"}
    OPTIONS = {"index": 2, "label": "Options"}
    EXIT = {"index": 3, "label": "Exit"}
    ITEMS = [START, SCOREBOARD, OPTIONS, EXIT]


class MainMenu:
    def __init__(self, window):
        self.selected_menu_item = 0
        self.window = window
        self.kb_compat = KeyboardCompat()

        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2
        self.banner_reveal = 0.0

        self.exiting = False

    def draw_banner(self, canvas):
        bg_colour = "Teal"
        text = "BerryDrive"
        text_size = 90
        text_colour = "White"
        x, y = 75, 75
        # Automatically calculate width of the banner to account for differing fonts in various environments
        width = self.window.frame.get_canvas_textwidth(text, text_size) + (2 * 25)
        height = 123
        canvas.draw_polygon([(x, y), (x, y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, bg_colour, bg_colour)
        canvas.draw_text(text, (75 + 25, 185), text_size, text_colour, "sans-serif")
        self.draw_banner_cover(canvas, width, height, x, y)

    def draw_banner_cover(self, canvas, width, height, x, y):
        # Covering polygon to facilitate slide-out animation
        canvas.draw_polygon([(x + (width * self.banner_reveal), y),
                             (x + (width * self.banner_reveal), y + height),
                             (x + width, y + height),
                             (x + width, y)], 1, "Black", "Black")

    def draw_exit_covers(self, canvas):
        box_colour = "Black"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2,
                              self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour, box_colour)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2,
                              self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour, box_colour)

    def draw_launch_covers(self, canvas):
        box_colour = "Teal"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour, box_colour)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)], 1,
                            box_colour, box_colour)

    # noinspection PyTypeChecker
    def key_down(self, key):
        if self.kb_compat.down_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item + 1) % len(MainMenuItems.ITEMS)
        elif self.kb_compat.up_key_pressed(key):
            self.selected_menu_item = (self.selected_menu_item - 1) % len(MainMenuItems.ITEMS)
        elif self.kb_compat.enter_key_pressed(key):
            if self.selected_menu_item == MainMenuItems.START["index"]:
                self.window.game_interface = GameInterface(self.window)
                self.window.frame.set_draw_handler(self.window.story_screen.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.SCOREBOARD["index"]:
                self.window.scoreboard = ScoreBoard(self.window)
                self.window.frame.set_draw_handler(self.window.scoreboard.draw_canvas)
            elif self.selected_menu_item == MainMenuItems.EXIT["index"]:
                print("Player exited game.")
                self.exiting = True

    def reveal(self, canvas):
        self.draw_launch_covers(canvas)
        if self.left_cover_x > -(self.window.__class__.WIDTH / 2):
            self.left_cover_x -= 25
            self.right_cover_x += 25
        elif round(self.banner_reveal, 1) < 1.0:
            self.banner_reveal += 0.1

    def player_exit(self, canvas):
        self.draw_exit_covers(canvas)
        if self.left_cover_x < 0:
            self.left_cover_x += 50
            self.right_cover_x -= 50
        else:
            exit()

    # noinspection PyTypeChecker
    def draw_canvas(self, canvas):
        self.window.frame.set_keydown_handler(self.key_down)
        self.draw_banner(canvas)
        menu_items = collections.OrderedDict([(item["index"], "White") for item in MainMenuItems.ITEMS])
        menu_items[list(menu_items.keys())[self.selected_menu_item]] = "Teal"
        for index, item in enumerate(MainMenuItems.ITEMS):
            canvas.draw_text(item["label"], (75, 375 + (50 * index)), 40, menu_items[item["index"]], "sans-serif")
        self.reveal(canvas)
        if self.exiting:
            self.player_exit(canvas)


class PlayerAttributes:
    """
    The PlayerAttributes object is used to store the properties of Player instance.
    Each Player object has its own PlayerAttributes instance, with its own methods to modulate parameters
    of that instance.

    To set a new value for any of the parameters, you can either directly assign the appropriate instance
    variable a new value, or use the set_params(self, name=None, level=None, high_score=None, currency=None, lives=None)
    method, specifying the relevant parameters.

    Note that you should not import this class directly.
    The PlayerAttributes class only should be used for instances where the simplegui import refers to the simplegui
    module. This is because Codeskulptor does not support SQLite3. PlayerSQLite should be used wherever the simplegui
    import refers to the simpleguitk module, in order to support database functionality.

    To make imports easier, use the following snippet:
    if simplegui.__name__ == "simpleguitk":
        from player_sqlite import PlayerSQLite as Player
        from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
    else:
        from player import Player
        from player_attributes import PlayerAttributes
    """

    DEFAULT_LEVEL = 1
    DEFAULT_SCORE = 0
    DEFAULT_CURRENCY = 0
    DEFAULT_LIVES = 3

    def __init__(self):
        self.name = None
        self.level = PlayerAttributes.DEFAULT_LEVEL
        self.high_score = PlayerAttributes.DEFAULT_SCORE
        self.currency = PlayerAttributes.DEFAULT_CURRENCY
        self.lives = PlayerAttributes.DEFAULT_LIVES

    def set_params(self, name=None, level=None, high_score=None, currency=None, lives=None):
        self.name = name
        self.level = level
        self.high_score = high_score
        self.currency = currency
        self.lives = lives

    """
    @staticmethod  
    def create(name):
        attr = PlayerAttributes()
        attr.set_params(name, PlayerAttributes.DEFAULT_LEVEL, PlayerAttributes.DEFAULT_SCORE,
                        PlayerAttributes.DEFAULT_CURRENCY, PlayerAttributes.DEFAULT_LIVES)
        return attr
    """


class Player:
    """
    The Player object represents the player sprite and provides a means of manipulating player
    attributes, using an instance of the PlayerAttributes object to store them.

    The fields name, level, high_score, currency, and lives are available as instance variables
    of PlayerAttributes. They can be updated by assigning a new value to them.

    Note that you should not import this class directly.
    The Player class only should be used for instances where the simplegui import refers to the simplegui module.
    This is because Codeskulptor does not support SQLite3. PlayerSQLite should be used wherever the simplegui import
    refers to the simpleguitk module, in order to support database functionality.

    To make imports easier, use the following snippet:
    if simplegui.__name__ == "simpleguitk":
        from player_sqlite import PlayerSQLite as Player
        from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
    else:
        from player import Player
        from player_attributes import PlayerAttributes
    """

    def __init__(self, attributes):
        """
        To create a new player, create a PlayerAttributes object using
        PlayerAttributes.create(name) and pass it onto this
        constructor as the attributes parameter.
        """
        self.current_score = 0
        self.attributes = attributes

    def rename(self, name):
        self.attributes.name = name

    def level_up(self):
        self.attributes.level += 1

    def high_score(self):
        if self.current_score > self.attributes.high_score:
            self.attributes.high_score = self.current_score
            return True
        return False

    def spend_money(self, amount):
        self.attributes.currency -= amount

    def receive_money(self, amount):
        self.attributes.currency += amount

    def lose_life(self):
        self.attributes.lives -= 1

    def gain_life(self, lives=1):
        self.attributes.lives += lives


class MoveObjects:
    def __init__(self, center, canvas_DIM):

        self.center = center
        self.DIM = canvas_DIM
        self.canvas_DIM = canvas_DIM.copy()
        self.moveLeft = False
        self.moveRight = False
        self.speed = 5

    def setCenter(self, carposition):
        self.center = carposition

    def move_left(self):
        self.center.add(Vector(-self.speed, 0))

    def move_right(self):
        self.center.add(Vector(self.speed, 0))

    def move(self, leftEnd, rightEnd):
        if self.moveLeft == True and not leftEnd:
            self.move_left()

        if self.moveRight == True and not rightEnd:
            self.move_right()

    def setSpeed(self, speed):
        self.speed = speed


class Values:
    tyre_sprite = 'https://i.imgur.com/phbmuSj.png'
    level_1_background = 'https://imgur.com/a/DiyAY'

    canvas_WIDTH = 800
    canvas_HEIGHT = 600


class HUD:
    """
    To implement the HUD, create a new instance of it in GameInterface using hud = HUD(), and then draw it in
    the draw_canvas(self, canvas) method of GameInterface by calling hud.draw_hud(canvas).
    """

    def __init__(self, window, score=0, lives=3, fuel=100):
        self.window = window

        # To update lives and score, assign a new value to the following instance variables
        self.lives = lives
        self.score = score
        self.fuel = fuel

    def draw_score_lives(self, canvas):
        text_size = 15
        score_colour = "Teal"
        lives_colour = "White"
        width = 190
        height = 25
        x, y = self.window.__class__.WIDTH - 75, 0
        canvas.draw_polygon([(x, 0), (x - width, 0), (x - width, height), (x, height)], 1, score_colour, score_colour)
        canvas.draw_polygon([(x, 0), (x - (width / 2), 0), (x - (width / 2), height), (x, height)], 1, lives_colour,
                            lives_colour)
        canvas.draw_text("Lives: {}".format(self.lives), (x - width + 10, height - 2), text_size, "White", "sans-serif")
        canvas.draw_text("Score: {}".format(self.score), (x - (width / 2) + 10, height - 2), text_size, "Teal",
                         "sans-serif")

    def draw_pause_button(self, canvas):
        text_size = 15
        colour = "Teal"
        width = 73
        height = 25
        x, y = 75 + ((width - self.window.frame.get_canvas_textwidth("Pause", text_size)) / 2), 0
        canvas.draw_polygon([(x, 0), (x + width, 0), (x + width, height), (x, height)], 1, colour, colour)
        canvas.draw_text("Pause", (x + 16, 23), text_size, "White", "sans-serif")

    def draw_fuel(self, canvas):
        text_size = 15
        colour = "White"
        width = self.window.frame.get_canvas_textwidth("Fuel: {}".format(self.fuel), text_size) + 30
        height = 25
        box_y = self.window.__class__.HEIGHT - height
        x, y = 75 + 15, self.window.__class__.HEIGHT
        canvas.draw_polygon([(75, box_y), (75, box_y + height), (75 + width, box_y + height), (75 + width, box_y)], 1,
                            colour, colour)
        canvas.draw_text("Fuel: {}".format(self.fuel), (x, y), text_size, "Teal", "sans-serif")

    def pause(self):
        self.window.hud = HUD(self.window)
        self.window.frame.set_draw_handler(self.window.pause_menu.draw_canvas)

    def draw_hud(self, canvas):
        self.draw_score_lives(canvas)
        self.draw_pause_button(canvas)
        self.draw_fuel(canvas)

    def update_attributes(self, score, lives, fuel):
        self.score = score
        self.lives = lives


class TransitionClock:

    def __init__(self):
        self.clock = 0

    def tick(self):
        self.clock += 1

    def transition(self, frame_duration):
        return self.clock % frame_duration == 0


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

    def backspace_key_pressed(self, key):
        # Use left arrow key as a fallback, as the backspace key is not supported by CodeSkulptor
        if simplegui.__name__ == "simpleguitk":
            return key == simplegui.KEY_MAP["backspace"] or key == simplegui.KEY_MAP["left"]
        return key == simplegui.KEY_MAP["left"]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def getP(self):
        return (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def copy(self):
        v = Vector(self.x, self.y)
        return v

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def divide(self, k):
        self.x /= k
        self.y /= k
        return self

    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def multiplyVector(self, other):
        self.x *= other.x
        self.y *= other.y
        return self.y

    def divideVector(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def toBackground(self, mover):
        self.subtract(mover.center)
        ratio = mover.canvas_DIM.copy().divideVector(mover.DIM)
        self.multiplyVector(ratio)
        self.add(mover.canvas_DIM.copy().divide(2))
        return self


class GamePlay:

    def __init__(self, mover, game_interface):

        # Road
        self.pointsList = list()
        self.endOfRoad_Origin = Vector(Values.canvas_WIDTH / 2, Values.canvas_HEIGHT / 2).copy().toBackground(mover)

        self.roadLength = 10000
        self.endOfRoadRight_Origin = Vector(10000 - (Values.canvas_WIDTH / 2),
                                            Values.canvas_HEIGHT / 2).copy().toBackground(mover)

        self.point1_pos = Vector()
        self.point2_pos = Vector()

        self.point1_front = Vector()
        self.point2_front = Vector()
        self.point1_t2 = Vector()
        self.point2_t2 = Vector()

        self.point1_bear = Vector()
        self.point2_bear = Vector()

        self.position = Vector(500, 100)
        # Mechanics
        self.acceleration = Vector()
        self.prevTime = time.time()

        # Tyre Vectors
        self.front_tyre = Vector(self.position.getX() + 90, self.position.getY())

        self.tyre_radius = 15

        self.fuel = 100
        self.distancePerLitre = 100
        self.fuelDistance = self.fuel * self.distancePerLitre

        self.berryMoney = 0

        # constants
        self.gravity_vector = Vector(0, 2)
        self.gravity_vector_up = Vector(0, 3)
        self.movement_vector = Vector(5, 0)

        self.carTyreDistance = 80

        self.berry1_pos = self.placeBerries(900, 2000, 0)
        self.berry1_dim = Vector(40, 30)
        self.berry1_draw_boolean = True
        self.berry2_pos = self.placeBerries(8000, 10000, 0)
        self.berry2_dim = Vector(40, 30)
        self.berry2_draw_boolean = True

        self.berryMerchant1_draw_boolean = True
        self.berryMerchant1_pos = Vector(2000, 400)
        self.berryMerchant1_dim = Vector(151, 122)

        self.bm1_pos = Vector(1400, 375)
        self.bm1_dim = Vector(260 / 3, 60)
        self.bm1_draw_boolean = True

        self.mover = mover

        self.rotation = 0
        self.car_rotation = 0

        self.gameInterface = game_interface
        self.score = 0

        # Boolean
        self.car_in_motion = False

        self.bear_pos = Vector(1800, 400)
        self.bear_dim = Vector(70, 70)

        self.blockCar = False

        self.bear_distance = 200

        self.level_completed = False

    # Road for level 1
    def createLevel1(self):
        negativeRoad = Vector(-50, 400)

        startingPoint = Vector(0, 400)
        straightlineEnd = Vector(300, 400)
        slope1End = Vector(600, 300)
        slope2End = Vector(900, 400)
        straightLine3end = Vector(2000, 400)
        slope4end = Vector(2400, 300)
        slope5end = Vector(2800, 300)
        straight6end = Vector(3500, 300)
        slope7end = Vector(4000, 400)
        straight8end = Vector(6000, 400)
        slope9end = Vector(6500, 200)
        slope10end = Vector(7000, 400)
        straight11end = Vector(8000, 400)
        slope12end = Vector(10000, 400)

        self.pointsList.append(negativeRoad)
        self.pointsList.append(startingPoint)
        self.pointsList.append(straightlineEnd)
        self.pointsList.append(slope1End)
        self.pointsList.append(slope2End)
        self.pointsList.append(straightLine3end)
        self.pointsList.append(slope4end)
        self.pointsList.append(slope5end)
        self.pointsList.append(straight6end)
        self.pointsList.append(slope7end)
        self.pointsList.append(straight8end)
        self.pointsList.append(slope9end)
        self.pointsList.append(slope10end)
        self.pointsList.append(straight11end)
        self.pointsList.append(slope12end)

        print(len(self.pointsList))

    def createLevel2(self):
        self.pointsList.append(Vector(-50, 400))
        self.pointsList.append(Vector(0, 400))
        self.pointsList.append(Vector(700, 400))
        self.pointsList.append(Vector(700, 250))
        self.pointsList.append(Vector(1100, 350))
        self.pointsList.append(Vector(1500, 350))
        self.pointsList.append(Vector(1600, 400))
        self.pointsList.append(Vector(2000, 400))
        self.pointsList.append(Vector(2300, 200))
        self.pointsList.append(Vector(2700, 400))
        self.pointsList.append(Vector(3200, 400))
        self.pointsList.append(Vector(3400, 250))
        self.pointsList.append(Vector(3800, 400))
        self.pointsList.append(Vector(4500, 400))
        self.pointsList.append(Vector(5000, 200))
        self.pointsList.append(Vector(5350, 400))
        self.pointsList.append(Vector(6000, 400))
        self.pointsList.append(Vector(7500, 400))
        self.pointsList.append(Vector(8000, 200))
        self.pointsList.append(Vector(8300, 400))
        self.pointsList.append(Vector(8500, 400))
        self.pointsList.append(Vector(9000, 200))
        self.pointsList.append(Vector(9400, 400))
        self.pointsList.append(Vector(10000, 400))

    def createLevel3(self):
        self.pointsList.append(Vector(-50, 400))
        self.pointsList.append(Vector(0, 400))
        self.pointsList.append(Vector(300, 300))
        self.pointsList.append(Vector(600, 300))
        self.pointsList.append(Vector(800, 200))
        self.pointsList.append(Vector(1000, 350))
        self.pointsList.append(Vector(1100, 400))
        self.pointsList.append(Vector(1300, 400))
        self.pointsList.append(Vector(1600, 200))
        self.pointsList.append(Vector(2000, 400))
        self.pointsList.append(Vector(2300, 400))
        self.pointsList.append(Vector(2500, 400))
        self.pointsList.append(Vector(2700, 300))
        self.pointsList.append(Vector(3000, 500))
        self.pointsList.append(Vector(3500, 500))
        self.pointsList.append(Vector(3700, 300))
        self.pointsList.append(Vector(4000, 400))
        self.pointsList.append(Vector(5000, 400))
        self.pointsList.append(Vector(5500, 500))
        self.pointsList.append(Vector(6000, 500))
        self.pointsList.append(Vector(6300, 400))
        self.pointsList.append(Vector(7000, 200))
        self.pointsList.append(Vector(7500, 400))
        self.pointsList.append(Vector(8500, 400))
        self.pointsList.append(Vector(9000, 200))
        self.pointsList.append(Vector(9500, 400))
        self.pointsList.append(Vector(10000, 400))

    def createLevel4(self):
        self.pointsList.append(Vector(-50, 400))
        self.pointsList.append(Vector(0, 400))
        self.pointsList.append(Vector(600, 400))
        self.pointsList.append(Vector(800, 300))
        self.pointsList.append(Vector(1100, 500))
        self.pointsList.append(Vector(1400, 400))
        self.pointsList.append(Vector(2000, 400))
        self.pointsList.append(Vector(2300, 200))
        self.pointsList.append(Vector(2600, 400))
        self.pointsList.append(Vector(3000, 400))
        self.pointsList.append(Vector(3200, 200))
        self.pointsList.append(Vector(3500, 400))
        self.pointsList.append(Vector(4000, 500))
        self.pointsList.append(Vector(4300, 300))
        self.pointsList.append(Vector(4500, 400))
        self.pointsList.append(Vector(5000, 400))
        self.pointsList.append(Vector(5400, 200))
        self.pointsList.append(Vector(5700, 400))
        self.pointsList.append(Vector(6400, 400))
        self.pointsList.append(Vector(6500, 300))
        self.pointsList.append(Vector(6700, 400))
        self.pointsList.append(Vector(7000, 400))
        self.pointsList.append(Vector(7700, 200))
        self.pointsList.append(Vector(8100, 500))
        self.pointsList.append(Vector(8200, 400))
        self.pointsList.append(Vector(8700, 400))
        self.pointsList.append(Vector(9100, 400))
        self.pointsList.append(Vector(9300, 300))
        self.pointsList.append(Vector(9600, 400))
        self.pointsList.append(Vector(10000, 400))

    def createLevel5(self):
        self.pointsList.append(Vector(-50, 400))
        self.pointsList.append(Vector(0, 400))
        self.pointsList.append(Vector(600, 400))
        self.pointsList.append(Vector(700, 200))
        self.pointsList.append(Vector(900, 400))
        self.pointsList.append(Vector(1200, 300))
        self.pointsList.append(Vector(1400, 400))
        self.pointsList.append(Vector(2000, 400))
        self.pointsList.append(Vector(2200, 200))
        self.pointsList.append(Vector(2600, 500))
        self.pointsList.append(Vector(2800, 400))
        self.pointsList.append(Vector(3000, 400))
        self.pointsList.append(Vector(3500, 300))
        self.pointsList.append(Vector(3900, 500))
        self.pointsList.append(Vector(4200, 400))
        self.pointsList.append(Vector(4500, 400))
        self.pointsList.append(Vector(5000, 400))
        self.pointsList.append(Vector(5400, 200))
        self.pointsList.append(Vector(5700, 400))
        self.pointsList.append(Vector(6400, 400))
        self.pointsList.append(Vector(6500, 300))
        self.pointsList.append(Vector(6700, 400))
        self.pointsList.append(Vector(7000, 300))
        self.pointsList.append(Vector(7500, 500))
        self.pointsList.append(Vector(7700, 400))
        self.pointsList.append(Vector(7900, 300))
        self.pointsList.append(Vector(8200, 400))
        self.pointsList.append(Vector(8500, 400))
        self.pointsList.append(Vector(9000, 200))
        self.pointsList.append(Vector(9300, 400))
        self.pointsList.append(Vector(9500, 500))
        self.pointsList.append(Vector(9700, 400))
        self.pointsList.append(Vector(10000, 400))

    # Returns point list
    def getPointsList(self):
        return self.pointsList

    def constructCar(self, canvas, mover):
        self.rotateCar()
        canvas.draw_image(car_image, (521 / 2, 131 / 2), (521, 131), Vector((self.front_tyre.getX() - 43), (
                (self.front_tyre.getY() + self.position.getY()) / 2) - 15).copy().toBackground(mover).getP(),
                          (150, 50), self.car_rotation)
        canvas.draw_image(tyre_image, (200 / 2, 200 / 2), (200, 200), self.position.copy().toBackground(mover).getP(),
                          (self.tyre_radius * 2, self.tyre_radius * 2), self.rotation)
        canvas.draw_image(tyre_image, (200 / 2, 200 / 2), (200, 200), self.front_tyre.copy().toBackground(mover).getP(),
                          (self.tyre_radius * 2, self.tyre_radius * 2), self.rotation)

        self.updateTyres()
        self.applyGravity()

    def updateTyres(self):
        self.front_tyre.setX(self.position.getX() + 90)

    def accelerate(self):
        if self.acceleration.getX() < 100:
            self.acceleration.add(Vector(3, 0))

    def decelerate(self):
        if self.acceleration.getX() > 0:
            self.acceleration.subtract(Vector(10, 0))

    def moveCarRight(self):
        newspeed = self.movement_vector.getX() + self.acceleration.getX() / 10
        self.position.add(Vector(newspeed, self.movement_vector.getY()))
        self.rotation += 0.5
        self.useFuel()
        self.accelerate()
        self.mover.setSpeed(newspeed)
        self.updateTyres()

    def moveCarLeft(self):
        newspeed = self.movement_vector.getX() + self.acceleration.getX() / 10
        self.position.subtract(Vector(newspeed, self.movement_vector.getY()))
        self.rotation += -0.5
        self.useFuel()
        self.accelerate()
        self.mover.setSpeed(newspeed)
        self.updateTyres()

    def findRoadPoints(self, currentX):
        for i in range(len(self.pointsList) - 1):
            if self.pointsList[i].getX() <= currentX:
                self.point1_pos = self.pointsList[i]
                self.point2_pos = self.pointsList[i + 1]
            if self.pointsList[i].getX() <= self.front_tyre.getX():
                self.point1_front = self.pointsList[i]
                self.point2_front = self.pointsList[i + 1]
            if self.pointsList[i].getX() <= self.bear_pos.getX():
                self.point1_bear = self.pointsList[i]
                self.point2_bear = self.pointsList[i + 1]

    def applyGravity(self):
        self.findRoadPoints(self.position.getX())

        roadY = self.getRoadHeight(self.point1_pos, self.point2_pos, self.position.getX())
        if self.position.getY() <= roadY - self.tyre_radius:
            gravityVec = Vector()
            difference = roadY - self.tyre_radius - self.position.getY()
            self.position.add(self.gravity_vector)
        elif self.position.getY() > roadY - self.tyre_radius:
            self.position.subtract(self.gravity_vector_up)

        # Front tyre
        roadY_front = self.getRoadHeight(self.point1_front, self.point2_front, self.front_tyre.getX())
        if self.front_tyre.getY() <= roadY_front - self.tyre_radius:
            self.front_tyre.add(self.gravity_vector)
        elif self.front_tyre.getY() > roadY_front - self.tyre_radius:
            self.front_tyre.subtract(self.gravity_vector_up)

        print(str(roadY) + " and " + str(roadY_front))

    def rotateCar(self):
        x1 = self.position.getX()
        y1 = self.position.getY()
        x2 = self.front_tyre.getX()
        y2 = self.front_tyre.getY()
        self.car_rotation = math.atan((y2 - y1) / (x2 - x1))
        print(str(self.car_rotation) + " rotation")

    def applyBackground(self, canvas, mover):
        canvas.draw_image(image_link, (3214 / 2, 600 / 2), (3214, 600),
                          Vector((3214 / 2) - 10, 600 / 2).copy().toBackground(mover).getP(), (3214, 600))
        for i in range(1, self.roadLength % image_link.get_width()):
            canvas.draw_image(image_link, (3214 / 2, 600 / 2), (3214, 600),
                              Vector((3214 * i + (3214 / 2) - 10), 600 / 2).copy().toBackground(mover).getP(),
                              (3214, 600))

    def drawBerries2(self, canvas, mover):
        if self.berry2_draw_boolean:
            canvas.draw_image(berry_image_link, (287 / 2, 230 / 2), (287, 230),
                              self.berry2_pos.copy().toBackground(mover).getP(), self.berry2_dim.getP())

    def drawBerries(self, canvas, mover):
        if self.berry1_draw_boolean:
            canvas.draw_image(berry_image_link, (287 / 2, 230 / 2), (287, 230),
                              self.berry1_pos.copy().toBackground(mover).getP(), self.berry1_dim.getP())
        elif self.berry2_draw_boolean:
            canvas.draw_image(berry_image_link, (287 / 2, 230 / 2), (287, 230),
                              self.berry2_pos.copy().toBackground(mover).getP(), self.berry2_dim.getP())

    def placeBerries(self, startX, endX, slope):
        xCoord = random.randint(startX, endX)
        yCoord = slope * xCoord + 400 - 15
        berry_pos = Vector(xCoord, yCoord)
        return berry_pos

    def getRoadHeight(self, point1, point2, currentX):
        x1 = point1.getX()
        x2 = point2.getX()
        y1 = point1.getY()
        y2 = point2.getY()
        print(str(x1) + " " + str(x2) + " " + str(y1) + " " + str(y2))

        # Gradient
        m = (y2 - y1) / (x2 - x1)

        roadHeight = (m * (currentX - x1)) + y1
        return roadHeight

    def berryCollision(self, car_pos, berry_center, berry_dim):
        horizontalCollisionBoolean = car_pos.getX() >= berry_center.getX() - (
                berry_dim.getX() / 2) and car_pos.getX() <= berry_center.getX() + (berry_dim.getX() / 2)
        verticalCollisionBoolean = car_pos.getY() >= berry_center.getY() - (
                berry_dim.getY() / 2) and car_pos.getY() <= berry_center.getY() + (berry_dim.getY() / 2)
        return horizontalCollisionBoolean and verticalCollisionBoolean

    def berryMerchantCollision(self, car_pos, berry_merchant_center, berryMerchant1_dim):
        horizontalCollisionBoolean = car_pos.getX() >= berry_merchant_center.getX() - (
                berryMerchant1_dim.getX() / 2) and car_pos.getX() <= berry_merchant_center.getX() + (
                                             berryMerchant1_dim.getX() / 2)
        verticalCollisionBoolean = car_pos.getY() >= berry_merchant_center.getY() - (
                berryMerchant1_dim.getY() / 2) and car_pos.getY() <= berry_merchant_center.getY() + (
                                           berryMerchant1_dim.getY() / 2)
        return horizontalCollisionBoolean and verticalCollisionBoolean

    def moneyCounter(self):
        if self.berryCollision(self.position, self.berry1_pos, self.berry1_dim):
            self.berryMoney = self.berryMoney + 2
            return self.berryMoney
        if self.berryCollision(self.position, self.berry2_pos, self.berry2_dim):
            self.berryMoney = self.berryMoney + 2
            return self.berryMoney
        elif self.berryMerchantCollision(self.position, self.berryMerchant1_pos, self.berryMerchant1_dim):
            self.berryMoney = self.berryMoney + 15
            return self.berryMoney

    def bmCollision(self, car_pos, bm_center, bm_dim):
        horizontalCollisionBoolean = car_pos.getX() >= bm_center.getX() - (
                bm_dim.getX() / 2) and car_pos.getX() <= bm_center.getX() + (bm_dim.getX() / 2)
        verticalCollisionBoolean = car_pos.getY() >= bm_center.getY() - (
                bm_dim.getY() / 2) and car_pos.getY() <= bm_center.getY() + (bm_dim.getY() / 2)
        return horizontalCollisionBoolean and verticalCollisionBoolean

    def useFuel(self):
        self.fuelDistance = self.fuelDistance - 5
        if self.fuelDistance % self.distancePerLitre == 0:
            self.fuel = self.fuel - 1

    def drawBerryMerchant(self, canvas, mover):

        global timer_counter_bm, frame_bm
        image_height = berry_merchant_image.get_height()
        image_width = berry_merchant_image.get_width()

        center = [image_width / 6, image_width / 2, 5 / 6 * image_width]
        if timer_counter_bm % 10 == 0:
            if frame_bm % 2 == 0:
                frame_bm = 1
            else:
                frame_bm = frame_bm + 1
        if self.bm1_draw_boolean:
            canvas.draw_image(berry_merchant_image, (center[frame_bm], image_height / 2),
                              (image_width / 3, image_height), self.bm1_pos.copy().toBackground(mover).getP(),
                              self.bm1_dim.getP())
        timer_counter_bm += 1

    def updateTimerCounter(self):
        global timer_counter_bm
        timer_counter_bm += 1

    def setCarInMotion(self):
        self.car_in_motion = True

    def setCarStationary(self):
        self.car_in_motion = False

    def drawBear(self, canvas, mover):
        global timer_counter_bm, frame_bear
        image_width = bear_image.get_width()
        image_height = bear_image.get_height()

        center = [image_width / 14,
                  image_width / 14 + image_width / 7,
                  image_width / 14 + image_width / 7 * 2,
                  image_width / 14 + image_width / 7 * 3,
                  image_width / 14 + image_width / 7 * 4,
                  image_width / 14 + image_width / 7 * 5,
                  image_width / 14 + image_width / 7 * 6]
        if timer_counter_bm % 3 == 0:
            if frame_bear % 5 == 0:
                frame_bear = 1
            else:
                frame_bear = frame_bear + 1
        canvas.draw_image(bear_image, (center[frame_bear], image_height / 2), (image_width / 7, image_height),
                          self.bear_pos.copy().toBackground(mover).getP(), self.bear_dim.getP())

        self.updateBearPosition()

    def applyBearGravity(self):
        roadY_bear = self.getRoadHeight(self.point1_bear, self.point2_bear, self.position.getX() - self.bear_distance)
        if self.bear_pos.getY() <= roadY_bear - self.bear_dim.getX() / 2:
            self.bear_pos.add(self.gravity_vector)
        elif self.bear_pos.getY() > roadY_bear - self.bear_dim.getX() / 2:
            self.bear_pos.subtract(self.gravity_vector_up)

    def updateBearPosition(self):
        self.findRoadPoints(self.position.getX())
        self.bear_pos.setX(self.position.getX() - self.bear_distance)
        self.applyBearGravity()

    def updateScore(self):
        self.gameInterface.player.current_score = self.score

    def handleBear(self):
        if self.acceleration.getX() <= 10:
            if self.bear_distance >= 10:
                self.bear_distance -= 2

    def updateScore(self):
        self.gameInterface.player.current_score = self.score

        if self.acceleration.getX() >= 90:
            if self.bear_distance <= 200:
                self.bear_distance += 2

        if self.bear_distance <= 10:
            if self.gameInterface.player.attributes.lives != 0:
                self.gameInterface.player.attributes.lives -= 1
                self.bear_distance = 200

    def handleLives(self):
        if self.gameInterface.player.attributes.lives == 0:
            self.gameInterface.window.frame.set_draw_handler(self.gameInterface.window.death_screen.draw_canvas)

    def createEndofRoadSign(self, canvas):
        image_height = end_of_road_image.get_height()
        image_width = end_of_road_image.get_width()
        canvas.draw_image(end_of_road_image, (image_width / 2, image_height / 2), (image_height, image_width),
                          Vector(200, 200).copy().toBackground(self.mover).getP(), (image_width, image_width))

    def checkEndOfLevel(self):
        print("X coord " + str(self.position.getX()))
        if self.position.getX() >= self.roadLength - 200:
            self.level_completed = True
            print("Level end")

    def draw(self, canvas, mover):
        self.updateScore()
        self.applyBackground(canvas, mover)

        for i in range(len(self.pointsList) - 1):
            point1 = self.pointsList[i].copy().toBackground(mover)
            point2 = self.pointsList[i + 1].copy().toBackground(mover)
            canvas.draw_line(point1.getP(), point2.getP(), 5, 'white')

        self.drawBerries2(canvas, mover)
        self.drawBerries(canvas, mover)

        self.drawBerryMerchant(canvas, mover)

        self.drawBerryMerchant(canvas, mover)
        self.constructCar(canvas, mover)

        self.drawBerries(canvas, mover)

        self.drawBerryMerchant(canvas, mover)
        self.drawBear(canvas, mover)
        self.constructCar(canvas, mover)

        canvas.draw_text("Fuel (litres): " + str(self.fuel) + " Distance: " + str(self.fuelDistance), [20, 20], 15,
                         'white')

        # Collision detection
        if self.berryCollision(self.position, self.berry1_pos, self.berry1_dim) or self.berryCollision(self.position,
                                                                                                       self.berry2_pos,
                                                                                                       self.berry2_dim):
            if self.berry1_draw_boolean or self.berry2_draw_boolean:
                self.score += 2
            self.berry1_draw_boolean = False
            self.berry2_draw_boolean = False
            print("Collision with Berry")

        # sound.play()

        if self.bmCollision(self.position, self.bm1_pos, self.bm1_dim):
            if self.bm1_draw_boolean:
                self.score += 15
            self.bm1_draw_boolean = False
            print("Collision with BM")

        self.handleBear()
        self.handleLives()

        self.createEndofRoadSign(canvas)

        self.checkEndOfLevel()

        self.berryMerchant1_draw_boolean = True
        self.updateTimerCounter()


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

        self.initial_origin_vector = Vector(Values.canvas_WIDTH / 2, Values.canvas_HEIGHT / 2)

        # Creating mover with the center set to center point of the canvas
        self.mover = MoveObjects(self.initial_origin_vector,
                                 Vector(Values.canvas_WIDTH, Values.canvas_HEIGHT))

        self.final_origin = self.initial_origin_vector.copy().toBackground(self.mover)
        self.mover.setCenter(self.final_origin)

        # Road bounds (For the mover)
        self.leftEnd = False
        self.rightEnd = False

        # self.car = Car(Vector(30, 100), 100, self.road,self.mover)

        self.gameplay = GamePlay(self.mover, self)

        # Car control booleans
        self.moveCarRight = False
        self.moveCarLeft = False

        # Level creation
        self.gameplay.createLevel1()

        # Player data
        self.player_attributes = PlayerAttributes()  # Do not directly call methods on this one
        self.player = Player(self.player_attributes)  # Call methods on self.player.attributes instead
        self.hud = HUD(self.window, self.player.current_score, self.player.attributes.lives)

    def draw_canvas(self, canvas):
        # Draw road
        self.gameplay.draw(canvas, self.mover)
        self.hud.draw_hud(canvas)
        self.hud.update_attributes(self.player.current_score, self.player.attributes.lives, self.gameplay.fuel)

        # Setting key up and down handlers and updating
        self.window.frame.set_keydown_handler(self.keydown)
        self.window.frame.set_keyup_handler(self.keyup)
        self.window.frame.set_mouseclick_handler(self.mouse_down)
        self.updateKey()

        # Opening transition
        self.transition_clock.tick()
        if self.left_cover_x > - self.window.__class__.WIDTH / 2:
            self.reveal(canvas)

    # Curtain animation mathod
    def reveal(self, canvas):
        box_colour_left = "Teal"
        box_colour_right = "Teal"
        canvas.draw_polygon([(self.left_cover_x, 0), (self.left_cover_x, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.left_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour_left, box_colour_left)
        canvas.draw_polygon([(self.right_cover_x, 0),
                             (self.right_cover_x, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, self.window.__class__.HEIGHT),
                             (self.right_cover_x + self.window.__class__.WIDTH / 2, 0)],
                            1, box_colour_right, box_colour_right)
        self.left_cover_x -= 25
        self.right_cover_x += 25

    def mouse_down(self, position):
        if 180 > position[0] > 75 and 25 > position[1] > 0:
            self.hud.pause()

    def keyup(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.mover.moveRight = False
            self.moveCarRight = False
        elif key == simplegui.KEY_MAP['left']:
            self.mover.moveLeft = False
            self.moveCarLeft = False
        elif key == simplegui.KEY_MAP['up']:
            self.mover.moveUp = False
        elif key == simplegui.KEY_MAP['down']:
            self.mover.moveDown = False

    def keydown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.mover.moveRight = True
            # Move car right
            self.moveCarRight = True

        elif key == simplegui.KEY_MAP['left']:
            self.mover.moveLeft = True
            # Move car left
            self.moveCarLeft = True

        elif key == simplegui.KEY_MAP['up']:
            self.mover.moveUp = True
        elif key == simplegui.KEY_MAP['down']:
            self.mover.moveDown = True
        elif self.kb_compat.escape_key_pressed(key):
            self.pause()

    def pause(self):
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2
        self.window.frame.set_draw_handler(self.window.pause_menu.draw_canvas)

    def checkRoadEnds(self):
        if self.mover.center.getX() < self.gameplay.endOfRoad_Origin.getX():
            self.leftEnd = True

        else:
            self.leftEnd = False
        if self.mover.center.getX() > self.gameplay.endOfRoadRight_Origin.getX():
            self.rightEnd = True
        else:
            self.rightEnd = False

    def updateKey(self):
        self.checkRoadEnds()
        self.mover.move(self.leftEnd, self.rightEnd)

        # Move car
        if self.moveCarRight == True:
            self.gameplay.moveCarRight()
        elif self.moveCarLeft == True:
            self.gameplay.moveCarLeft()
        elif self.moveCarLeft == False and self.moveCarRight == False:
            self.gameplay.decelerate()
        # self.mover.zoom() -- Zoom feature is disabled
        print(self.gameplay.acceleration.getP())


class Game:
    WIDTH = 800
    HEIGHT = 600

    # Image resource links

    def __init__(self):
        """
        Create the frame and instance variables assigned to instances of classes that constitute the various
        screens of the game.

        An instance of this class will be passed onto the classes that require the ability to draw onto the canvas,
        or change the draw, key down/up, and mouse click handlers.
        """
        self.frame = simplegui.create_frame("BerryDrive (CS1830 Group Cloudberry)", Game.WIDTH, Game.HEIGHT)

        # Instantiating classes
        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.death_menu = DeathMenu(self)
        self.game_interface = GameInterface(self)
        self.scoreboard = None  # Must be initialised in main menu to reload records
        self.options = None  # WIP
        self.hud = HUD(self)
        self.player_details_form = PlayerDetailsForm(self)
        self.story_screen = StoryInitialiser(self).story_screen

    # Start main_menu
    def start(self):
        """
        When starting the frame, set the draw handler to render the main menu first.
        """
        self.frame.set_draw_handler(self.main_menu.draw_canvas)
        self.frame.start()


# The main funciton
if __name__ == "__main__":
    # Using start method from class Game to display main_menu
    window = Game()
    window.start()

