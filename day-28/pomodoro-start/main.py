# imports
import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    status_label.config(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
    count_down(0)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps <= 8:
        if reps % 8 == 0:
            count_down(10)
            status_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(5)
            status_label.config(text="Break", fg=PINK)
        else:
            count_down(20)
            status_label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps != 0 and reps % 2 == 0:
            check_label["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)


# Canvas
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# label 1
status_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
status_label.grid(row=0, column=1)

# Start Button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=0)

# Reset Button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=3)

# Label 2
check_label = Label(text="", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=4, column=1)

window.mainloop()
