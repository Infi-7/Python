# imports
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# Canvas
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=img)
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# label 1
timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

# Start Button
start = Button(text="Start")
start.grid(row=3, column=0)

# Reset Button
reset = Button(text="Reset")
reset.grid(row=3, column=3)

# Label 2
check_label = Label(text="✔", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=4, column=1)

window.mainloop()
