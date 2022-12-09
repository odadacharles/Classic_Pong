from turtle import Turtle
PLAYER1_START = (-350, 0)
PLAYER2_START = (350, 0)


class Paddle(Turtle):
    """ Define the paddle class """
    def __init__(self, player_no):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.player_no = player_no
        self.penup()
        self.player_side()

    def player_side(self):
        """ Method that takes players' paddles to their starting positions """
        if self.player_no == 1:
            self.goto(PLAYER1_START)
            self.color('white')
        else:
            self.goto(PLAYER2_START)
            self.color('white')

    def up(self):
        """ Method that defines movement when the 'Up' or 'w' button is pressed """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """ Method that defines movement when the 'Down' or 's' button is pressed """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        """ Method that moves players' paddles back to their starting positions"""
        if self.player_no == 1:
            self.goto(PLAYER1_START)
        else:
            self.goto(PLAYER2_START)
