import simpleguitk


BALL_RADIUS = 10
tyre1_pos = [70, 300]
tyre2_pos = [170, 300]

gravity = -0.1
velocity = 8
vel = [0,  velocity]


class GameInterface:
    def __init__(self, window):
        self.window = window

    def draw(self, canvas):
        global velocity

        #Constructing the road
        canvas.draw_line([0, 400], [350, 400], 5, 'white')


        vel[1] -= gravity


        # Update car position
        tyre1_pos[1] += vel[1]
        tyre2_pos[1] += vel[1]

        # Boundaries
        if tyre1_pos[1] <= BALL_RADIUS:
            vel[1] = - vel[1]
        if tyre1_pos[1] >= 375:
            vel[1] = - velocity

        canvas.draw_circle(tyre1_pos, 20, 5, "Grey", "white")
        canvas.draw_circle(tyre2_pos, 20, 5, "Grey", "White")


        """
                    3-----------4
                   /             \
            1____2/               \5_____6
            |                            | 
            |                            |  
            8----------------------------7
                tyre1           tyre2  
        """
        car_body_point1 = [tyre1_pos[0] - 50, tyre1_pos[1] - 60]
        car_body_point2 = [tyre1_pos[0], tyre1_pos[1]-60]
        car_body_point3 = [tyre1_pos[0]+15, tyre1_pos[1]-80]
        car_body_point4 = [tyre2_pos[0] - 15, tyre2_pos[1] - 80]
        car_body_point5 = [tyre2_pos[0], tyre2_pos[1] - 60]
        car_body_point6 = [tyre2_pos[0] + 50, tyre2_pos[1] - 60]
        car_body_point7 = [tyre2_pos[0] + 50, tyre2_pos[1] - 30]
        car_body_point8 = [tyre1_pos[0] - 50, tyre1_pos[1] - 30]

        car_body_pos = [car_body_point1,car_body_point2,car_body_point3,car_body_point4,car_body_point5,car_body_point6,car_body_point7,car_body_point8]

        canvas.draw_polygon(car_body_pos, 1, 'white', 'white')