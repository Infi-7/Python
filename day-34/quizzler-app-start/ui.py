from tabnanny import check
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        image_check = PhotoImage(file="./images/true.png")
        image_cross = PhotoImage(file="./images/false.png")

        self.button_1 = Button(image=image_check, width=100, height=97, highlightthickness=0, command=self.true_pressed)
        self.button_1.grid(row=2, column=0, padx=20, pady=20)

        self.button_2 = Button(image=image_cross, width=100, height=97, highlightthickness=0, command=self.false_pressed)
        self.button_2.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score is: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz!")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

