# Images
# Backgrounds


# This program draws two versions of the same image, one of
#	which has a transparent background.

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui


# Global Variables

canvas_width = 200
canvas_height = 200
image_center = (25, 25)
image_size = (50, 50)
pos1 = [60, 100]
pos2 = [140, 100]
# This line is necessary to import images for your program.
white_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week5-triangle.png")
clear_image = simplegui.load_image("https://i.imgur.com/LzsJYH2.png")
image2_size = (clear_image.get_width(), clear_image.get_height())


# Event Handlers

def draw(canvas):
    canvas.draw_image(white_image, image_center, image_size, pos1, image_size)
    canvas.draw_image(clear_image, (100,90), (100,100), pos2, image_size)


# Frame

frame = simplegui.create_frame("Backgrounds", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_canvas_background("Maroon")

# Start
frame.start()