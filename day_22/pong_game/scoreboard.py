from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_markup()
        self.goto(-100, 175)
        self.write(self.l_score, False, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 175)
        self.write(self.r_score, False, align='center', font=('Courier', 80, 'normal'))

    def draw_markup(self):
        self.goto(0, -280)
        self.seth(90)
        self.pensize(5)
        for _ in range(15):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

