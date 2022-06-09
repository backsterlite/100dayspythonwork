import turtle

import pandas
import pandas as pd

df = pd.read_csv("50_states.csv")


correct_answer_count = 0
all_answer_count = df["state"].count()
correct_answers = []
user_try = 0

screen =  turtle.Screen()
screen.title("U.S.A states game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)

turtle.penup()
turtle.hideturtle()
turtle.color("black")

while user_try < 50:

    user_guess = screen.textinput(title=f"{correct_answer_count}/{all_answer_count} correct answers", prompt="What next state?").title()

    if user_guess == "Exit":
        ca = df.state[~df.state.isin(correct_answers)]
        ca.to_csv("missing_states.csv")
        break
    if user_guess not in correct_answers and user_guess in df["state"].values:
        new_x = int(df.x[df.state == user_guess])
        new_y = int(df.y[df.state == user_guess])
        correct_answers.append(user_guess)
        turtle.goto(new_x, new_y)
        turtle.write(f"{user_guess}", align="center", font=("Arial", 10, "normal"))
        correct_answer_count += 1
        user_try += 1

