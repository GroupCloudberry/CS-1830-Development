from story_screen import StoryPage, StoryScreen


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
