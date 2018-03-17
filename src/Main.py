import simpleguitk as simpleguics2pygame
from KeyHandler import keydown,keyup
from Objects import road,cam
from Settings import CANVAS_HEIGHT,CANVAS_WIDTH

def draw(canvas):

    road.draw(canvas,cam)
    print("------------------------------------------")
    print(cam.dim)
    print(cam.dimCanv)
    print("-------------------FINISH------------------")
    cam.zoom()
    cam.move()


frame = simpleguics2pygame.create_frame("Testing", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)
frame.start()
