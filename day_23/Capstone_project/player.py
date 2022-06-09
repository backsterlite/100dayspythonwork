from turtle import Turtle


class Player(Turtle):
    STARTING_POSITION = (0, -280)
    FINISH_Y_LINE = 280

    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.seth(90)
        self.refresh()

    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def refresh(self):
        self.goto(Player.STARTING_POSITION)
