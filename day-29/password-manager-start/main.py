# imports
from tkinter import *

# variables
WIDTH = 200
HEIGHT = 200
PADDING = 50

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP -------------------------------#
# main Window
window = Tk()
window.title("Password Manager")
window.config(pady=PADDING, padx=PADDING)

# canvas
canvas = Canvas(height=HEIGHT, width=WIDTH)
img = PhotoImage(file="logo.png")
canvas.create_image(65, HEIGHT/2, image=img)
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
text_website = Entry(width=40)
text_website.grid(row=1, column=1, columnspan=2, stick="W")

# Username/Email Textbox
text_user_email = Entry(width=40)
text_user_email.grid(row=2, column=1, columnspan=2, stick="W")

# Password Textbox
text_password = Entry(width=21)
text_password.grid(row=3, column=1, columnspan=2, stick="W")

# Add button
button_add = Button(text="Add", width=33)
button_add.grid(row=4, column=1, padx=PADDING - 47, pady=PADDING - 47, columnspan=2, sticky="W")

# Generate Button
button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3, column=1, stick="E",columnspan=2)

window.mainloop()
