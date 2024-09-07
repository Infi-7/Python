from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI

# Window Settings
window = Tk()
window.title("Flashy")
window.minsize(width=200, height=200)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Main Canvas Settings
canvas_main = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
guess_check = PhotoImage(file="./images/right.png")
guess_wrong = PhotoImage(file="./images/wrong.png")

canvas_main.create_image(400, 265, image=card_front)
canvas_main.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_main.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas_main.grid(row=0, column=0, columnspan=2)

# Wrong Button
button_wrong = Button(image=guess_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=0)

# Check Button
button_check = Button(image=guess_check, highlightthickness=0)
button_check.grid(row=1, column=1)


window.mainloop()
