from Vector import Vector
from Camera import Camera
from Road import Road
from Settings import *

cam= Camera(Vector(0,0),CAM_ZOOM_SENSITIVITY,CAM_MOVE_SENSITIVITY,Vector(CANVAS_WIDTH,CANVAS_HEIGHT))
road = Road()
road.initSlope()