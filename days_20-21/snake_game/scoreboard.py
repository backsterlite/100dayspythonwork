from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self._score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-20, 265)
        self.update_score()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def game_over(self):
        self.home()
        self.write("Game Over", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        text = f"score {self._score}"
        self.write(text, align=ALIGN, font=FONT)
