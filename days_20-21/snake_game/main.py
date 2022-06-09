from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def out_of_screen(turtle):
    x, y = turtle.position()
    return x > screen.window_width()//2 - 10 or x < -(screen.window_width()//2) + 10 \
            or y > screen.window_height()//2 - 10 or y < -(screen.window_height()//2) + 10


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("SNAKE GAME")
screen.listen()

game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score = scoreboard.score + 1
        scoreboard.update_score()
    if out_of_screen(snake.head):
        game_is_on = False
        scoreboard.game_over()
    # collision with tail
    for seq in snake.snake_segments[1::]:
        if snake.head.distance(seq) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
