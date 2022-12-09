from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 30, 'bold')


class Scoreboard(Turtle):
    """ Define class for the scoreboard """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, -250)
        self.goto(0, 250)
        self.player1_score = 0
        self.player2_score = 0
        self.write_score()

    def write_score(self):
        """ Method that writes player's scores on the screen """
        self.write(f"{self.player1_score}           {self.player2_score}", False, ALIGNMENT, FONT)

    def score(self, ball_position):
        """ Method that defines how scoring is done when a player doesn't reach the ball"""
        if ball_position > 330:
            self.player1_score += 1
        else:
            self.player2_score += 1
        self.clear()
        self.write_score()
