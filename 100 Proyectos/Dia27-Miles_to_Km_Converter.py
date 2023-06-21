from tkinter import *

FONT = ("Arial", 12)
def calculator():
    miles_input = int(user_input.get())
    convert = str((miles_input * 1.61))
    km_result.config(text=convert)

window = Tk()
window.title("Miles to Km Converter")

window.config(padx=20, pady=20)

user_input = Entry()
user_input.config(width=5)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

equal_label = Label(text="is equal to:", font=FONT)
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_result = Label(text="0", font=FONT)
km_result.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)


window.mainloop()

