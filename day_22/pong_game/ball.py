from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__('circle')
        self.ball_speed = 0.1
        self.x_move = 10
        self.y_move = 10
        self.color('white')
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def revert(self):
        self.ball_speed = 0.1
        self.home()
        self.bounce_x()

