from story_screen import StoryPage, StoryScreen


class StoryInitialiser:

    def __init__(self, window):
        self.window = window
        self.pages = []

        self.pages.append(StoryPage(
            {
                "text": "Sigh! Another day, another battle to survive! "
                        "Hey, but maybe you can help me out today :) Help me collect cloudberries?",
                "image": "https://i.imgur.com/V0Loqpm.png"
            },
            {
                "text": "",
                "image": None
            }
        ))
        self.pages.append(StoryPage(
            {
                "text": "",
                "image": None
            },
            {
                "text": "",
                "image": None
            }
        ))

        self.story_screen = StoryScreen(self.window, self.pages)
