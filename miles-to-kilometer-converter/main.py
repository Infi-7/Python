from tkinter import *

converter_win = Tk()
converter_win.title("Miles to Kilometer Converter")
converter_win.minsize(width=300, height=200)
converter_win.config(pady=20, padx=20, background="black")

# input
user_input = Entry()
user_input.grid(row=0, column=3)

# label 1
label_1 = Label(text="Miles")
label_1.config(padx=10, pady=10, background="black")
label_1.grid(row=0, column=6)

# label 2
label_2 = Label(text="is equal to")
label_2.config(padx=10, pady=10, background="black", foreground="white")
label_2.grid(row=1, column=0)

# label 3
label_3 = Label(text="0")
label_3.config(padx=10, pady=10, background="black", foreground="white")
label_3.grid(row=1, column=3)

# label 4
label_4 = Label(text="Km")
label_4.config(padx=10, pady=10, background="black", foreground="white")
label_4.grid(row=1, column=6)


# Button click function
def button_click():
    temp = user_input.get()
    result = int(temp) * 1.609344
    label_3["text"] = f"{round(result, 4)}"


# Button
calculate_button = Button(text="Calculate", command=button_click)
calculate_button.grid(row=2, column=3)
calculate_button.config(padx=10, pady=10)

converter_win.mainloop()
