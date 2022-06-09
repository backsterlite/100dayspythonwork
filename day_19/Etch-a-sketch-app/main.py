from turtle import Turtle, Screen

t = Turtle('turtle')
t.color("red")
screen = Screen()


def key_w():
    t.fd(10)


def key_s():
    t.back(10)


def key_a():
    t.left(10)


def key_d():
    t.right(10)


def key_c():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()

screen.onkey(key_w, 'Up')
screen.onkey(key_s, 'Down')
screen.onkey(key_a, 'Left')
screen.onkey(key_d, 'Right')
screen.onkey(key_c, 'c')
screen.exitonclick()