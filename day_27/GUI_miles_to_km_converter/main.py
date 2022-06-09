import tkinter as tk

def calculate():
    miles = float(miles_entry.get())
    km = round(miles * 1.6, 2)
    km_result.config(text=km)

window = tk.Tk()
window.config(padx=20, pady=20)
window.title('miles to km')


label_equal = tk.Label(text="is equal to")

miles_entry = tk.Entry(width=10)
miles_entry.insert(0, "0")

miles_description = tk.Label(text="Miles")
km_description = tk.Label(text="Km")

km_result = tk.Label(text="0")

calc_button = tk.Button(text="calculate", command=calculate)

label_equal.grid(column=0, row=1)
miles_entry.grid(column=1, row=0)
miles_description.grid(column=2, row=0)
km_description.grid(column=2, row=1)
km_result.grid(column=1, row=1)
calc_button.grid(column=1, row=2)

window.mainloop()