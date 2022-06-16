import os
from random import choice
import pandas as pd
import tkinter as tk
import builtins
BACKGROUND_COLOR = "#B1DDC6"
right_words = []
current_word = {}
timer = ""

def before_close(event=None):
    global right_words
    df = pd.DataFrame(right_words)
    df.to_csv("./data/learned_words.csv", index=False)
    root.destroy()

def click_right(card_list):
    global right_words, current_word
    right_words.append(current_word)
    create_card(card_list)

def click_wrong(card_list): create_card(card_list)

def create_card(card_list):
    global current_word, timer
    current_word = choice(card_list)
    card_list.remove(current_word)
    card_canvas.itemconfig(card_container, image=front_card)
    card_canvas.itemconfig(card_label, text='English', fill="black")
    card_canvas.itemconfig(card_word, text=current_word['English'], fill="black")
    timer = root.after(3000, flip_card)

def flip_card(event=None):
    global current_word, timer
    if timer: root.after_cancel(timer)
    card_key, label, fill_color = (back_card, "Ukrainian", 'white') if  card_canvas.itemcget(card_container, "image") == "pyimage1" else (front_card, "English", 'black')
    card_canvas.itemconfig(card_container, image=card_key)
    card_canvas.itemconfig(card_label, text=label, fill=fill_color)
    card_canvas.itemconfig(card_word, text=current_word[label], fill=fill_color)
# ---------------------------- READ WORDS ------------------------------- #
df = pd.read_csv("./data/Ukrainian_words.csv")
if os.path.exists("./data/learned_words.csv"):
    learned_words = pd.read_csv("./data/learned_words.csv")
    learned_list = learned_words["Ukrainian"].tolist()
    right_words.extend(learned_words.to_dict(orient="records"))
    df = df[~df["Ukrainian"].isin(learned_list)]
words = df.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Learn Words")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.bind('<Button-1>', flip_card)
front_card = tk.PhotoImage(file="./images/card_front.png")
back_card = tk.PhotoImage(file="./images/card_back.png")
card_container = card_canvas.create_image(400, 263, image=front_card)
card_label = card_canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

wrong_image = tk.PhotoImage(file="./images/wrong.png")
right_image = tk.PhotoImage(file="./images/right.png")

wrong_button = tk.Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: click_wrong(words))
right_button = tk.Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda: click_right(words))

card_canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

create_card(words)
root.bind("<Escape>", before_close)
root.protocol("WM_DELETE_WINDOW", before_close)
root.mainloop()
