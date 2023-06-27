from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
WHITE = "#FFFFFF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
    passwd_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    passwd_input.insert(0, password)
    pass_copied_label.config(text="The password has been copied to your clipboard.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    passwd = passwd_input.get()

    if website == "" or email == "" or passwd == "":
        messagebox.showerror(title="Error!", message="Please do not leave any field empty.")
    if " " in website:
        messagebox.showerror(title="No Spaces", message="The website field must not contain spaces")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:\nWebsite: {website}\n"
                                                              f"User Name: {email}\nPassword: {passwd}")
        if is_ok:
            with open("data.txt", mode="a") as new_data:
                new_data.write(f"{website} | {email} | {passwd}\n")
                website_input.delete(0, END)
                passwd_input.delete(0, END)
                pass_copied_label.config(text="")
                website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

passwd_label = Label(text="Password:")
passwd_label.grid(row=3, column=0)

pass_copied_label = Label(text="", font=("Arial", 8, "italic"))
pass_copied_label.grid(row=5, column=1, columnspan=2)

#Imputs
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

username_input = Entry(width=35)
username_input.insert(0, "micorreo@midominio.com")
username_input.grid(row=2, column=1, columnspan=2)

passwd_input = Entry(width=21)
passwd_input.grid(row=3, column=1)

#Buttons
gen_passed_button = Button(text="Generate Password", command=generate_pass)
gen_passed_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
