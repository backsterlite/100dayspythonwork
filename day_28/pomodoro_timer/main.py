import tkinter as tk
import time
from datetime import datetime
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
ROUND_MARK = u'\u2713'
reps = 0
coef = 1
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer
    if timer:
        window.after_cancel(timer)
    img_canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    round_marker.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps < 9:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    if count > 0:
        min, sec = divmod(count, 60)
        if sec < 10:
            sec = f"0{sec}"
        img_canvas.itemconfig(canvas_text, text =f"{min}:{sec}")
        timer = window.after(100,count_down, count - 1)
    else:
        global coef
        timer_start()
        if reps % 2 == 0:
            round_marker.config(text=f"{ROUND_MARK}" * coef)
            coef += 1
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas
img_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = tk.PhotoImage(file='tomato.png')
img_canvas.create_image(100, 112, image=pomodoro_img)
canvas_text = img_canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 20, "bold"))

# create timer
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 36, 'normal'), fg=GREEN, bg=YELLOW)

# create start button
start_button = tk.Button(text="start", command=timer_start, highlightthickness=0)

# create reset button
reset_button = tk.Button(text="reset", command=timer_reset, highlightthickness=0)

#create round marker
round_marker = tk.Label(font=(FONT_NAME, 18, 'bold'), fg=GREEN, bg=YELLOW)

# disposition
timer_label.grid(column=1, row=0)
img_canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
round_marker.grid(column=1, row=4)

window.mainloop()