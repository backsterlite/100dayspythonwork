from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 20, 'normal')
DATA_PATH = "data.txt"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self._score = 0
        self.high_score = self.read_data()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def reset_scoreboard(self):
        if self._score > self.high_score:
            self.high_score = self._score
        self._score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-20, 265)
        text = f"Score: {self._score} High score: {self.high_score}"
        self.write(text, align=ALIGN, font=FONT)

    def read_data(self):
        with open(DATA_PATH, 'r') as file:
            high_score = file.readline()
        return int(high_score)

    def write_data(self):
        with open(DATA_PATH, 'w') as file:
            file.write(str(self.high_score))
