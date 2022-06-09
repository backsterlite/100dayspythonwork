from turtle import Turtle
STARTING_POSITIONS_Y = [-40, -20, 0, 20, 40]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() + 40 < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() - 40 > - 280:
            self.goto(self.xcor(), self.ycor() - 20)
