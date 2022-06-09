from turtle import Turtle
import time
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
DIRECTION = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
ALLOW_DIRECTIONS = {
    'left': [90, 270],
    'right': [90, 270],
    'down': [0, 180],
    'up': [0, 180],
}


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
        self.head = self.snake_segments[0]

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seq_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seq_num - 1].xcor()
            new_y = self.snake_segments[seq_num - 1].ycor()
            self.snake_segments[seq_num].goto(new_x, new_y)

        self.head.fd(MOVE_STEP)

    def up(self):
        if self.head.heading() in ALLOW_DIRECTIONS['up']:
            self.head.seth(DIRECTION['up'])

    def down(self):
        if self.head.heading() in ALLOW_DIRECTIONS['down']:
            self.head.seth(DIRECTION['down'])

    def left(self):

        if self.head.heading() in ALLOW_DIRECTIONS['left']:
            self.head.seth(DIRECTION['left'])

    def right(self):
        if self.head.heading() in ALLOW_DIRECTIONS['right']:
            self.head.seth(DIRECTION['right'])

    def mirror_position(self):
        if self.head.ycor() > 300 or self.head.ycor() < -300:
            self.head.goto(self.head.xcor(), self.head.ycor() * -1)
        elif self.head.xcor() > 300 or self.head.xcor() < -300:
            self.head.goto(self.head.xcor() * -1, self.head.ycor())

    def reset_snake(self):
        for seq in self.snake_segments:
            seq.goto(1000, 1000)
        self.snake_segments = []
        self.create_snake()

    def blink_snake(self, screen):
        for period in range(8):
            time.sleep(0.3)
            screen.update()
            for seq in self.snake_segments:
                if period % 2 == 0:
                    seq.color('white')
                else:
                    seq.color('black')

