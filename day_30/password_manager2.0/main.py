import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import string
from random import randint, choice, shuffle
import pyperclip
import os
import json

DATA_PATH = 'data.json'
default_email = ''

def search():
    key_str = web_input.get().lower()
    try:
        with open(DATA_PATH) as data_file:
            password_storage = json.load(data_file)
        result = password_storage[key_str]
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="Data  file not find")
    except KeyError as web_site:
        messagebox.showerror(title="Oops", message=f"Web site {web_site} not found in password storage")
    else:
        messagebox.showinfo(title=key_str, message=f"Email: {result['email']}\nPassword: {result['password']}")
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
    website = web_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    inputs = website, email, password
    if "" in inputs:
        messagebox.showwarning(title="Oops", message="You can't leave any fields empty")
        return None

    is_ok = messagebox.askokcancel(title=website, message=(f"You fill follow fields\nEmail/username:{email}\n"
                                                           f"Password:{password}\nYou want to save this?"))

    new_dict = {
        website: {
            "email": email,
            "password": password,
        }
    }
    data = {}
    if is_ok:
        try:
            with open(DATA_PATH, mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_dict
        else:
            data.update(new_dict)
        finally:
            with open(DATA_PATH, mode="w") as data_file:
                json.dump(data, data_file, indent=4)
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
web_input = tk.Entry(width=21)
email_input = tk.Entry(width=35)
password_input = tk.Entry()

#Create buttons
g_password_button = tk.Button(text="Gen. Passwd.", command=generate_password)
submit_button = tk.Button(text="Save", width=35, command=save)
search_button = tk.Button(text="Search", command=search)
#Dispossition
password_canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1, sticky=tk.W)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
web_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)
g_password_button.grid(column=2, row=3)
submit_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

if not os.path.exists(DATA_PATH):
    default_email = simpledialog.askstring(title="default email", prompt="Please enter your regular email/username:")
    if default_email:
        email_input.insert(tk.END, default_email)
else:
    with open(DATA_PATH, mode='r') as data:
        data = json.load(data)
        email = data[list(data.keys())[0]]["email"]
        email_input.insert(tk.END, email)


window.mainloop()