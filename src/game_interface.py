from hud import HUD
from keyboard_compat import KeyboardCompat
from transition_clock import TransitionClock
from vector import Vector
from values import Values
from gameplay import GamePlay
from car import Car
from move_objects import MoveObjects

try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
from values import Values

if simplegui.__name__ == "simpleguitk":
    from player_sqlite import PlayerSQLite as Player
    from player_attributes_sqlite import PlayerAttributesSQLite as PlayerAttributes
else:
    from player import Player
    from player_attributes import PlayerAttributes


class GameInterface:
    def __init__(self, window):
        self.window = window
        self.kb_compat = KeyboardCompat()
        self.transition_clock = TransitionClock()
        self.left_cover_x = 0
        self.right_cover_x = self.window.__class__.WIDTH / 2

        self.initial_origin_vector = Vector(Values.canvas_WIDTH/2, Values.canvas_HEIGHT/2)

        # Creating mover with the center set to center point of the canvas
        self.mover = MoveObjects(self.initial_origin_vector,
                                 Vector(Values.canvas_WIDTH,Values.canvas_HEIGHT))

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
        self.gameplay.createLevel4()

        # Player data
        self.player_attributes = PlayerAttributes() # Do not directly call methods on this one
        self.player = Player(self.player_attributes) # Call methods on self.player.attributes instead
        self.hud = HUD(self.window, self.player.current_score,  self.player.attributes.lives)

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

    def keyup(self,key):
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

    def keydown(self,key):
        if key == simplegui.KEY_MAP['right']:
            self.mover.moveRight = True
            #Move car right
            self.moveCarRight = True

        elif key == simplegui.KEY_MAP['left']:
            self.mover.moveLeft = True
            #Move car left
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
        #self.mover.zoom() -- Zoom feature is disabled
        print(self.gameplay.acceleration.getP())
