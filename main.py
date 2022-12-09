# imports
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# initialize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

# initialize objects
player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
board = Scoreboard()

# listen for key presses
screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")

# Game logic
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(player2) < 50 or \
            ball.xcor() < -320 and ball.distance(player1) < 50:
        ball.paddle_bounce()

    # Detect ball missing paddle
    if ball.xcor() > 370 or ball.xcor() < -370:
        board.score(ball.xcor())
        ball.reset_position()
        ball.paddle_bounce()
        player1.reset_position()
        player2.reset_position()

screen.exitonclick()
