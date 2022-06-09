from turtle import Turtle, Screen
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
MOVE_DISTANCE_START = 5
MOVE_DISTANCE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = MOVE_DISTANCE_START

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.seth(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.fd(self.move_distance)

    def car_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 30:
                return True
        return False

    def update_speed(self):
        self.move_distance += MOVE_DISTANCE_INCREMENT

