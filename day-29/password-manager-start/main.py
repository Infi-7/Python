# imports
from tkinter import *

# variables
WIDTH = 200
HEIGHT = 200
PADDING = 20

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
canvas.create_image(WIDTH/2, HEIGHT/2, image=img)
canvas.grid(row=0, column=1)

# Website Label
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0)

# Username/Email Label
label_user_email = Label(text="Email/Username: ")
label_user_email.grid(row=2, column=0)

# Password Label
label_password = Label(text="Password: ")
label_password.grid(row=3, column=0)

# Website Textbox
text_website = Entry(width=35)
text_website.grid(row=1, column=1)

# Username/Email Textbox
text_user_email = Entry(width=35)
text_user_email.grid(row=2, column=1)

# Password Textbox
text_password = Entry(width=21)
text_password.grid(row=3, column=1)

# Add button
button_add = Button(text="Add", width=35)
button_add.grid(row=4, column=1)

# Generate Button
button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3, column=2)

window.mainloop()
