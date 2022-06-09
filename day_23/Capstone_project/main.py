from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move, "Up")

game_over = False

while not game_over:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if car_manager.car_collision(player):
        game_over = True
        scoreboard.game_over()
    if player.ycor() == player.FINISH_Y_LINE:
        time.sleep(1)
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.update_speed()
        player.refresh()


screen.exitonclick()
