import random
import math
from vector import Vector
from values import Values
import math
import time
import simpleguitk as simplegui

tyre_image = simplegui.load_image('https://i.imgur.com/m7e5j6O.png')
car_image = simplegui.load_image('https://i.imgur.com/dtyG7HO.png')
image_link = simplegui.load_image('https://i.imgur.com/ZhPTrBH.jpg')

# berry_image_link = simplegui.load_image('https://i.imgur.com/erLYnGU.png')

berry_image_link = simplegui.load_image('https://i.imgur.com/IPlsY2L.png')

# berry_merchant_image = simplegui.load_image('https://i.imgur.com/iQIBDHX.png')

berry_merchant_image = simplegui.load_image('https://i.imgur.com/78r4LwF.png')

bear_image = simplegui.load_image('https://i.imgur.com/284X6gP.png')
end_of_road_image = simplegui.load_image('https://i.imgur.com/eqboshP.png')

# Commented code for audio
# sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')

timer_counter_bm = 0
frame_bm = 0
frame_bear = 0


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
        self.bear_distance -= 5
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
            self.gameplay.window.frame.set_draw_handler(self.gameInterface.window.death_screen.draw_canvas)

    def createEndofRoadSign(self, canvas):
        image_height = end_of_road_image.get_height()
        image_width = end_of_road_image.get_width()
        canvas.draw_image(end_of_road_image, (image_width / 2, image_height / 2), (image_height, image_width),
                          Vector(self.roadLength-200, 200).copy().toBackground(self.mover).getP(), (image_width, image_width))

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
