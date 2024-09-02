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

canvas.grid(row=0, column=0)

window.mainloop()
