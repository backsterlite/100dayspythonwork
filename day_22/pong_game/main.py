from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.colormode(255)
screen.bgcolor((0, 0, 0))
screen.tracer(0)
HALF_VERTICAL_FIELD = screen.window_height() // 2 - 20
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() == HALF_VERTICAL_FIELD or ball.ycor() == -HALF_VERTICAL_FIELD:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and right_paddle.xcor() > 340 \
        or ball.distance(left_paddle) < 50 and left_paddle.xcor() < -340:
        ball.bounce_x()

    # Detect right missing
    if ball.xcor() > 420:
        ball.revert()
        scoreboard.l_point()

    # Detect left missing
    if ball.xcor() < -420:
        ball.revert()
        scoreboard.r_point()

screen.exitonclick()

