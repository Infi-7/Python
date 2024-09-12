from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        image_check = PhotoImage(file="./images/true.png")
        image_cross = PhotoImage(file="./images/false.png")

        self.button_1 = Button(image=image_check, width=100, height=97, highlightthickness=0)
        self.button_1.grid(row=2, column=0, padx=20, pady=20)

        self.button_2 = Button(image=image_cross, width=100, height=97, highlightthickness=0)
        self.button_2.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()
