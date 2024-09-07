import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
QUESTION = ""
ANSWER = ""
correct = []
skipped = []
RNG = 0

# Main code
og_df = pd.read_csv("./data/french_words.csv")
df = og_df.to_dict()


def word_display():
    global RNG, QUESTION, ANSWER, flip_timer
    RNG = 0
    QUESTION = ""
    ANSWER = ""
    RNG = random.randint(0, len(og_df) - 1)

    canvas_main.itemconfig(image_display, image=card_front)
    if len(correct) == 0 or RNG not in correct or RNG in skipped:
        window.after_cancel(flip_timer)
        QUESTION = df["French"][RNG]
        ANSWER = df["English"][RNG]
        canvas_main.itemconfig(replace_language, text="French", fill="black")
        canvas_main.itemconfig(replace_words, text=QUESTION, fill="black")
        flip_timer = window.after(3000, func=display_translated)


def display_translated():
    canvas_main.itemconfig(replace_language, text="English", fill="white")
    canvas_main.itemconfig(replace_words, text=ANSWER, fill="white")
    canvas_main.itemconfig(image_display, image=card_back)


def correct_guess():
    word_display()
    correct.append(RNG)


def skipped_word():
    skipped.append(RNG)
    word_display()


# UI
# Window Settings
window = Tk()
window.title("Flashy")
window.minsize(width=200, height=200)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=display_translated)

# Main Canvas Settings
canvas_main = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
guess_check = PhotoImage(file="./images/right.png")
guess_wrong = PhotoImage(file="./images/wrong.png")

image_display = canvas_main.create_image(400, 265, image=card_front)
replace_language = canvas_main.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
replace_words = canvas_main.create_text(400, 263, text=f"{QUESTION}", font=("Ariel", 60, "bold"))
word_display()
canvas_main.grid(row=0, column=0, columnspan=2)

# Wrong Button
button_wrong = Button(image=guess_wrong, highlightthickness=0, command=skipped_word)
button_wrong.grid(row=1, column=0)

# Check Button
button_check = Button(image=guess_check, highlightthickness=0, command=correct_guess)
button_check.grid(row=1, column=1)

window.mainloop()
