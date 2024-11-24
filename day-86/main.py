import time
import random
import tkinter
from tkinter import *
from tkinter import messagebox

MIN_WIDTH = 300
MIN_HEIGHT = 200
WIDTH = 900
HEIGHT = 600

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language.",
    "Typing speed tests are fun and engaging.",
    "Always practice to improve your typing skills.",
    "A journey of a thousand miles begins with a single step.",
    "Coding is a skill that requires patience and practice.",
    "An apple a day keeps the doctor away.",
    "Success is the sum of small efforts repeated daily.",
    "Never stop learning because life never stops teaching.",
    "The cat sat on the mat and stared at the door.",
    "Good things come to those who work hard and stay consistent.",
    "The stars shine brightest when the night is the darkest.",
    "A goal without a plan is just a wish waiting to happen.",
    "Happiness is a journey, not a destination.",
    "Dream big, work hard, and stay humble always.",
]

class SpeedTester:
    def __init__(self, window):
        self.window = window

        self.start = None
        self.displayed_sentence = StringVar()
        self.user_input = StringVar()
        self.result_label = None

        header_label = Label(window, text="Typing Speed Test")
        header_label.pack(pady=10)

        self.sentence_label = Label(window, textvariable=self.displayed_sentence,
                                    wraplength=500, justify="center")
        self.sentence_label.pack(pady=10)

        user_input = Entry(window, textvariable=self.user_input, width=50)
        user_input.pack(pady=10)

        self.start_button = Button(window, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.submit_button = Button(window, text="Submit", command=self.calculate_result)
        self.submit_button.pack(pady=5)
        self.submit_button.config(state=DISABLED)

    def start_test(self):
        self.displayed_sentence.set(random.choice(sentences))
        self.user_input.set("")

        self.submit_button.config(state=NORMAL)
        self.start = time.time()
        self.result = None
        messagebox.showinfo("Start Typing","Type as fast as possible.")

    def calculate_result(self):
        if not self.start:
            return

        time_taken = time.time() - self.start
        words = len(self.displayed_sentence.get().split())
        words_per_min = round((words/ time_taken) * 60, 2)

        user_text = self.user_input.get()
        og_text = self.displayed_sentence.get()
        correct_chars = sum(1 for o,u in zip(og_text, user_text) if o==u)
        acc = round((correct_chars/len(og_text)) * 100, 2)

        result_text = f"Typing Speed: {words_per_min} WPM \nAccuracy :{acc}%"
        self.result_label = tkinter.Label(self.window, text=result_text, fg="red")
        self.result_label.pack(pady=10)

        self.submit_button.config(state=DISABLED)


window = Tk()
SpeedTester(window)
window.mainloop()