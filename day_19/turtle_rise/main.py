from turtle import Turtle, Screen
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
is_on = False
turtles = [Turtle(shape='turtle') for c in colors]
screen = Screen()
screen.setup(width=500, height=400)
start_x = -230
start_y = -100
screen.title('turtle rises')
user_bit = screen.textinput("Chose your bet", "Who is win. Pick a color: ")


def out_of_screen(turtle):
    x, y = turtle.position()
    return x > screen.window_width()//2 - 20 or x < -(screen.window_width()//2) + 20\
            or y > screen.window_height()//2 - 20 or y < -(screen.window_height()//2) + 20


for i, t in enumerate(turtles):
    t.penup()
    t.color(colors[i])
    t.goto(start_x, start_y)
    t.speed(3)
    start_y += 30
if user_bit:
    is_on = True

while is_on:
    for turtle in turtles:
        if out_of_screen(turtle):
            if turtle.pencolor() == user_bit:
                print(f"You are win! {turtle.pencolor()} turtle is a win")
            else:
                print(f"You are lose! {turtle.pencolor()} turtle is a win")
            is_on = False
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
screen.exitonclick()
