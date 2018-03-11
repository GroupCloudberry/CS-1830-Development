from story_screen import StoryScreen, StoryPage

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


class StoryScreenDemo:

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.frame = simplegui.create_frame("BerryDrive (CS1830 Group Cloudberry)", StoryScreenDemo.WIDTH, StoryScreenDemo.HEIGHT)
        self.test_page1 = StoryPage({"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                           "Donec sed lorem in sem elementum pretium at ut eros. "
                                           "Quisque sollicitudin arcu nulla, eu venenatis lorem tristique hendrerit. "
                                           "Nam gravida tincidunt placerat. Sed sed nisl nec orci bibendum condimentum.",
                                   "image": "https://i.imgur.com/CWVsgu3.png"},
                                    {"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                            "Donec sed lorem in sem elementum pretium at ut eros. "
                                            "Quisque sollicitudin arcu nulla, eu venenatis lorem tristique hendrerit. "
                                            "Nam gravida tincidunt placerat. Sed sed nisl nec orci bibendum condimentum.",
                                    "image": "https://i.imgur.com/CWVsgu3.png"},
                                    )
        self.test_page2 = StoryPage({"text": "Ut quam quam, pretium id lobortis quis, viverra ac odio. "
                                             "Donec efficitur a magna eleifend ullamcorper. "
                                             "Aliquam finibus aliquam neque, sed consequat magna. "
                                             "Morbi rutrum felis turpis, laoreet ultricies nisi suscipit quis. "
                                             "Praesent fringilla nibh tellus, ut tristique velit mattis non. "
                                             "Fusce mollis ex ipsum, a lobortis massa pharetra non.",
                                     "image": "https://i.imgur.com/CWVsgu3.png"},
                                    {"text": "Ut quam quam, pretium id lobortis quis, viverra ac odio. "
                                             "Donec efficitur a magna eleifend ullamcorper. "
                                             "Aliquam finibus aliquam neque, sed consequat magna. "
                                             "Morbi rutrum felis turpis, laoreet ultricies nisi suscipit quis. "
                                             "Praesent fringilla nibh tellus, ut tristique velit mattis non. "
                                             "Fusce mollis ex ipsum, a lobortis massa pharetra non.",
                                     "image": "https://i.imgur.com/CWVsgu3.png"},
                                    )
        self.pages = [self.test_page1, self.test_page2]
        self.story_screen = StoryScreen(self, self.pages)

    def start(self):
        self.frame.set_draw_handler(self.story_screen.draw_canvas)
        self.frame.start()


if __name__ == "__main__":
    window = StoryScreenDemo()
    window.start()
