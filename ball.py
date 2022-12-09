from turtle import Turtle


class Ball(Turtle):
    """ Define the ball class with ball's attributes and methods"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.speed(1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ Method for moving the ball around the screen """
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """ Method defining how the ball behaves when it hits a wall """
        self.y_move = -self.y_move
        self.move()

    def paddle_bounce(self):
        """ Method defining how the ball behaves when it hits a paddle """
        self.x_move = -self.x_move
        self.move_speed *= 0.9
        self.move()

    def reset_position(self):
        """ Method for resetting the ball after one player fails"""
        self.goto(0, 0)
        self.move_speed = 0.1
