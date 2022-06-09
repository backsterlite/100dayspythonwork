###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
rgb_colors.pop(0)
rgb_colors.pop(0)
rgb_colors.pop(2)
rgb_colors.pop(3)

tl = Turtle()
screen = Screen()

screen.colormode(255)
lines = 10
dotes = 10
tl.speed(6)
tl.penup()
tl.back(300)
tl.seth(270)
tl.fd(200)
tl.seth(0)
start_x, start_y = tl.position()

def draw_dots_line(dotes, current_x):
    for _ in range(dotes):
        current_x += 50
        tl.goto(current_x, start_y)
        tl.dot(20, random.choice(rgb_colors))


for _ in range(lines):
    tl.goto(start_x, start_y)
    current_x = start_x
    draw_dots_line(dotes, current_x)
    start_y = start_y + 50


screen.exitonclick()

