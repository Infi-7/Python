from tkinter import *

converter_win = Tk()
converter_win.title("Miles to Kilometer Converter")
converter_win.minsize(width=300, height=200)
converter_win.config(pady=20, padx=20, background="black")

# theme changer
choices = ["Light", "Dark"]
variable = StringVar()
variable.set(choices[0])


def theme_changer():
    if variable.get() == "Light":
        converter_win.config(background="white")
        label_1.config(background="white", foreground="black")
        label_2.config(background="white", foreground="black")
        label_3.config(background="white", foreground="black")
        label_4.config(background="white", foreground="black")
    elif variable.get() == "Dark":
        converter_win.config(background="black")
        label_1.config(background="black", foreground="white")
        label_2.config(background="black", foreground="white")
        label_3.config(background="black", foreground="white")
        label_4.config(background="black", foreground="white")


# button to change theme
theme_chang_button = Button(command=theme_changer)
theme_chang_button.config(pady=10, padx=10)
theme_chang_button.grid(row=0, column=8)

theme_choice = OptionMenu(converter_win, variable, *choices)
theme_choice.config(padx=10, pady=10)
theme_choice.grid(row=0, column=6)


# input
user_input = Entry()
user_input.grid(row=1, column=3)

# label 1
label_1 = Label(text="Miles")
label_1.config(padx=10, pady=10, background="black", foreground="white")
label_1.grid(row=1, column=6)

# label 2
label_2 = Label(text="is equal to")
label_2.config(padx=10, pady=10, background="black", foreground="white")
label_2.grid(row=2, column=0)

# label 3
label_3 = Label(text="0")
label_3.config(padx=10, pady=10, background="black", foreground="white")
label_3.grid(row=2, column=3)

# label 4
label_4 = Label(text="Km")
label_4.config(padx=10, pady=10, background="black", foreground="white")
label_4.grid(row=2, column=6)


# Button click function
def button_click():
    temp = user_input.get()
    result = int(temp) * 1.609344
    label_3["text"] = f"{round(result, 4)}"


# Button
calculate_button = Button(text="Calculate", command=button_click)
calculate_button.grid(row=3, column=3)
calculate_button.config(padx=10, pady=10)

theme_changer()

converter_win.mainloop()
