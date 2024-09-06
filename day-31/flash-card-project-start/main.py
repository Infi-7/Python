from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI

# Window Settings
window = Tk()
window.title("Flashy")
window.minsize(width=200, height=200)
window.config(bg=BACKGROUND_COLOR, padx=50)

# Canvas Settings
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
guess_check = PhotoImage(file="./images/right.png")
guess_wrong = PhotoImage(file="./images/wrong.png")

canvas.create_image(400, 265, image= card_back)
canvas.grid(row=0, column=0,columnspan=2)

canvas.create_image(400, 265, image= card_front)
canvas.grid(row=0, column=1)

# Wrong Button
button_wrong = Button(image=guess_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=0, sticky="w",columnspan=2)

# Check Button
check_wrong = Button(image=guess_check, highlightthickness=0)
check_wrong.grid(row=1, column=1, sticky="e")


mainloop()
