# imports
import json
import string
from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# variables
WIDTH = 200
HEIGHT = 200
PADDING = 50
PASS = ''


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    global PASS
    text_password.delete(0, len(text_password.get()))
    PASS = ""
    for _ in range(0, 10):
        var1 = random.randint(0, 2)
        if var1 == 0:
            PASS += string.ascii_lowercase[random.randint(0, 25)]
        elif var1 == 1:
            PASS += string.ascii_uppercase[random.randint(0, 25)]
        else:
            PASS += string.digits[random.randint(0, 9)]

    text_password.insert(0, PASS)
    pyperclip.copy(PASS)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = text_website.get()
    email = text_user_email.get()
    password = text_password.get()

    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo("Oops!", "Please don't leave any field empty!")

    else:

        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)

            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)

        finally:
            text_website.delete(0, len(website))
            text_password.delete(0, len(password))


# ---------------------------- UI SETUP -------------------------------#
# main Window
window = Tk()
window.title("Password Manager")
window.config(pady=PADDING, padx=PADDING)

# canvas
canvas = Canvas(height=HEIGHT, width=WIDTH)
img = PhotoImage(file="logo.png")
canvas.create_image(65, HEIGHT / 2, image=img)
canvas.grid(row=0, column=1)

# Website Label
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0, padx=PADDING - 47, pady=PADDING - 47)

# Username/Email Label
label_user_email = Label(text="Email/Username: ")
label_user_email.grid(row=2, column=0, padx=PADDING - 47, pady=PADDING - 47)

# Password Label
label_password = Label(text="Password: ")
label_password.grid(row=3, column=0, padx=PADDING - 47, pady=PADDING - 47)

# Website Textbox
text_website = Entry(width=40, highlightthickness=0)
text_website.focus()
text_website.grid(row=1, column=1, columnspan=2, stick="W")

# Username/Email Textbox
text_user_email = Entry(width=40, highlightthickness=0)
text_user_email.insert(0, "abc@gmail.com")
text_user_email.grid(row=2, column=1, columnspan=2, stick="W")

# Password Textbox
text_password = Entry(width=21, highlightthickness=0)
text_password.grid(row=3, column=1, columnspan=2, stick="W")

# Add button
button_add = Button(text="Add", width=33, highlightthickness=0, borderwidth=0.5, command=save)
button_add.grid(row=4, column=1, padx=PADDING - 47, pady=PADDING - 47, columnspan=2, sticky="W")

# Generate Button
button_generate_password = Button(text="Generate Password", highlightthickness=0, borderwidth=0.5,
                                  command=password_generator)
button_generate_password.grid(row=3, column=1, stick="E", columnspan=2)

window.mainloop()
