from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.grid(row=0, column=0)
my_label.config(pady=50, padx=50)

# Button


def button_clicked():
    user_input = inp.get()

    my_label["text"] = f"{str(user_input)}"


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# New Button

new_button = Button(text="Click Me")
new_button.grid(row=0, column=2)

# Input

inp = Entry()
inp.grid(row=2, column=3)


window.mainloop()
