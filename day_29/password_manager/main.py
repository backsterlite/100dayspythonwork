import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import string
from random import randint, choice, shuffle
import pyperclip
import os

DATA_PATH = 'data.txt'
default_email = ''
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
    password_list += [choice(string.digits) for _ in range(randint(2, 4))]
    password_list += [choice(string.punctuation) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(tk.END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    inputs = website, email, password
    if "" in inputs:
        messagebox.showwarning(title="Oops", message="You can't leave any fields empty")
        return None

    is_ok = messagebox.askokcancel(title=website, message=(f"You fill follow fields\nEmail/username:{email}\n"
                                                           f"Password:{password}\nYou want to save this?"))
    if is_ok:
        DATA_PATH = 'data.txt'
        if os.path.exists(DATA_PATH):
            file_mode = 'a'
        else:
            file_mode = 'w'

        with open(DATA_PATH, mode=file_mode) as data:
            data.write(f'{website} | {email} | {password}\n')
            web_input.delete(0, tk.END)
            password_input.delete(0, tk.END)



# ---------------------------- UI SETUP ------------------------------- #

#Create window
window = tk.Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

#Create canvas
password_canvas = tk.Canvas(width=200, height=200)
password_image = tk.PhotoImage(file='logo.png')
password_canvas.create_image(100, 100, image=password_image)

#Create Labels
web_label = tk.Label(text="Website")
email_label = tk.Label(text="Email/Username")
password_label = tk.Label(text="password")

#Create inputs
web_input = tk.Entry(width=35)
email_input = tk.Entry(width=35)
password_input = tk.Entry()

#Create buttons
g_password_button = tk.Button(text="Gen. Passwd.", command=generate_password)
submit_button = tk.Button(text="Save", width=35, command=save)
#Dispossition
password_canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
web_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)
g_password_button.grid(column=2, row=3)
submit_button.grid(column=1, row=4, columnspan=2)

if not os.path.exists(DATA_PATH):
    default_email = simpledialog.askstring(title="default email", prompt="Please enter your regular email/username:")
    if default_email:
        email_input.insert(tk.END, default_email)
else:
    with open(DATA_PATH, mode='r') as data:
        email = data.readline().split("|")[1]
        email_input.insert(tk.END, email)


window.mainloop()