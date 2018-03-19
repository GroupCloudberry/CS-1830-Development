import random
import math
from vector import Vector
from values import Values
import math
import simpleguitk as simplegui

tyre_image = simplegui.load_image('https://i.imgur.com/m7e5j6O.png')
car_image = simplegui.load_image('https://i.imgur.com/dtyG7HO.png')
image_link = simplegui.load_image('https://i.imgur.com/ZhPTrBH.jpg')
berry_image_link = simplegui.load_image('https://i.imgur.com/IPlsY2L.png')
berry_merchant_image = simplegui.load_image('https://i.imgur.com/iQIBDHX.png')
berry_merchant_image = simplegui.load_image("https://i.imgur.com/2wJC0d9.png")


class GamePlay:

    def __init__(self, cam):
        #Road
        self.pointsList = list()
        self.endOfRoad_Origin = Vector(Values.canvas_WIDTH/2, Values.canvas_HEIGHT/2).copy().toBackground(cam)
        self.endOfRoadRight_Origin = Vector(15000-(Values.canvas_WIDTH/2), Values.canvas_HEIGHT/2).copy().toBackground(cam)

        self.point1_pos = Vector()
        self.point2_pos = Vector()

        self.point1_front = Vector()
        self.point2_front = Vector()
        self.point1_t2 = Vector()
        self.point2_t2 = Vector()

        self.position = Vector(300,100)
        #Tyre Vectors
        self.front_tyre = Vector(self.position.getX()+40, self.position.getY())

        self.tyre_radius = 15


        #constants
        self.gravity_vector = Vector(0,2)
        self.movement_vector = Vector(5,0)

        self.carTyreDistance = 80

        self.berry1_pos = Vector(1000,375)
        self.berry1_dim = Vector(40,30)
        self.berry1_draw_boolean = True
        self.berryMerchant1_draw_boolean = True
        self.berryMerchant1_pos = Vector(2000, 400)
        self.berryMerchant1_dim = Vector(300, 235)

        self.cam = cam

        self.rotation = 0
        self.car_rotation = 0


#Road for level 1
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
        slope12end = Vector(10000, 300)
        slope13end = Vector(12000, 300)
        slope14end = Vector(13000, 400)
        straight15end = Vector(15000, 400)

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
        self.pointsList.append(slope13end)
        self.pointsList.append(slope14end)
        self.pointsList.append(straight15end)

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
        self.pointsList.append(Vector(11000, 400))
        self.pointsList.append(Vector(13000, 300))
        self.pointsList.append(Vector(14000, 400))
        self.pointsList.append(Vector(15000, 400))


    #Returns point list
    def getPointsList(self):
        return self.pointsList

    def constructCar(self, canvas ,cam):
        self.rotateCar()
        canvas.draw_image(car_image, (521 / 2, 131 / 2), (521, 131), Vector((self.front_tyre.getX()-40),((self.front_tyre.getY() + self.position.getY())/2)-15).copy().toBackground(cam).getP(),(130, 50), self.car_rotation)
        canvas.draw_image(tyre_image, (200 / 2, 200 / 2), (200, 200), self.position.copy().toBackground(cam).getP(), (self.tyre_radius*2, self.tyre_radius*2), self.rotation)
        canvas.draw_image(tyre_image, (200 / 2, 200 / 2), (200, 200), self.front_tyre.copy().toBackground(cam).getP(),(self.tyre_radius * 2, self.tyre_radius * 2), self.rotation)

        self.updateTyres()
        self.applyGravity()

    def updateTyres(self):
        self.front_tyre.setX(self.position.getX()+80)

    def moveCarRight(self):
        self.position.add(self.movement_vector)
        self.rotation += 0.5

    def moveCarLeft(self):
        self.position.subtract(self.movement_vector)
        self.rotation += -0.5

    def findRoadPoints(self, currentX):
        for i in range(len(self.pointsList)-1):
            if self.pointsList[i].getX() <= currentX:
                self.point1_pos = self.pointsList[i]
                self.point2_pos = self.pointsList[i + 1]
            if self.pointsList[i].getX() <= self.front_tyre.getX():
                self.point1_front = self.pointsList[i]
                self.point2_front = self.pointsList[i + 1]

    def applyGravity(self):
        self.findRoadPoints(self.position.getX())

        roadY = self.getRoadHeight(self.point1_pos, self.point2_pos, self.position.getX())
        if self.position.getY()<= roadY - self.tyre_radius:
            self.position.add(self.gravity_vector)
        elif self.position.getY()>roadY - self.tyre_radius:
            self.position.subtract(self.gravity_vector)

        #Front tyre
        roadY_front = self.getRoadHeight(self.point1_front, self.point2_front, self.front_tyre.getX())
        if self.front_tyre.getY() <= roadY_front - self.tyre_radius:
            self.front_tyre.add(self.gravity_vector)
        elif self.front_tyre.getY() > roadY_front - self.tyre_radius:
            self.front_tyre.subtract(self.gravity_vector)

        print(str(roadY) + " and " + str(roadY_front))

    def rotateCar(self):
        x1 = self.position.getX()
        y1 = self.position.getY()
        x2 = self.front_tyre.getX()
        y2 = self.front_tyre.getY()
        self.car_rotation = math.atan((y2 - y1) / (x2 - x1))
        print(str(self.car_rotation) + " rotation")


    def applyBackground(self, canvas, cam):
        canvas.draw_image(image_link, (3214 / 2, 600 / 2), (3214, 600), Vector((3214 / 2) - 10, 600 / 2).copy().toBackground(cam).getP(), (3214, 600))

    def drawBerries(self, canvas, mover):
        if self.berry1_draw_boolean:
            canvas.draw_image(berry_image_link, (287 / 2, 230 / 2), (287, 230), self.berry1_pos.copy().transformToCam(mover).getP(), self.berry1_dim.getP())

    def nextFrame(self, frameIndex, columns, rows):
        i = (frameIndex[0] + 1) % columns
        if i == 0:
            j = (frameIndex[1] + 1) % rows
        else:
            j = frameIndex[1]
        frameIndex = (i, j)

    def drawBerryMerchant(self, canvas, mover):
        if self.berryMerchant1_draw_boolean:
            width = 900
            height = 234
            columns = 3
            rows = 1

            frameWidth = width // columns
            frameHeight = height // rows

            frameCentreX = frameWidth // 2
            frameCentreY = frameHeight // 2
            frameIndex = (2, 1)

            x = frameWidth * frameIndex[0] + frameCentreX
            y = frameHeight * frameIndex[1] + frameCentreY
            center_source = Vector(x, y)
            width_height_source = Vector(frameWidth, frameHeight)
            center_dest = Vector(frameWidth / 2, frameHeight / 2)
            width_height_dest = Vector(frameWidth, frameHeight)
            canvas.draw_image(berry_merchant_image, center_source.copy().transformToCam(mover).getP(), width_height_source.copy().transformToCam(mover).getP(), center_dest.copy().transformToCam(mover).getP(), width_height_dest.getP())
            #timer = simplegui.create_timer(200, self.nextFrame(frameIndex, columns, rows))
            #timer.start()

            canvas.draw_image(berry_image_link, (287 / 2, 230 / 2), (287, 230), self.berry1_pos.copy().toBackground(cam).getP(), self.berry1_dim.getP())

    def getRoadHeight(self, point1, point2, currentX):
        x1 = point1.getX()
        x2 = point2.getX()
        y1 = point1.getY()
        y2 = point2.getY()

        #Gradient
        m = (y2-y1)/(x2-x1)

        roadHeight = (m*(currentX-x1)) + y1
        return roadHeight

    def berryCollision(self, car_pos, berry_center, berry_dim):
        horizontalCollisionBoolean = car_pos.getX() >= berry_center.getX() - (berry_dim.getX()/2) and car_pos.getX() <= berry_center.getX() + (berry_dim.getX()/2)
        verticalCollisionBoolean = car_pos.getY() >= berry_center.getY() - (berry_dim.getY()/2) and  car_pos.getY()<= berry_center.getY() + (berry_dim.getY()/2)
        return horizontalCollisionBoolean and verticalCollisionBoolean


    def berryMerchantCollision(self, car_pos, berry_merchant_center, berryMerchant1_dim):
        horizontalCollisionBoolean = car_pos.getX() >= berry_merchant_center.getX() - (
                    berryMerchant1_dim.getX() / 2) and car_pos.getX() <= berry_merchant_center.getX() + (berryMerchant1_dim.getX() / 2)
        verticalCollisionBoolean = car_pos.getY() >= berry_merchant_center.getY() - (
                    berryMerchant1_dim.getY() / 2) and car_pos.getY() <= berry_merchant_center.getY() + (berryMerchant1_dim.getY() / 2)
        return horizontalCollisionBoolean and verticalCollisionBoolean


    def moneyCounter(self):
        money = 0
        if self.berryCollision(self.position, self.berry1_pos, self.berry1_dim):
            money = money+2
            return money
        elif self.berryMerchantCollision(self.position, self.berryMerchant1_pos, self.berryMerchant1_dim):
            money = money+15
            return money


    def draw(self,canvas,cam):
        self.applyBackground(canvas, cam)

        for i in range(len(self.pointsList)-1):
            point1 = self.pointsList[i].copy().toBackground(cam)
            point2 = self.pointsList[i+1].copy().toBackground(cam)
            canvas.draw_line(point1.getP(), point2.getP(), 5, 'white')
        self.drawBerries(canvas, cam)
        self.drawBerryMerchant(canvas, cam)
        self.constructCar(canvas, cam)


        #Collision detection
        if self.berryCollision(self.position, self.berry1_pos, self.berry1_dim):
            self.berry1_draw_boolean = False
            print("Collision")

        self.berryMerchant1_draw_boolean = True
        self.drawBerryMerchant(canvas, cam)
        print(self.moneyCounter())
        canvas.draw_polygon([(50, 50), (50, 100), (100, 100), (100, 50)], 5, 'Green')
        canvas.draw_text(self.moneyCounter(),(75, 75), 25, 'Green')
        #timer = simplegui.create_timer(200, self.nextFrame(self.drawBerryMerchant.frameIndex, self.drawBerryMerchant.columns, self.drawBerryMerchant.rows))
        #timer.start()







